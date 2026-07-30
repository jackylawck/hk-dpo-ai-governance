# Data Governance & Privacy Architecture (數據管治與隱私架構)

**Document Control:** V1.0
**Framework Alignment:** ISO/IEC 42001:2023 (Annex A.7), GDPR / HK PDPO
**Scope:** HK DPO GenAI Governance Sandbox (Deterministic Tier Classifier)

## 1. Data Provenance & Lineage (數據來源與血統)

* **Sandbox Ruleset Baseline:** The underlying logic matrix is hard-coded strictly based on the official text of the HK Digital Policy Office (DPO) "Generative AI Technical and Application Guideline V1.1"[cite: 1].
* **Input Data Restrictions:** The system is explicitly programmed to process categorical organizational variables (e.g., "Internal Use", "Public Facing") and binary readiness checks. 

## 2. Data Minimization & Privacy by Design (資料最小化與隱私設計)

* **Zero PII Collection:** The sandbox does not request, accept, or parse any Personally Identifiable Information (PII) or sensitive corporate documents.
* **Zero Persistent Storage:** The system utilizes no external relational databases (e.g., PostgreSQL, MySQL). All user inputs reside entirely in the volatile memory (RAM) of the active Streamlit session.
* **Automatic Destruction:** Upon browser closure or manual session reset, all inputted state variables and generated scorecards are instantly and irreversibly destroyed.

## 3. Out-of-Scope Blocking (主動阻斷機制)

To prevent data contamination and compliance misclassification, the system implements proactive out-of-scope blocking. Inputs related to traditional discriminative machine learning models (e.g., Random Forest, XGBoost) are programmatically rejected.
