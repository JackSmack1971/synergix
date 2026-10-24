#!/usr/bin/env python3
"""Synthetic regression cases for the report's mechanical guard."""

import unittest
from validate_report import validate


SECTIONS = [
    "Executive summary", "Scope and assumptions", "Threat model and invariants",
    "Findings", "Centralization and trust risks", "Invariant, test, and OWASP coverage",
    "Discarded candidates", "Appendix",
]


def sample(status="INCOMPLETE", finding="", coverage="| auth | SCSVS-A-1 | NOT TESTED | Source HTML; cannot inspect Solidity | — |"):
    body = f"STATUS: {status}\n"
    if status == "INCOMPLETE":
        body += "Blocker: missing Solidity source\n"
    for n, heading in enumerate(SECTIONS, 1):
        body += f"\n## {n}. {heading}\n\n"
        if n == 4:
            body += finding
        elif n == 6:
            body += "| Category | Control/test | Status | Evidence | Finding |\n|---|---|---|---|---|\n"
            body += coverage + "\n"
        else:
            body += "Evidence limited by source availability.\n"
    return body


FINDING = """### M-01 Unprotected path

Severity: Medium
Impact: Medium
Likelihood: Medium
Confidence: Inferred
Calibration: [INFERRED: code-path reasoning]
SCWE: SCWE-001 https://scs.owasp.org/SCWE/
SCSVS: SCSVS-A-1
Locations: contracts/Example.sol:21 and guard contracts/Example.sol:18
Root cause: Missing control
Attack scenario: Actor calls function after valid preconditions
PoC: UNEXECUTED
Falsification: Existing guard was checked and rejected
Impact detail: Limited effect
Recommendation: Add the narrow guard
Regression risk: Behavior changes for previous callers
Status: OPEN
"""


class ValidatorTests(unittest.TestCase):
    def test_blocked_audit_is_valid(self):
        self.assertEqual([], validate(sample()))

    def test_complete_moderate_finding(self):
        coverage = "| auth | SCSVS-A-1 | PASS | contracts/Example.sol:21 | — |"
        self.assertEqual([], validate(sample("COMPLETE", FINDING, coverage)))

    def test_complete_high_with_local_poc(self):
        high = (FINDING.replace("M-01", "H-01")
                .replace("Severity: Medium", "Severity: High")
                .replace("Calibration: [INFERRED: code-path reasoning]", "Calibration: [VERIFIED: PoC executed + output]")
                .replace("PoC: UNEXECUTED", "PoC: EXECUTED test/poc/H-01.test.js; captured output in Appendix"))
        coverage = "| auth | SCSVS-A-1 | PASS | contracts/Example.sol:21 | — |"
        self.assertEqual([], validate(sample("COMPLETE", high, coverage)))

    def test_missing_section(self):
        self.assertTrue(any("headings" in p for p in validate(sample().replace("## 8. Appendix", "## 9. Appendix"))))

    def test_pass_requires_evidence(self):
        bad = sample(coverage="| auth | SCSVS-A-1 | PASS | README | — |")
        self.assertTrue(any("file:line" in p for p in validate(bad)))

    def test_critical_high_require_executed_poc(self):
        bad = sample("COMPLETE", FINDING.replace("M-01", "H-01"), "| auth | SCSVS-A-1 | PASS | contracts/Example.sol:21 | — |")
        self.assertTrue(any("EXECUTED PoC" in p for p in validate(bad)))

    def test_finding_requires_guard_citation_or_search(self):
        bad = sample("COMPLETE", FINDING.replace(" and guard contracts/Example.sol:18", ""),
                     "| auth | SCSVS-A-1 | PASS | contracts/Example.sol:21 | — |")
        self.assertTrue(any("guard citation" in p for p in validate(bad)))

    def test_complete_cannot_have_not_tested(self):
        self.assertTrue(any("NOT TESTED control" in p for p in validate(sample("COMPLETE"))))

    def test_duplicate_finding_ids(self):
        self.assertTrue(any("Duplicate" in p for p in validate(sample(finding=FINDING + FINDING))))

    def test_failed_control_must_link_to_retained_finding(self):
        bad = sample(coverage="| auth | SCSVS-A-1 | FAIL | contracts/Example.sol:21 | H-01 |")
        self.assertTrue(any("retained finding" in p for p in validate(bad)))


if __name__ == "__main__":
    unittest.main()
