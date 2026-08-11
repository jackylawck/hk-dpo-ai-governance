# Human Oversight & Escalation Protocol / 人工監督與申訴機制

**Document Control / 文檔管控:** V1.0  
**Framework Alignment / 框架對齊:** ISO/IEC 42001:2023 (Annex A.8.3), EU AI Act (Article 14)  
**Scope / 適用範圍:** HK DPO GenAI Governance Sandbox (Deterministic Tier Classifier / 決定性風險分級器)

---

## 1. Human-in-the-Loop (HITL) Philosophy / 人機協同理念

This AI governance sandbox is designed exclusively as a **Decision Support System (決策支援系統)**. The final accountability for compliance assessment, risk tiering, and deployment rests entirely with the designated human executive, AI Governance Professional, or legal counsel.  
本管治沙盒定位為決策支援系統。合規評估、風險分級及部署之最終問責，完全由指定之企業高管、AI 管治專家或法務顧問承擔。

---

## 2. Operational Oversight Mechanisms / 營運監督機制

* **Pre-Execution Parameter Verification (執行前參數驗證):** Users must manually input organizational parameters accurately before any algorithmic routing begins (任何演算法路由啟動前，使用者必須精確輸入組織參數)。
* **Executive Sign-off (高管審核簽署):** All system-generated risk scorecards must be reviewed and cross-verified against official legal advice before board reporting (所有評分卡於呈報董事會前，必須經由法務意見覆核)。
* **Human Override Authority (人工覆核與否決權):** Human operators possess the absolute authority to override the system's generated risk tier based on nuanced corporate context (管治人員有權依據企業實際情境，否決或修正系統生成之風險等級)。

---

## 3. Escalation & Feedback Process / 申訴與異常回饋流程

In the event of a suspected logic error or conflicting compliance output (若發現邏輯錯誤或合規輸出衝突):
1. **Immediate Cessation (立即暫停):** Cease utilizing the specific generated scorecard for official reporting (立即停止使用該疑義評分卡作為官方報告)。
2. **Log & Report (紀錄與通報):** Capture the specific input parameters and report to the AI Governance Lead (截取特定輸入參數，通報至 AI 管治負責人)。
3. **Manual Code Audit (人工程式碼審計):** The AI Governance Lead will conduct a manual review of the deterministic Python `if-else` logic matrix (管治負責人將對 Python 條件邏輯矩陣進行人工審計)。
4. **Logic Patch Deployment (邏輯修補部署):** If a logical contradiction is verified, a patch will be deployed and logged in the risk register (證實邏輯矛盾後部署修補檔，並納入風險登記冊)。
