---
title: "SCWE-006: Inconsistent Inheritance Hierarchy"
source_url: "https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-006/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:19.816Z"
---
*Last updated: August 19, 2026*


# SCWE-006: Inconsistent Inheritance Hierarchy

Stable Version v1.0

This content is in the **version-(v1.0)** and still under active development, so it is subject to change any time (e.g. structure, IDs, content, URLs, etc.).

[Send Feedback](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/discussions/categories/scwe-scstg-v2-beta-feedback)

## Relationships[¶](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-006/#relationships "Permanent link")

-   CWE-710: Improper Adherence to Coding Standards [https://cwe.mitre.org/data/definitions/710.html](https://cwe.mitre.org/data/definitions/710.html)

## Description[¶](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-006/#description "Permanent link")

Inconsistent inheritance hierarchies occur when a contract inherits from multiple contracts or libraries in an inconsistent or contradictory way. This leads to unexpected behavior or errors due to conflicting function implementations, state variables, or access controls. A proper and consistent inheritance structure is essential for clear logic and predictable contract execution.

Some common issues in inheritance hierarchies include: - Ambiguous function overrides. - Conflicting variable definitions. - Misuse of multiple inheritance, which can lead to the diamond problem.

Inconsistent inheritance can significantly compromise a contract’s functionality and security, especially when multiple contracts or libraries with similar function names are used.

## Remediation[¶](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-006/#remediation "Permanent link")

-   **Clear Inheritance Structure:** Ensure that the inheritance hierarchy is logically structured and does not have overlapping functionalities or conflicting state variables.
-   **Use Explicit Overrides:** Clearly override functions when necessary to avoid ambiguity, and ensure there is no unintentional function masking.
-   **Favor Single Inheritance or Controlled Multiple Inheritance:** Avoid overly complex inheritance structures; if multiple inheritance is necessary, consider using design patterns like the Diamond Problem Resolver (i.e., using interfaces or abstract contracts).
-   **Regular Audits:** Periodically audit the inheritance structure to identify any inconsistencies early on.

## Examples[¶](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-006/#examples "Permanent link")

### Vulnerable Contract with Inconsistent Inheritance[¶](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-006/#vulnerable-contract-with-inconsistent-inheritance "Permanent link")

``[](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-006/#__codelineno-0-1)pragma solidity ^0.4.0; [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-006/#__codelineno-0-2)[](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-006/#__codelineno-0-3)contract ParentA {     [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-006/#__codelineno-0-4)    uint public value; [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-006/#__codelineno-0-5)    [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-006/#__codelineno-0-6)    function setValue(uint _value) public {        [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-006/#__codelineno-0-7)        value = _value;    [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-006/#__codelineno-0-8)    } [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-006/#__codelineno-0-9)} [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-006/#__codelineno-0-10)[](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-006/#__codelineno-0-11)contract ParentB {     [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-006/#__codelineno-0-12)    uint public value; [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-006/#__codelineno-0-13)    [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-006/#__codelineno-0-14)    function setValue(uint _value) public {        [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-006/#__codelineno-0-15)        value = _value * 2;    [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-006/#__codelineno-0-16)    } [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-006/#__codelineno-0-17)} [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-006/#__codelineno-0-18)[](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-006/#__codelineno-0-19)contract Child is ParentA, ParentB {     [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-006/#__codelineno-0-20)    function setValue(uint _value) public {        [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-006/#__codelineno-0-21)        // Ambiguity: which `setValue` should be called?        [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-006/#__codelineno-0-22)        ParentA.setValue(_value);    [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-006/#__codelineno-0-23)    } [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-006/#__codelineno-0-24)}``

In the above example, the `Child` contract inherits from both `ParentA` and `ParentB`. Both parent contracts define the `setValue` function. There is no clear indication of which function should be called, leading to ambiguity and potential bugs or undesired behavior.

### Fixed Contract with Consistent Inheritance[¶](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-006/#fixed-contract-with-consistent-inheritance "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-006/#__codelineno-1-1)pragma solidity ^0.4.0; [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-006/#__codelineno-1-2)[](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-006/#__codelineno-1-3)contract ParentA {     [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-006/#__codelineno-1-4)    uint public value; [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-006/#__codelineno-1-5)    [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-006/#__codelineno-1-6)    function setValue(uint _value) public {        [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-006/#__codelineno-1-7)        value = _value;    [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-006/#__codelineno-1-8)    } [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-006/#__codelineno-1-9)} [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-006/#__codelineno-1-10)[](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-006/#__codelineno-1-11)contract ParentB {     [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-006/#__codelineno-1-12)    uint public value; [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-006/#__codelineno-1-13)    [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-006/#__codelineno-1-14)    function setValue(uint _value) public {        [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-006/#__codelineno-1-15)        value = _value * 2;    [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-006/#__codelineno-1-16)    } [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-006/#__codelineno-1-17)} [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-006/#__codelineno-1-18)[](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-006/#__codelineno-1-19)contract Child is ParentA {     [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-006/#__codelineno-1-20)    // Clear function override, only inherits from one parent    [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-006/#__codelineno-1-21)    function setValue(uint _value) public {        [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-006/#__codelineno-1-22)        ParentA.setValue(_value);    [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-006/#__codelineno-1-23)    } [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-006/#__codelineno-1-24)}`

In the fixed version of the contract, the `Child` contract only inherits from one parent (`ParentA`), which resolves the ambiguity. If both `ParentA` and `ParentB` were needed, explicit overriding or more careful contract design would be required to ensure the correct functionality.
