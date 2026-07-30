# System Lifecycle & Change Management (生命週期與變更管理)

**Document Control:** V1.0
**Framework Alignment:** ISO/IEC 42001:2023 (Clause 8 & Annex A.10), EU AI Act (Article 72)
**Scope:** HK DPO GenAI Governance Sandbox (Deterministic Tier Classifier)

## 1. Versioning & Baseline Alignment (版本控制與基準對齊)

The current production release (V1.1) is mathematically and logically anchored to the **HK DPO Generative AI Technical and Application Guideline V1.1 (Dec 2025)**[cite: 1]. Any modification to this external regulatory baseline constitutes a mandatory trigger for a new system lifecycle phase.

## 2. Change Management Triggers (變更管理觸發條件)

The system will enter a mandatory maintenance and code review cycle upon the occurrence of:
* The official release of a new version of the HK DPO Guideline (e.g., V2.0)[cite: 1].
* Enactment of binding AI legislation by the Hong Kong Legislative Council that supersedes current administrative guidelines.
* Discovery of a vulnerability in the underlying open-source deployment framework (Streamlit).

## 3. Regression Testing Protocol (迴歸測試規範)

Prior to deploying any major logic update to the Streamlit Community Cloud:
* **Deterministic Verification:** The updated Python logic matrix must undergo a strict unit testing protocol.
* **Pass Rate Threshold:** The system must achieve a 100% pass rate against a standardized set of 50 pre-defined compliance scenarios (covering Very High to Minimal risk tiers) to ensure zero logic drift.

## 4. Decommissioning Strategy (系統退役策略)

If the system's logic is deemed obsolete or irreconcilable with new legal frameworks:
1. A formal decommissioning notice will be published on the GitHub repository.
2. The Streamlit Community Cloud instance will be taken offline permanently to prevent users from relying on outdated compliance logic.
3. The GitHub repository will be archived to preserve the historical audit trail for compliance continuity.
