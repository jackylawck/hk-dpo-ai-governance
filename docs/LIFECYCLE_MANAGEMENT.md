# System Lifecycle & Change Management / 生命週期與變更管理

**Document Control / 文檔管控:** V1.0  
**Framework Alignment / 框架對齊:** ISO/IEC 42001:2023 (Clause 8 & Annex A.10), EU AI Act (Article 72)  
**Scope / 適用範圍:** HK DPO GenAI Governance Sandbox (Deterministic Tier Classifier / 決定性風險分級器)

---

## 1. Versioning & Baseline Alignment / 版本控制與基準對齊

The current production release (V1.1) is mathematically and logically anchored to the **HK DPO Generative AI Technical and Application Guideline V1.1 (Dec 2025)**. Any update to this regulatory baseline triggers a mandatory system lifecycle review.  
本系統 (V1.1) 邏輯完全錨定香港數字辦《生成式人工智能技術及應用指引》V1.1 (2025年12月)。法規基準更新時，自動觸發生命週期審查。

---

## 2. Change Management Triggers / 變更管理觸發條件

The system enters a mandatory maintenance cycle upon:
當發生以下情境時，系統自動進入強制維護與程式碼審查週期：
* Official release of a new version of the HK DPO Guideline (e.g., V2.0) (數字辦發布新版指引，如 V2.0)。
* Enactment of binding AI legislation by the HK Legislative Council (立法會通過具約束力之 AI 法例)。
* Discovery of critical vulnerabilities in underlying deployment libraries (部署套件發現重大安全漏洞)。

---

## 3. Regression Testing Protocol / 迴歸測試規範

Prior to deploying major logic updates to Streamlit Community Cloud:  
於 Streamlit 雲端部署重大邏輯更新前：
* **Deterministic Unit Testing (決定性單元測試):** The updated Python logic matrix must undergo rigorous unit testing. (更新後之 Python 條件矩陣必須進行嚴格單元測試)。
* **Pass Rate Threshold (通過率閾值):** The system must achieve a **100% pass rate** against a standardized suite of 50 pre-defined compliance scenarios to ensure zero logic drift. (必須於 50 個標準合規測試情境中達成 **100% 通過率**，確保零邏輯漂移)。

---

## 4. Decommissioning Strategy / 系統退役策略

If the system's logic is rendered obsolete by new legal frameworks:  
若新法律框架導致本系統邏輯過時退役：
1. A formal decommissioning notice will be published on the GitHub repository (於 GitHub 發布正式退役公告)。
2. The Streamlit instance will be taken offline permanently to prevent reliance on outdated logic (永久下線 Web App，防止誤用過時邏輯)。
3. The repository will be archived to preserve the historical audit trail (歸檔 GitHub 倉庫，保留歷史審計軌跡)。
