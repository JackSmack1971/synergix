#!/usr/bin/env python3
"""Read-only syntactic guard for the SynergiX audit report. Does not prove audit correctness."""

from __future__ import annotations

import argparse
from pathlib import Path
import re

SECTIONS = [
    "Executive summary",
    "Scope and assumptions",
    "Threat model and invariants",
    "Findings",
    "Centralization and trust risks",
    "Invariant, test, and OWASP coverage",
    "Discarded candidates",
    "Appendix",
]
FINDING = re.compile(r"^###\s+([CHMLIG]-\d{2})\s+\S.*$", re.M)
LOCATION = re.compile(r"\b[\w./-]+\.sol:\d+\b")
REQUIRED_FIELDS = (
    "Severity", "Impact", "Likelihood", "Confidence", "Calibration", "SCWE",
    "SCSVS", "Locations", "Root cause", "Attack scenario", "PoC",
    "Falsification", "Impact detail", "Recommendation", "Regression risk", "Status",
)


def validate(content: str) -> list[str]:
    problems: list[str] = []
    status = re.search(r"^STATUS:\s*(COMPLETE|INCOMPLETE)\s*$", content, re.M)
    if not status:
        problems.append("Missing exact top-level STATUS: COMPLETE or STATUS: INCOMPLETE")
    elif status.group(1) == "INCOMPLETE" and not re.search(r"^Blocker:\s*\S+", content, re.M):
        problems.append("INCOMPLETE report requires a nonempty Blocker: line")

    headings = re.findall(r"^##\s+(.+?)\s*$", content, re.M)
    required = [f"{n}. {title}" for n, title in enumerate(SECTIONS, 1)]
    if headings != required:
        problems.append("Level-2 section headings must match all eight required sections in order")
        return problems

    found_section = content.split("## 4. Findings", 1)[1].split("## 5. Centralization", 1)[0]
    matches = list(FINDING.finditer(found_section))
    claimed_headings = re.findall(r"^###\s+(.+)$", found_section, re.M)
    if len(claimed_headings) != len(matches):
        problems.append("All finding subheadings must use ### C-01/H-01/M-01/L-01/I-01/G-01 Title")
    ids = [m.group(1) for m in matches]
    if len(ids) != len(set(ids)):
        problems.append("Duplicate finding IDs")

    for i, match in enumerate(matches):
        fid = match.group(1)
        block = found_section[match.end(): matches[i + 1].start() if i + 1 < len(matches) else None]
        for field in REQUIRED_FIELDS:
            if not re.search(rf"^{re.escape(field)}:\s*\S", block, re.M):
                problems.append(f"{fid}: missing field {field}:")
        locations = LOCATION.findall(block)
        if not locations:
            problems.append(f"{fid}: no .sol file:line citation")
        elif len(locations) < 2 and not re.search(r"no guard exists.*search|searched.*no guard exists", block, re.I | re.S):
            problems.append(f"{fid}: guard citation absent; describe the search proving no guard exists")
        if not re.search(r"\bSCWE-\d{3}\b", block):
            problems.append(f"{fid}: no SCWE-NNN mapping")
        if not re.search(r"\bSCSVS\b|\bSCSVS-[\w-]+", block, re.I):
            problems.append(f"{fid}: no SCSVS reference")
        if not re.search(r"^Status:\s*OPEN\s*$", block, re.M):
            problems.append(f"{fid}: Status must be OPEN")
        if fid[0] in "CH":
            poc = re.search(r"^PoC:\s*(.+)$", block, re.M)
            if not poc or not re.search(r"\bEXECUTED\b", poc.group(1)) or re.search(r"\bUNEXECUTED\b", poc.group(1)):
                problems.append(f"{fid}: Critical/High requires locally EXECUTED PoC evidence")
            if f"test/poc/{fid}.test.js" not in block:
                problems.append(f"{fid}: missing expected local Hardhat PoC file path")
            if not re.search(r"\boutput\b", block, re.I):
                problems.append(f"{fid}: missing PoC output reference")
            if not re.search(r"^Calibration:.*\[VERIFIED: PoC executed \+ output\]", block, re.M):
                problems.append(f"{fid}: verified Critical/High must use executed-PoC calibration")

    coverage = content.split("## 6. Invariant, test, and OWASP coverage", 1)[1].split("## 7. Discarded", 1)[0]
    rows = [line.strip().strip("|").split("|") for line in coverage.splitlines() if line.lstrip().startswith("|")]
    normalized = [[c.strip() for c in row] for row in rows]
    header = ["category", "control/test", "status", "evidence", "finding"]
    if not any([c.lower() for c in row] == header for row in normalized):
        problems.append("Section 6 requires coverage table header: Category | Control/test | Status | Evidence | Finding")
    else:
        top = next(i for i, row in enumerate(normalized) if [c.lower() for c in row] == header)
        entries = [row for row in normalized[top + 1:] if not all(re.fullmatch(r"[-: ]+", c) for c in row)]
        if not entries:
            problems.append("Coverage table contains no control or explicit not-tested entry")
        for row in entries:
            if len(row) != 5:
                problems.append("Coverage table row does not have five columns")
                continue
            category, control, state, evidence, linked = row
            state = state.upper().replace("-", " ")
            if state not in {"PASS", "FAIL", "N/A", "NOT TESTED"}:
                problems.append(f"Invalid coverage status for {control}: {state}")
            if state == "PASS" and not LOCATION.search(evidence):
                problems.append(f"PASS control {control} lacks file:line evidence")
            if state == "FAIL" and linked not in ids:
                problems.append(f"FAIL control {control} lacks retained finding ID")
            if state in {"N/A", "NOT TESTED"} and len(evidence.strip(" —-")) < 8:
                problems.append(f"{state} control {control} needs explanatory search or blocker evidence")
            if status and status.group(1) == "COMPLETE" and state == "NOT TESTED":
                problems.append(f"COMPLETE report contains NOT TESTED control: {control}")

    if status and status.group(1) == "COMPLETE" and re.search(r"\b\[TODO\b|\bTBD\b|<specific", content, re.I):
        problems.append("COMPLETE report contains unfinished placeholder")
    return problems


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("report", type=Path, nargs="?", default=Path("audit/REPORT.md"))
    args = parser.parse_args()
    try:
        content = args.report.read_text(encoding="utf-8")
    except OSError as exc:
        print(f"FAIL: cannot read report: {exc}")
        return 2
    problems = validate(content)
    if problems:
        for problem in problems:
            print(f"FAIL: {problem}")
        return 1
    print("PASS: report structure and selected evidence-syntax checks (not semantic audit verification)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
