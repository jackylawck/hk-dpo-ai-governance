# Technological Limitations & Failure-Safe Design (技術限制與安全退回設計)

## 1. Scope of the HK DPO Guideline (香港數字辦指引的適用邊界)
* **EN:** This compliance workstation is strictly designed for the **HK Generative AI Technical and Application Guideline V1.1**[cite: 1, 2]. It is intentionally bounded to **Generative AI** technologies (e.g., Transformer architectures, LLMs)[cite: 1, 2].
* **ZH (繁中):** 本合規系統嚴格專注於**香港數字政策辦公室《生成式人工智能技術及應用指引》V1.1**的範疇[cite: 1, 2]。其邏輯與控制措施僅適用於**生成式 AI**（如大語言模型、Transformer 架構）[cite: 1, 2]。

## 2. Intentional Boundaries (刻意設定的拒絕作答邏輯)
* **Discriminative/Traditional AI (傳統判別式 AI):** Non-generative models (e.g., Random Forest, regression algorithms for logistics demand forecasting) are classified as **Out of Scope** under this specific guideline. The system will direct users to verify basic data governance (14-point checklist) rather than misleadingly assigning GenAI risk tiers.
  非生成式模型（如用於物流預測的隨機森林、線性回歸等傳統演算法）不屬於本生成式指引的管轄範圍。系統將主動提示切換，引導用戶回歸 14 項基本治理，而非給出錯誤的生成式風險評級。
* **Cross-Jurisdictional Legal Constraints (跨法域法律約束):** Queries regarding international legal frameworks (e.g., EU AI Act, GDPR) are systematically flagged as **Out of Scope**. Users must consult licensed legal practitioners for extraterritorial compliance.
  涉及歐盟 AI 法案、GDPR 等跨境多法域的問題將被系統自動識別為「超出範圍」，用戶應尋求專業法律顧問協助，以防範「合規幻覺 (Compliance Illusion)」。
