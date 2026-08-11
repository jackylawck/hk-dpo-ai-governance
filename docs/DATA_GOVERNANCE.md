# Data Governance & Privacy Architecture / 數據管治與隱私架構

**Document Control / 文檔管控:** V1.0  
**Framework Alignment / 框架對齊:** ISO/IEC 42001:2023 (Annex A.7), GDPR / HK PDPO (Cap. 486)  
**Scope / 適用範圍:** HK DPO GenAI Governance Sandbox (Deterministic Tier Classifier / 決定性風險分級器)

---

## 1. Data Provenance & Lineage / 數據來源與血統

* **Ruleset Baseline (規則庫基準):** Hard-coded strictly based on the HK Digital Policy Office (DPO) "Generative AI Technical and Application Guideline V1.1" (Dec 2025).  
  邏輯矩陣嚴格依據香港數字政策辦公室《生成式人工智能技術及應用指引》V1.1 (2025年12月) 編碼。
* **Input Data Limits (輸入限制):** System strictly processes categorical variables (e.g., "Internal Use", "Public Facing").  
  系統僅處理類別型組織變數（如「內部使用」、「面向公眾」），不接收文字段落。

---

## 2. Data Minimization & Privacy by Design / 資料最小化與隱私設計

* **Zero PII Collection (零個人資料收集):** The sandbox does not request, accept, or parse any Personally Identifiable Information (PII) or confidential text.  
  沙盒絕對不索取、不接收亦不解析任何個人識別資訊 (PII) 或機密文本。
* **Zero Persistent Storage (零持久化儲存):** Uses no external databases (e.g., SQL/NoSQL). All parameters exist solely in volatile RAM.  
  完全不使用任何外部資料庫，所有參數僅存於揮發性記憶體 (RAM) 中。
* **Automatic Destruction (自動銷毀機制):** Upon browser closure or session reset, all state variables and generated scorecards are instantly destroyed.  
  關閉瀏覽器或重置會話時，所有輸入狀態與評分卡即刻銷毀。

---

## 3. Proactive Out-of-Scope Blocking / 主動超出範疇阻斷機制

To prevent misclassification, inputs related to traditional discriminative machine learning models (e.g., Random Forest, XGBoost) are programmatically rejected with an out-of-scope warning.  
為防止合規混淆，若輸入傳統判別式機器學習模型（如隨機森林、XGBoost），系統將自動攔截並發出超出範疇警告。
