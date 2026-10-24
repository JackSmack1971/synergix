# Audit report contract — `audit/REPORT.md`

One Markdown report, with the exact eight level-2 headings below. Begin with `STATUS: COMPLETE` only if the workflow gates were satisfied and all blocking uncertainties resolved; otherwise use `STATUS: INCOMPLETE` and `Blocker: <specific missing evidence or permission>` near the top. Completion is a calibrated statement about **scope audited**, never an absence-of-bugs guarantee.

## Required sections

1. `## 1. Executive summary`: Scope, pinned commit, target chains, methodology, severity counts, 3–5-sentence posture summary, top three risks, and audit limitations.
2. `## 2. Scope and assumptions`: All in-scope Solidity files with LOC, exclusions, assumptions/trust model, exact tools/versions, baseline commands/results, dependencies, compiler/EVM, and untested items.
3. `## 3. Threat model and invariants`: Actor and asset model; table of invariant, observation/test, `PASS`/`FAIL`/`NOT TESTED`, and evidence.
4. `## 4. Findings`: Only validated retained findings, descending severity; if none, explain depth/limitations. Use headings like `### H-01 Unauthorized mint in <file>`. For each finding include labeled fields: `Severity:`, `Impact:`, `Likelihood:`, `Confidence:`, `Calibration:`, `SCWE:`, `SCSVS:`, `Locations:`, `Root cause:`, `Attack scenario:`, `PoC:`, `Falsification:`, `Impact detail:`, `Recommendation:`, `Regression risk:`, `Status: OPEN`. Number attack steps under `Attack scenario` and state actor, prerequisites, timing/capital. Locations include vulnerable lines **and** insufficient guards, or state missing guard with actual search performed. Include concrete source URLs for OWASP citations.
5. `## 5. Centralization and trust risks`: Document intended role powers, what compromise enables, trust assumptions, and mitigations; separate architectural/design risks from exploitable errors.
6. `## 6. Invariant, test, and OWASP coverage`: Techniques/tests run, what failed and why, recommended invariants, and table with **exact** columns `Category | Control/test | Status | Evidence | Finding`. For coverage `PASS`, use `file:line` evidence; for `FAIL`, reference validated finding; for `N/A`, show search rationale; for `NOT TESTED`, explain the limitation.
7. `## 7. Discarded candidates`: Each falsified or unverified candidate with the failed validation gate, strongest counterargument, and evidence. Distinguish unverified leads from disproven hypotheses.
8. `## 8. Appendix`: Inventory table, call-graph summary, condensed tool command/output/exit-status list, cited OWASP page URLs/edition, glossary.

Use Markdown tables **only** for inventory, severity counts, invariants, and checklist coverage. Other material should be prose/lists with code fences labeled by language. Use finding ID sequence by category `C-01`, `H-01`, `M-01`, `L-01`, `I-01`, `G-01`, restarting within each severity and without duplicate IDs.

## Severity and confidence rules

- Impact high: loss, insolvency, or permanent frozen funds; medium: bounded loss/freeze or broken core operation; low: minor disclosure/griefing without loss.
- Likelihood high: realistic unprivileged path without special prerequisites; medium: timing/capital/specific state; low: privileged/compromised or prohibitive cost. Combined risk **informs**, not mechanically dictates, Critical vs High; specify exploit cost and assumptions. Admin compromise normally belongs in Section 5, not a fabricated unprivileged finding.
- Every finding carries a calibration tag: `[VERIFIED: PoC executed + output]`, `[INFERRED: code-path reasoning]`, `[TOOL-FLAGGED: unvalidated]`, or `[UNKNOWN: state what is missing]`. `[ESTIMATED: basis]` for dollars; `[REPORTED: source, unverified this session]` for historical events not verified now. Tool-only leads normally belong in Section 7 until validated.
- **Critical/High findings require PoC execution evidence**. If unavailable, do not assert verified High/Critical. State the unverified risk in Section 7 or present clearly as limited informational discussion, and mark the corresponding validation limitation. `PoC: UNEXECUTED` is not a passing validation gate.
- A code path, tool alert, or OWASP category does not alone determine severity. A reported `PASS` must be supported by code or a test; a testing failure in the pre-existing baseline does not prove a vulnerability.

## Report completion

Before stating `STATUS: COMPLETE`, check each source file/invariant/control mapping and candidate, reconcile different threat-model assumptions, and verify PoC/test claims against collected output. Run the package's read-only `scripts/validate_report.py` and review all semantic evidence that a syntactic validator cannot check. A structurally valid `STATUS: INCOMPLETE` report is the correct artifact for missing source, blocked tests, unavailable OWASP pack, or unresolved permissions.
