---
title: "What is HCP Vault Dedicated?"
source_url: "https://developer.hashicorp.com/vault/cloud"
host: "developer.hashicorp.com"
depth: 2
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:54.541Z"
---
# What is HCP Vault Dedicated?

HCP Vault Dedicated is a hosted version of Vault Enterprise operated by Hashicorp on your behalf.

HCP Vault Dedicated is a hosted version of Vault Enterprise operated by HashiCorp that allows organizations to get up and running quickly. HCP Vault Dedicated uses the same binary as self-hosted Vault Enterprise, which means you will have a consistent user experience. You can use the same CLI, API, and UI to communicate with HCP Vault Dedicated as you use to communicate with a self-hosted Vault Enterprise.

You can create HCP Vault Dedicated clusters on either AWS or Azure across multiple regions across North America, Asia, and Europe. HashiCorp manages the cloud provider you select in an account dedicated to your organization.

## [](https://developer.hashicorp.com/vault/cloud#why-hcp-vault-dedicated)Why HCP Vault Dedicated?

Vault Enterprise running on the HashiCorp Cloud Platform (HCP) enables users to secure, store, and control access to tokens, passwords, certificates, and encryption keys within one unified cloud-based platform.

The benefits of HCP Vault Dedicated are:

-   **Reduce operational overhead:** Push-button deployment, fully managed upgrades, and backups mean organizations can focus on adoption and integration instead of operational overhead.

-   **Increase security across clouds and machines:** Secure your infrastructure across all your environments through a single interface and globally control and restrict access to sensitive data and systems.

-   **Control cost:** Reduce the number of systems, licenses, and manual overhead by centralizing secrets management with HCP Vault Dedicated.

-   **Day zero readiness:** Modern cloud security to secure applications, access, and data from day zero.

-   **Reliability:** HashiCorp has experience supporting thousands of commercial Vault Enterprise clusters and HCP Vault Dedicated brings that expertise directly to users.

-   **Ease of use:** HCP Vault Dedicated is built around making cloud security automation simple. Get up and running so that you can onboard applications and teams.


## [](https://developer.hashicorp.com/vault/cloud#feature-parity)Feature parity

Since HCP Vault Dedicated uses the same binary as Vault Enterprise, most enterprise features are available to HCP Vault Dedicated users. Some features such as auto-unseal are managed by HashiCorp to manage the cluster.

The table compares the features available on the self-managed Vault Enterprise and HCP Vault Dedicated.

| Features | HCP Vault Dedicated | Self-managed |
| --- | :-: | :-: |
| All community edition features | ✅ | ✅ |
| Audit logging by default | ✅ | ❌ |
| Automatic minor version upgrade | ✅ | ❌ |
| Automatic major version upgrade | ✅ | ❌ |
| Control groups | ✅ | ✅ |
| Disaster Recovery (DR) replication | ✅ | ✅ |
| Event notifications | ✅ | ✅ |
| Key management secrets engine | ✅ | ✅ |
| KMIP secrets engine | ✅ | ✅ |
| Namespaces | ✅ | ✅ |
| Performance replication | ✅ | ✅ |
| Paths filter | ✅ | ✅ |
| Read replica | ✅ | ✅ |
| Snapshots & restore | ✅ | ❌ |
| Sentinel | ✅ | ✅ |
| Transform secrets engine | ✅ | ✅ |
| Workload identity federation (WIF)1 | ✅ | ✅ |
| Entropy augmentation | ❌ | ✅ |
| FIPS 140-2 & seal wrap | ❌ | ✅ |
| HSM auto-unseal | ❌ | ✅ |

*1\. HCP Vault Dedciated supports WIF on clusters with a public interface.*

## [](https://developer.hashicorp.com/vault/cloud#self-managed-vs-hcp-vault-dedicated-cluster)Self-managed vs. HCP Vault Dedicated cluster

Here is a comparison between a self-managed Vault Enterprise cluster and an HCP Vault Dedicated cluster.

