---
title: "SCSVS-CODE-3¶"
source_url: "https://scs.owasp.org/SCSVS/controls/SCSVS-CODE-3/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:28:55.282Z"
---
[](https://github.com/OWASP/www-project-smart-contract-security-verification-standard/edit/master/SCSVS/controls/SCSVS-CODE-3.md "Edit this page")

# SCSVS-CODE-3[¶](https://scs.owasp.org/SCSVS/controls/SCSVS-CODE-3/#scsvs-code-3 "Permanent link")

## S2.3 Test Coverage[¶](https://scs.owasp.org/SCSVS/controls/SCSVS-CODE-3/#s23-test-coverage "Permanent link")

### Control Objective[¶](https://scs.owasp.org/SCSVS/controls/SCSVS-CODE-3/#control-objective "Permanent link")

Ensure comprehensive test coverage for smart contracts, encompassing unit tests, integration tests, and security-specific tests, to identify vulnerabilities and maintain code quality throughout development.

### S2.3.A Unit Tests, Integration Tests, Automated Testing[¶](https://scs.owasp.org/SCSVS/controls/SCSVS-CODE-3/#s23a-unit-tests-integration-tests-automated-testing "Permanent link")

| **SCSVS VR ID** | Requirement | L1 | L2 | L3 | SWE |
| --- | --- | --- | --- | --- | --- |
| S2.3.A1 | Verify that all critical functions in the smart contract have comprehensive unit tests that cover both typical and edge cases. |  | ✓ | ✓ |  |
| S2.3.A2 | Ensure that integration tests are implemented to validate the interactions between the smart contract and other contracts or external systems. |  | ✓ | ✓ |  |
| S2.3.A3 | Check that automated tests are set up to run on each code commit to detect regressions and maintain continuous quality of the smart contract. |  | ✓ | ✓ |  |
| S2.3.A4 | Verify that test coverage tools are used to monitor and achieve a high percentage of coverage for the smart contract code. |  | ✓ | ✓ |  |
| S2.3.A5 | Ensure that the testing framework supports mocking and simulating external dependencies to effectively isolate and test specific functionalities of the smart contract. |  | ✓ | ✓ |  |

### S2.3.B Security-Specific Tests[¶](https://scs.owasp.org/SCSVS/controls/SCSVS-CODE-3/#s23b-security-specific-tests "Permanent link")

| **SCSVS VR ID** | Requirement | L1 | L2 | L3 | SWE |
| --- | --- | --- | --- | --- | --- |
| S2.3.B1 | Verify that the test suite for the smart contract includes security-specific tests designed to identify vulnerabilities such as reentrancy, integer overflows, and improper access controls. |  | ✓ | ✓ |  |
| S2.3.B2 | Ensure that the security tests validate proper implementation of access controls and permissions within the smart contract. |  | ✓ | ✓ |  |
| S2.3.B3 | Check that fuzz testing is conducted to uncover unexpected behaviors and potential security issues under various input scenarios. |  | ✓ | ✓ |  |
| S2.3.B4 | Verify that the smart contract's response to invalid inputs and edge cases is thoroughly tested to ensure robust security measures are in place. |  | ✓ | ✓ |  |
