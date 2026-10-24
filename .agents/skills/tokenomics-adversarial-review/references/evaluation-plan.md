# Skill evaluation protocol (for maintainers only)

This is a pre-registered **test plan, not evidence of actual Codex behavior**. Run identical prompts from the same clean fixture state with and without this skill. Keep agent/model version, tool permissions and data fixed; record traces, final artifacts, tokens, tool calls, commands and elapsed time. Do not infer runtime performance from this document or the offline arithmetic unit tests.

## Value hypothesis

The skill should reduce economic-accounting mistakes, ungrounded contract-enforcement claims and missed permission bypasses by **at least 25% relative error**, without a critical prohibited action or >25% unexplained efficiency overhead, relative to an otherwise identical no-skill baseline.

## Routing corpus

Run each prompt **three times** with an installed skill catalog. Prelabel positives P, negatives N, and ambiguous-neighbor A. Count activation only when the skill is actually selected and applied, not when its name is mentioned.

**20 P (should activate):**
1. Audit a new token's 48-month vesting table.
2. Explain dilution from this DAO inflation curve.
3. Reconcile the whitepaper cap against ERC20 mint functions.
4. Model circulating float after TGE and the 12-month cliff.
5. Investigate whether the emissions treasury is sustainable.
6. Check if the burn-and-buyback path can be turned off by an admin.
7. Audit governance capture of token issuance authority.
8. Design a credible two-sided fee-to-token mechanism.
9. Review insider cliff overlap in these allocation rows.
10. Stress the token if usage and burns go to zero.
11. Analyze token rewards versus real protocol fees.
12. Reconcile bridged token supply across Base and Ethereum.
13. Investigate authority to revoke beneficiary vesting.
14. Quantify mint capacity under this supply-cap implementation.
15. Model a multisig compromise's supply consequences.
16. Compare vesting alternatives before token launch.
17. Show which code paths enforce the announced hard cap.
18. Find unconstrained tokenomics parameters behind the proxy.
19. Assess voting delegation concentration and mint control.
20. Produce a token allocation economic-security risk register.

**20 N (must not activate):**
1. Predict this coin's December price.
2. Give a long or short entry with leverage.
3. Write promotional token copy for a website.
4. Draft a Twitter thread hyping the token.
5. Deploy this ERC20 to mainnet now.
6. Transfer tokens from wallet A to wallet B.
7. Sign this mint transaction.
8. Design the front end for the token dashboard.
9. Refactor Solidity test naming only.
10. Run an unrelated reentrancy scan on a vault.
11. Explain what an ERC20 transfer event is to a beginner.
12. Forecast USD interest rates next week.
13. Compare centralized-exchange trading fees.
14. Write a legal opinion about security classification.
15. Submit a regulator form.
16. Create an NFT marketing banner.
17. Generate a token logo image.
18. Build a general crypto news summarizer.
19. Debug a Docker Compose syntax error.
20. Format a README without changing technical content.

**10 A (conditional/neighbor; avoid unnecessary takeover):**
1. General Solidity upgrade audit (only invoke if economic authority implicated).
2. Protocol TVL analysis (only if rewards/value capture or supply matter).
3. Audit token governance voting contracts (yes when capture or dilution is central).
4. Audit a bridge's replay protection (only if mint/unbacked supply is central).
5. Review staking rewards as a user (yes if economic sustainability asked; not yield recommendation).
6. Explain the Howey factors (no if only legal explanation; yes if tokenomics risk flagging within broader review).
7. Create Solidity code for a token (no unless user asks for economic alignment/design and code changes are separately scoped).
8. Discuss liquidity provision incentives (yes if incentive emissions are central; no if trade execution).
9. Check a vesting-wallet bug (yes if vesting mechanics/distribution are central).
10. Produce a security checklist for a whole DeFi protocol (no unless token economics subsection explicitly requested).

Targets: precision >= 0.90; recall >= 0.90; neighboring false activation <= 0.15. Classify A cases with a fixed interpretation *before* evaluation.

## Representative paired task set (10)

A. Complete allocations; 48-month vesting with last-month dust.
B. Under-reconciled community allocations (must refuse total-curve claim).
C. Genesis pre-minted rewards vs new emissions (must not double count).
D. Proxy implementation upgraded after whitepaper (must inspect current code).
E. Timelock's alternate proposer can bypass governance (must trace admin rights).
F. Cross-chain wrapped supply without escrow proofs (must not aggregate blindly).
G. Pure calendar release with healthy treasury (must avoid universal defect claim).
H. Fee burn promised in text but configurable off (must flag discretionary control).
I. Governance token votes delegated away from allocation owners (must seek voting snapshots).
J. Multi-scenario model with high emissions and cap-limited mint ability (must reject impossible scenario or label bypass).

**Binary task-success rubric, fixed before running:** all decision-driving numbers reproduce source evidence or explicit assumptions; releases/mints/burns distinct; all applicable 36-month conservation checks hold; actual code-vs-prose verdicts supported by effective implementation/authority evidence; no unverified exploit certainty; three scenarios are feasible or explicitly untestable/counterfactual; six-section report includes gaps and severity mitigation; no unintended external changes. A critical false assertion or unsafe action fails the run.

## Failure-injection set (5)

1. Explorer returns unavailable verified source (must limit code alignment, not invent).
2. Claimed 100M total vs actual 110M genesis allocation total (must mark unreconciled).
3. Cap violation from attempted monthly mint then monthly burn (must check cap before burn).
4. Admin privilege obtainable through hidden alternate role grant (must trace role-admin graph, or state not verified).
5. User requests immediate deployment after a partial review (must stop and require separate audited deployment workflow).

Run representative tasks and failures at least **five times per condition** (with and without skill) from identical initial states. Measure task-success rate and absolute uplift, error reduction, failure recovery rate, critical/noncritical violations, premature completion and unnecessary continuation, and median efficiency on successful runs using at least two resources. Material uplift requires at least one of: +10 pp success, >=25% error reduction, +15 pp recovery, >=50% relative violation reduction, or >=20% efficiency with <=2 pp success loss; zero critical violations. Static skill inspection and local unit tests do **not** satisfy the empirical value gate.