| Cluster Feature | Self-managed | HCP Vault Dedicated |
| --- | --- | --- |
| Edition | Vault Community Edition or Vault Enterprise | Vault Enterprise |
| Version | Self-manage the upgrade process | Minor and major versions are upgraded for you automatically. See the [Vault version documentation](https://developer.hashicorp.com/vault/hcp-docs/versions) for more detail. |
| [Advanced Data Protection (ADP)](https://www.hashicorp.com/products/vault/advanced-data-protection) features | Available with Vault Enterprise license | Available with HCP Vault Dedicated Standard. |
| Cluster scaling | No built in feature to scale the cluster size up or down. | [Scale your cluster size](https://developer.hashicorp.com/vault/tutorials/cloud/vault-ops#scale-an-hcp-vault-cluster-up-or-down) dynamically via the HashiCorp Cloud Platform Portal or Terraform. |
| [Disaster recovery replication](https://developer.hashicorp.com/vault/hcp-docs/what-is-hcp-vault/high-avail-disaster-recover) | Available with Vault Enterprise license | Cross-region disaster recovery is available with HCP Vault Dedicated Standard and managed by HashiCorp. |
| [Performance replication](https://developer.hashicorp.com/vault/tutorials/manage-hcp-vault-dedicated/scale-out-vault) | Available with Vault Enterprise license | [Performance Replication](https://developer.hashicorp.com/vault/tutorials/cloud-ops/vault-replication) is available with HCP Vault Dedicated Standard. |
| Seal | Seal uses Shamir's Secret Sharing algorithm to generate key shares by default. | Auto-unseal is configured. A unique Key Management Service (KMS) key is created for each cluster. |
| [Secrets sync](https://developer.hashicorp.com/vault/docs/sync) | Available with Vault Enterprise license | Available with HCP Vault Dedicated Standard. |
| [Sentinel](https://developer.hashicorp.com/vault/docs/enterprise/sentinel) and [Control Groups](https://developer.hashicorp.com/vault/docs/enterprise/control-groups) | Available with Vault Enterprise license | Available with HCP Vault Dedicated Standard. |
| Storage backend | Choose one and self-manage | Integrated Storage |
| Super user access | Vault initialization process generates a `root` token. To regenerate a `root` token, unseal keys or recovery keys are required. | Click on the **Generate token** button via HCP Vault Dedicated Portal returns an `admin` token which is valid for 6 hours. |
| Tier sizing | Not applicable | For information on tier sizing and pricing, see [HCP Vault Dedicated Pricing](https://cloud.hashicorp.com/products/vault/pricing). |
| Top-level Namespace | `root` | `admin` |

## [](https://developer.hashicorp.com/vault/cloud#operational-responsibilities)Operational responsibilities

HCP Vault Dedicated follows a shared responsibility model.

### [](https://developer.hashicorp.com/vault/cloud#hashicorp-responsibilities)HashiCorp responsibilities

HashiCorp operates and maintains the HCP Vault platform, including:

-   Infrastructure monitoring
-   Cluster health management
-   Storage operations
-   Backups and snapshots
-   Upgrades and maintenance
-   High availability operations
-   Platform and infrastructure recovery

### [](https://developer.hashicorp.com/vault/cloud#customer-responsibilities)Customer responsibilities

Customers are responsible for configuring and operating Vault within their environment, including:

-   Vault configuration
-   Authentication and access policies
-   Identity management
-   Secrets engines
-   Application integration and connectivity
-   Usage and capacity planning
-   Monitoring through metrics and audit logs

### [](https://developer.hashicorp.com/vault/cloud#storage-lifecycle-management)Storage lifecycle management

HashiCorp manages the underlying storage infrastructure.

Customers manage the logical lifecycle of data stored in Vault, including:

-   Tokens
-   Leases
-   KV secret versions
-   Unused secrets
-   Vault configuration that is no longer needed

### [](https://developer.hashicorp.com/vault/cloud#restore-and-disaster-recovery)Restore and disaster recovery

HashiCorp operates the backup, restore, and managed disaster recovery capabilities for HCP Vault Dedicated.

Following a recovery event, customers should validate that applications, authentication workflows, and integrations continue to function as expected.

Cross-region disaster recovery is available as an optional production capability.

### [](https://developer.hashicorp.com/vault/cloud#summary)Summary

HashiCorp operates, maintains, and recovers the HCP Vault platform. Customers securely configure Vault, monitor its usage, and validate application recovery following restore or disaster recovery events.

## [](https://developer.hashicorp.com/vault/cloud#hcp-vault-dedicated-on-azure)HCP Vault Dedicated on Azure

HCP Vault Dedicated on Azure includes all features found on AWS with the exception of the following features which are planned:

-   Oracle Database Secrets Plugin
-   KMIP Secrets Engine

## [](https://developer.hashicorp.com/vault/cloud#tutorial)Tutorial

Refer to the [Getting Started with HCP Vault Dedicated](https://developer.hashicorp.com/vault/tutorials/cloud) tutorial to get hands-on with HCP Vault Dedicated and set up your managed Vault cluster.

[Edit this page on GitHub](https://github.com/hashicorp/web-unified-docs/blob/main/content/vault-hcp//docs/hcp-docs/index.mdx)
