"""Offline unit and CLI boundary tests. Run: python -m unittest discover -s scripts -p 'test_*.py' -v"""
import copy
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

import supply_model as sm


def fixture():
    return {
        "token_symbol": "DEMO", "token_decimals": 0, "horizon_months": 48,
        "genesis_supply_units": "1000", "outstanding_cap_units": "1400",
        "allocations": [
            {"id": "team", "cohort": "team", "amount_units": "300", "tge_unlocked_units": "0", "cliff_months": 12, "linear_months": 36},
            {"id": "community", "cohort": "community", "amount_units": "700", "tge_unlocked_units": "200", "cliff_months": 0, "linear_months": 12},
        ],
        "emissions": [{"id": "rewards", "from_month": 1, "through_month": 24, "monthly_units": "5"}],
        "burns": [{"id": "fees", "from_month": 1, "through_month": 24, "monthly_units": "1"}],
        "scenarios": [
            {"name": "base", "emission_multiplier": "1", "burn_multiplier": "1", "extra_mints": []},
            {"name": "low-usage", "emission_multiplier": "1", "burn_multiplier": "0", "extra_mints": []},
            {"name": "admin-mint", "emission_multiplier": "1", "burn_multiplier": "1", "extra_mints": [{"month": 12, "amount_units": "100"}]},
        ],
    }


