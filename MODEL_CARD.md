# Model Card: HK DPO GenAI Governance Workstation (Deterministic Guardrail Engine)

> **ISO 42001 Compliance Statement:** This Model Card serves as audit-ready documentation for System Transparency, Lifecycle Control, and Risk Assessment in accordance with ISO/IEC 42001:2023 Artificial Intelligence Management System (AIMS) standard.

---

## 1. System Overview & Intended Use (系統概述與預期用途)

* **Model Name:** HK DPO GenAI Compliance Workstation & Tier Classifier
* **Version:** 1.1 (Aligned with HK DPO Guideline V1.1 Dec 2025)
* **Type:** Deterministic Logic Gate & Rule-Based Compliance Classifier (Zero Generative Hallucination)
* **Target Audience:** Executive Leadership, Board Directors, AI Risk & Compliance Auditors, HR Professionals.
* **Intended Use:** Automated pre-audit evaluation, 4-tier risk classification, and governance readiness scoring for enterprise GenAI deployments within Hong Kong jurisdiction.
* **Out-of-Scope Use:** Explicitly blocks non-generative ML models (e.g., Random Forest, XGBoost). This system DOES NOT provide formal legal advice or binding regulatory approvals.

---

## 2. Architecture & Technical Specifications (架構與技術規範)

* **Core Engine:** 100% Python Conditional Decision Matrix & Deterministic Risk Mapping.
* **Hosting Environment:** Streamlit Community Cloud (Zero data persistence at rest).
* **Deterministic Guardrails:** Implements hard conditional boundaries to completely eliminate generative AI hallucinations during audit evaluation.
* **Auditability:** Every compliance response maps 1:1 to specific clauses in the HK Digital Policy Office (DPO) "Generative AI Technical and Application Guideline V1.1".

---

## 3. Risk Management & Safety Guardrails (風險管理與安全護欄)

* **Data Minimization:** No User PII or corporate audit logs are saved, stored in a database, or transmitted to third-party endpoints.
* **Fail-Safe Mechanism:** System defaults to the highest risk tier (Very High / High Risk) if input variables contain ambiguity or insufficient organizational controls.
* **Out-of-Scope Enforcement:** Rejects non-GenAI technologies programmatically to prevent compliance misclassification.

---

## 4. ISO 42001 Control Mapping (ISO 42001 控制措施對齊)

* **A.6.2 (AI System Impact Assessment):** Evaluates system deployment impact against public interest, privacy, and systemic risk tiers.
* **A.8.2 (Data for AI Systems):** Audits enterprise data provenance, user consent, and shadow AI mitigation.
* **A.9.3 (Human Oversight):** Enforces mandatory Human-in-the-Loop override and emergency termination mechanisms.

---

## 5. Contact & Accountability (問責與聯絡人)

* **System Owner:** Jacky Law CK (ISO 42001 Lead Auditor Track / AI Governance Professional)
* **LinkedIn:** [https://www.linkedin.com/in/jackylawck](https://www.linkedin.com/in/jackylawck)
