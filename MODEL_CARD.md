# Model Card: HK DPO GenAI Governance Workstation (Deterministic Guardrail Engine)
# 模型卡片：香港數字辦 GenAI 管治工作站（決定性護欄引擎）

> **ISO 42001 Compliance Statement:** This Model Card serves as audit-ready documentation for System Transparency, Lifecycle Control, and Risk Assessment in accordance with ISO/IEC 42001:2023 Artificial Intelligence Management System (AIMS) standard.
> **ISO 42001 合規聲明：** 本模型卡片依據 ISO/IEC 42001:2023 人工智能管理體系 (AIMS) 標準編寫，作為系統透明度、生命週期控制及風險評估之審計即用型文檔。

---

## 1. System Overview & Intended Use (系統概述與預期用途)

* **Model Name / 模型名稱:** HK DPO GenAI Compliance Workstation & Tier Classifier (香港數字辦 GenAI 合規工作站與風險分級器)
* **Version / 系統版本:** 1.1 (Aligned with HK DPO Guideline V1.1 Dec 2025 / 對齊 2025 年 12 月數字辦指引 V1.1)[cite: 1]
* **Type / 模型類型:** Deterministic Logic Gate & Rule-Based Compliance Classifier (100% 決定性邏輯閘與規則型合規分類器 - 零生成幻覺)
* **Target Audience / 目標受眾:** Executive Leadership, Board Directors, AI Risk & Compliance Auditors, HR Professionals (企業高管、董事會成員、AI 風險與合規審計師、HR 專業人員)。
* **Intended Use / 預期用途:** Automated pre-audit evaluation, 4-tier risk classification, and governance readiness scoring for enterprise GenAI deployments within Hong Kong jurisdiction (針對香港司法管轄區內之企業級 GenAI 部署，提供自動化預審評估、四級風險分類及管治準備度評分)[cite: 1]。
* **Out-of-Scope Use / 禁用範疇:** Rejects traditional non-generative ML models (e.g., Random Forest, XGBoost) programmatically. This system DOES NOT provide formal legal advice (主動阻斷傳統判別式機器學習模型。本系統絕對不提供正式法律諮詢意見)。

---

## 2. Architecture & Technical Specifications (架構與技術規範)

* **Core Engine / 核心引擎:** 100% Python Conditional Decision Matrix & Deterministic Risk Mapping (100% 純 Python 條件決策矩陣與決定性風險映射)。
* **Hosting Environment / 部署環境:** Streamlit Community Cloud (Zero data persistence at rest / 短暫性內存沙盒，資料不落地)。
* **Deterministic Guardrails / 決定性護欄:** Implements hard conditional boundaries to completely eliminate generative AI hallucinations during audit evaluation (實作硬性條件邊界，在審計評估過程中徹底消除生成式 AI 幻覺)。
* **Auditability / 可審計性:** Every compliance response maps 1:1 to specific clauses in the HK Digital Policy Office (DPO) "Generative AI Technical and Application Guideline V1.1" (每項合規輸出均 1:1 對齊香港數字政策辦公室《生成式人工智能技術及應用指引》V1.1 之特定條文)[cite: 1]。

---

## 3. Risk Management & Safety Guardrails (風險管理與安全護欄)

* **Data Minimization / 資料最小化:** No User PII or corporate audit logs are saved, stored in a database, or transmitted to third-party endpoints (完全不收集個人識別資訊 PII，亦不儲存任何企業審計日誌於硬碟或第三方端點)。
* **Fail-Safe Mechanism / 失效安全機制:** System defaults to the highest risk tier (Very High / High Risk) if input variables contain ambiguity or insufficient organizational controls (若輸入變數存在模糊性或組織控制措施不足，系統預設提升至最高風險層級)。
* **Out-of-Scope Enforcement / 超出範疇阻斷:** Programmatically rejects non-GenAI technologies to prevent compliance misclassification (自動拒絕非生成式 AI 技術，防止合規分類混淆)。

---

## 4. ISO 42001 Control Mapping (ISO 42001 控制措施對齊)

* **A.6.2 (AI System Impact Assessment / AI 系統衝擊評估):** Evaluates system deployment impact against public interest, privacy, and systemic risk tiers (針對公共利益、私隱及系統性風險層級進行部署衝擊評估)[cite: 1]。
* **A.8.2 (Data for AI Systems / AI 系統數據管治):** Audits enterprise data provenance, user consent, and shadow AI mitigation (審計企業數據源頭、用戶授權及影子 AI 緩解策略)。
* **A.9.3 (Human Oversight / 人工監督):** Enforces mandatory Human-in-the-Loop override and emergency termination mechanisms (強制執行人工介入覆核與緊急終止機制)。

---

## 5. Contact & Accountability (問責與聯絡人)

* **System Owner / 系統負責人:** Jacky Law 羅子淇
* **LinkedIn / 專業人脈:** [https://www.linkedin.com/in/jackylawck](https://www.linkedin.com/in/jackylawck)

## 5. Contact & Accountability (問責與聯絡人)

* **System Owner:** Jacky Law 羅子淇
* **LinkedIn:** [https://www.linkedin.com/in/jackylawck](https://www.linkedin.com/in/jackylawck)
