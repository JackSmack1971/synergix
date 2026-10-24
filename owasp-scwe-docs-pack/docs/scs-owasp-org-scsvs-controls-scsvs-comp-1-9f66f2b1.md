---
title: "SCSVS-COMP-1¶"
source_url: "https://scs.owasp.org/SCSVS/controls/SCSVS-COMP-1/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:28:59.212Z"
---
[](https://github.com/OWASP/www-project-smart-contract-security-verification-standard/edit/master/SCSVS/controls/SCSVS-COMP-1.md "Edit this page")

# SCSVS-COMP-1[¶](https://scs.owasp.org/SCSVS/controls/SCSVS-COMP-1/#scsvs-comp-1 "Permanent link")

## S11.1 Tokens (ERC20, ERC721, ERC1155)[¶](https://scs.owasp.org/SCSVS/controls/SCSVS-COMP-1/#s111-tokens-erc20-erc721-erc1155 "Permanent link")

### Control Objective[¶](https://scs.owasp.org/SCSVS/controls/SCSVS-COMP-1/#control-objective "Permanent link")

Ensure secure implementation and management of token standards to prevent vulnerabilities.

### S11.1.A Secure Implementation and Management[¶](https://scs.owasp.org/SCSVS/controls/SCSVS-COMP-1/#s111a-secure-implementation-and-management "Permanent link")

| **SCSVS VR ID** | Requirement | L1 | L2 | L3 | SWE |
| --- | --- | --- | --- | --- | --- |
| S11.1.A1 | Verify that the totalSupply value is consistent during token minting operations, ensuring that callbacks do not result in incorrect values. |  | ✓ | ✓ |  |
| S11.1.A2 | Some tokens have multiple addresses associated with them, which can introduce vulnerabilities. Ensure all token addresses are managed and verified securely to avoid related risks. |  | ✓ | ✓ |  |
| S11.1.A3 | Verify that tokens handle zero amount transfers properly to prevent issues in integrations and operations. |  | ✓ | ✓ |  |
| S11.1.A4 | Verify that tokens handle zero amount transfers properly to prevent issues in integrations and operations. |  | ✓ | ✓ |  |
| S11.1.A5 | Some tokens revert on the transfer of a zero amount, which can cause issues in certain integrations and operations. Ensure compatibility with such tokens to avoid integration problems. |  | ✓ | ✓ |  |
| S11.1.A6 | Not all ERC20 tokens comply with the EIP20 standard; some may not return a boolean flag or revert on failure. Verify compliance with the ERC20 standard to avoid compatibility issues. |  | ✓ | ✓ |  |