class SupplyModelTests(unittest.TestCase):
    def test_tge_cliff_and_full_release_with_dust(self):
        m = sm.parse(fixture())
        rows, _ = sm.simulate(m, m["cases"][0])
        self.assertEqual(rows[0]["circulating_units"], 200)
        self.assertEqual(rows[12]["unlock_team_units"], 0)
        self.assertEqual(rows[13]["unlock_team_units"], 8)
        self.assertEqual(rows[48]["unlock_team_units"], 9)
        self.assertEqual(rows[48]["genesis_locked_units"], 0)
        self.assertEqual(sum(r["unlock_team_units"] for r in rows), 300)

    def test_supply_conservation_for_all_scenarios_every_month(self):
        m = sm.parse(fixture())
        for case in m["cases"]:
            rows, summary = sm.simulate(m, case)
            self.assertEqual(len(rows), 49)
            for r in rows:
                self.assertEqual(r["outstanding_units"], r["genesis_locked_units"] + r["circulating_units"])
            self.assertIn("not_verified", summary["status"])

    def test_original_genesis_supply_not_double_minted_at_tge(self):
        rows, _ = sm.simulate(sm.parse(fixture()), sm.parse(fixture())["cases"][0])
        self.assertEqual(rows[0]["outstanding_units"], 1000)
        self.assertEqual(rows[0]["unlock_community_units"], 200)
        self.assertEqual(rows[0]["unlock_existing_units"], 0)

    def test_emissions_vs_vesting_distinct(self):
        m = sm.parse(fixture())
        rows, _ = sm.simulate(m, m["cases"][0])
        self.assertEqual(rows[1]["unlock_existing_units"], 41)
        self.assertEqual(rows[1]["new_emissions_units"], 5)
        self.assertEqual(rows[1]["outstanding_units"], 1004)
        self.assertEqual(rows[1]["circulating_units"], 245)

    def test_scenario_stress_burn_difference(self):
        m = sm.parse(fixture())
        base, _ = sm.simulate(m, m["cases"][0])
        zero_burn, _ = sm.simulate(m, m["cases"][1])
        self.assertEqual(zero_burn[24]["outstanding_units"] - base[24]["outstanding_units"], 24)

    def test_multiplier_rounds_down_each_month(self):
        d = fixture()
        d["scenarios"] = [{"name": "half", "emission_multiplier": "0.5"}]
        d["emissions"][0]["monthly_units"] = "5"
        m = sm.parse(d)
        rows, _ = sm.simulate(m, m["cases"][0])
        self.assertEqual(rows[1]["new_emissions_units"], 2)

    def test_78_digit_supply_preserves_last_base_units(self):
        n = 10 ** 76 + 9
        self.assertEqual(sm.scaled(n, sm.factor("0.5", "fraction")), n // 2)
        self.assertEqual(sm.scaled(n, sm.factor("1", "fraction")), n)

    def test_cliff_only_lump_occurs_after_full_cliff(self):
        d = fixture()
        d["allocations"][0]["linear_months"] = 0
        m = sm.parse(d)
        rows, _ = sm.simulate(m, m["cases"][0])
        self.assertEqual(rows[12]["unlock_team_units"], 0)
        self.assertEqual(rows[13]["unlock_team_units"], 300)

    def test_incomplete_allocations_fail_closed(self):
        d = fixture()
        d["allocations"][0]["amount_units"] = "301"
        with self.assertRaisesRegex(sm.ModelError, "sum exactly"):
            sm.parse(d)

    def test_tge_over_allocation_rejected(self):
        d = fixture()
        d["allocations"][0]["tge_unlocked_units"] = "301"
        with self.assertRaisesRegex(sm.ModelError, "TGE"):
            sm.parse(d)

    def test_invalid_units_rejected_not_float(self):
        for value in (1000, "1.00", "-1", "1e6"):
            d = fixture()
            d["genesis_supply_units"] = value
            with self.subTest(value=value), self.assertRaises(sm.ModelError):
                sm.parse(d)

    def test_undefined_shock_is_null(self):
        d = fixture()
        for a in d["allocations"]:
            a["tge_unlocked_units"] = "0"
        m = sm.parse(d)
        rows, _ = sm.simulate(m, m["cases"][0])
        self.assertIsNone(rows[1]["unlock_shock_pct"])
        self.assertIsNone(rows[1]["mint_shock_pct"])

    def test_unauthorized_cap_overrun_rejected_before_burn(self):
        d = fixture()
        d["outstanding_cap_units"] = "1002"
        m = sm.parse(d)
        with self.assertRaisesRegex(sm.ModelError, "before burn"):
            sm.simulate(m, m["cases"][0])

    def test_cap_bypass_explicit_and_flagged(self):
        d = fixture()
        d["outstanding_cap_units"] = "1002"
        d["scenarios"] = [{"name": "counterfactual", "assume_cap_bypass": True}]
        m = sm.parse(d)
        _, result = sm.simulate(m, m["cases"][0])
        self.assertTrue(result["cap_breach_months"])
        self.assertTrue(result["assume_cap_bypass"])

    def test_burn_cannot_exceed_available_circulation(self):
        d = fixture()
        d["burns"][0]["monthly_units"] = "10000"
        m = sm.parse(d)
        with self.assertRaisesRegex(sm.ModelError, "burns exceed"):
            sm.simulate(m, m["cases"][0])

    def test_monthly_data_month_36_at_least(self):
        d = fixture()
        d["horizon_months"] = 35
        with self.assertRaises(sm.ModelError):
            sm.parse(d)

    def test_slug_prevents_path_traversal(self):
        d = fixture()
        d["scenarios"][0]["name"] = "../../outside"
        with self.assertRaises(sm.ModelError):
            sm.parse(d)

    def test_cli_writes_then_refuses_to_overwrite(self):
        with tempfile.TemporaryDirectory() as temp:
            input_path = Path(temp) / "case.json"
            output = Path(temp) / "reports"
            input_path.write_text(json.dumps(fixture()), encoding="utf-8")
            cmd = [sys.executable, str(Path(sm.__file__)), "--input", str(input_path), "--output-dir", str(output)]
            first = subprocess.run(cmd, capture_output=True, text=True)
            self.assertEqual(first.returncode, 0, first.stderr)
            self.assertTrue((output / "monthly_base.csv").is_file())
            self.assertEqual(len((output / "monthly_base.csv").read_text().splitlines()), 50)
            second = subprocess.run(cmd, capture_output=True, text=True)
            self.assertEqual(second.returncode, 2)
            self.assertIn("refusing to overwrite", second.stderr)

    def test_cli_invalid_model_leaves_no_outputs(self):
        with tempfile.TemporaryDirectory() as temp:
            d = fixture()
            d["outstanding_cap_units"] = "1002"
            path = Path(temp) / "bad.json"
            path.write_text(json.dumps(d), encoding="utf-8")
            dest = Path(temp) / "reports"
            cmd = [sys.executable, str(Path(sm.__file__)), "--input", str(path), "--output-dir", str(dest)]
            res = subprocess.run(cmd, capture_output=True, text=True)
            self.assertEqual(res.returncode, 2)
            self.assertFalse(dest.exists())


if __name__ == "__main__":
    unittest.main()
