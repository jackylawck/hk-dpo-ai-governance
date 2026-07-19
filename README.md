# HK DPO GenAI Governance Sandbox (香港數字辦指引合規沙盒)

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge.svg)](https://hk-dpo-ai-governance.streamlit.app/)
👉 **[點此立即訪問線上動態合規風險評分卡系統 (Live Sandbox App)](https://hk-dpo-ai-governance.streamlit.app/)**

An enterprise GenAI compliance workstation built 100% deterministically per the HK Digital Policy Office (DPO) "Generative AI Technical and Application Guideline V1.1" (Dec 2025). 
本系統為一套企業級生成式人工智能合規工作站，核心邏輯 100% 依據香港數字政策辦公室 (DPO) 於 2025 年 12 月發布之《香港生成式人工智能技術及應用指引》V1.1 進行決定性編碼。

---

### 🧱 Governance Methodology & Architecture (管治方法論與架構)

This project is powered by the **"Jacky Law Human-Centred AI Governance Stack"** and features rigid Engineering-driven Guardrails to prevent compliance illusions:
本專案採用 **「Jacky Law 人本 AI 管治五層架構」** 進行頂層設計，並實作了高強度的工程化決定性護欄，以杜絕任何合規幻覺：

1. **100% Deterministic Failure-Safe Logic (100% 決定性失效安全邏輯):** Unlike unstable AI wrappers, this system implements a strict conditional hard-gate mechanism. It completely eliminates generative hallucinations when auditing organizational readiness.
2. **Automated 4-Tier Risk Classification (自動化四級風險分類):** Algorithms automatically classify organizational scenarios into Very High Risk, High Risk, Moderate Risk, or Minimal Risk based on systemic variables (e.g., core government functions vs. internal back-office administration).
3. **Proactive Out-of-Scope Blocking (主動超出範疇阻斷機制):** The compliance matrix is hardened to evaluate GenAI technologies only. Traditional discriminative or statistical machine learning models (e.g., Random Forest, XGBoost) are programmatically rejected with a clear out-of-scope warning.

---

### 🛡️ Enterprise Executive Audit Scorecard (企業高管審計評分卡)

The workstation evaluates corporate AI procurement and integration workflows across key structural layers:
本工作站針對企業引進 AI 的採購與整合工作流，進行多維度的結構化審計評估：

* **Data Provenance & Privacy Auditing (數據源頭與隱私審查):** Ensures explicit boundary controls over PII, model training inputs, and vendor accountability metrics.
* **Organizational Change & Training Alignment (組織變更與培訓對齊):** Audits whether mandatory internal usage guidelines, staff cross-training, and shadow AI mitigation strategies are established.
* **Human-in-the-Loop Override Verification (人工介入與終止機制驗證):** Evaluates if the system architecture permits real-time human override and risk containment under extreme operational drift.

---

### ⚙️ Local Environment & Requirements (本地環境配置)

To spin up this compliance workstation locally, ensure you have Python 3.11+ installed and execute the following commands:
若您希望於本地環境啟動本合規工作站，請確保已安裝 Python 3.11+ 並執行以下命令：

1. **Clone the repository (克隆倉庫):**
   ```bash
   git clone [https://github.com/jackylawck/hk-dpo-ai-governance.git](https://github.com/jackylawck/hk-dpo-ai-governance.git)
   cd hk-dpo-ai-governance
