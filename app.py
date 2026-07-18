import streamlit as st

# ==========================================
# 1. 頁面配置與高管級 UI 設定
# ==========================================
st.set_page_config(
    page_title="HK DPO GenAI Governance Station",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 初始化語言設定 (預設繁體中文)
if 'lang' not in st.session_state: 
    st.session_state.lang = '繁體中文'

is_zh = st.session_state.lang == '繁體中文'

# ==========================================
# 2. 側邊欄 UI 設計 (純官方界定與免責)
# ==========================================
with st.sidebar:
    st.markdown("### 🌐 UI Language / 介面語言" if is_zh else "### 🌐 UI Language")
    lang_choice = st.radio("Select Language", ['繁體中文', 'English'], index=0 if is_zh else 1, label_visibility="collapsed")
    if lang_choice != st.session_state.lang:
        st.session_state.lang = lang_choice
        st.rerun()
    
    st.markdown("---")
    st.markdown("### 🏛️ 官方指引核對基準" if is_zh else "### 🏛️ Official Baseline")
    st.caption("本系統核心指標 100% 依據香港數字政策辦公室 (DPO) 《香港生成式人工智能技術及應用指引》V1.1 (2025年12月) 編碼。\n\n⚠️ **超出本指引涵蓋範圍之合規問題，系統將不予評判。**" if is_zh else "Coded 100% based on the HK DPO Generative AI Guideline V1.1 (Dec 2025).\n\n⚠️ **Compliance issues beyond the scope of this Guideline will not be evaluated.**")

    st.markdown("---")
    st.markdown("### 👥 官方持份者角色映射" if is_zh else "### 👥 Stakeholder Role Mapping")
    st.caption("1. 技術開發者 (Technology Developers)\n2. 服務提供者 (Service Providers)\n3. 服務使用者 (Service Users)" if is_zh else "1. Technology Developers\n2. Service Providers\n3. Service Users")

    st.markdown("---")
    st.caption("🚨 *註：本專案為獨立第三方合規工具，與香港特區政府數字政策辦公室無任何官方隸屬關係。*" if is_zh else "🚨 *Note: This is an independent third-party tool and has no official affiliation with the HK DPO.*")

# ==========================================
# 3. 主畫面標題與獨立性聲明 (硬化防禦邊界)
# ==========================================
st.title("⚖️ 香港數字政策辦公室 (DPO) AI 合規工作區" if is_zh else "⚖️ HK DPO GenAI Compliance Workstation")

if is_zh:
    st.warning(
        "⚠️ **獨立性與免責聲明：** 本系統為**獨立開發之非官方開源合規沙盒**，僅供個人研究及企業內部管治自查參考。本系統非特區政府數字政策辦公室（DPO）之官方工具，其診斷輸出絕對不構成正式的法律意見或政府合規背書。",
        icon="🛡️"
    )
else:
    st.warning(
        "⚠️ **Independence & Disclaimer:** This system is an **independent, unofficial open-source compliance sandbox** for personal research and internal governance reference only. It is NOT an official tool published by the HK Digital Policy Office (DPO). The outputs do not constitute formal legal advice or official regulatory endorsement.",
        icon="🛡️"
    )

tabs = st.tabs([
    "💬 官方情境診斷 (Scenario Q&A)" if is_zh else "💬 Scenario Q&A",
    "📊 風險與行業管治 (Risk & Industry)" if is_zh else "📊 Risk & Industry",
    "📝 14項法定內部政策 (14-Point Checklist)" if is_zh else "📝 14-Point Checklist"
])

# ==========================================
# 4. 分頁一：官方情境診斷 (具有技術類型過濾的主動退回引擎)
# ==========================================
with tabs[0]:
    st.subheader("👨‍💼 DPO 指引智能情境診斷引擎" if is_zh else "👨‍💼 DPO Guideline Scenario Diagnostic Engine")
    st.markdown("請描述您在企業中遇到的 AI 管治情境。系統將嚴格依據 DPO 官方指引為您進行風險拆解，**若問題超出指引範圍將直接提示**。" if is_zh else "Describe your enterprise AI governance scenario. The system will provide a risk breakdown strictly based on official DPO guidelines. **Out-of-scope issues will be explicitly flagged.**")
    
    # 雙語歷史紀錄分流
    if "messages_zh" not in st.session_state:
        st.session_state.messages_zh = [{"role": "assistant", "content": "您好！我是基於香港 DPO 指引構建的企業合規助手。請問今天有什麼 AI 導入的場景需要探討？（請注意：超出《香港生成式人工智能技術及應用指引》範圍的提問，我將直接告知無法處理。）"}]
    if "messages_en" not in st.session_state:
        st.session_state.messages_en = [{"role": "assistant", "content": "Hello! I am an enterprise compliance assistant built on the HK DPO Guidelines. What AI deployment scenario would you like to discuss today? (Note: I will explicitly decline to answer queries outside the scope of the Hong Kong Generative AI Guideline.)"}]

    current_messages = st.session_state.messages_zh if is_zh else st.session_state.messages_en

    for msg in current_messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    input_placeholder = "請輸入企業情境... (如：市場部主管私自用 iPad 上傳客戶名單)" if is_zh else "Type your scenario here... (e.g., Marketing head used personal iPad to upload client data)"
    if prompt := st.chat_input(input_placeholder):
        current_messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            # 規則引擎關鍵字定義
            shadow_ai_words = ["ipad", "私自", "影子", "客戶名單", "shadow", "unauthorized", "personal"]
            out_of_scope_law_words = ["勞工法", "報稅", "薪資", "employment ordinance", "tax", "salary", "休假", "leave"]
            
            # 核心硬化：傳統判別式機器學習（ML）過濾關鍵字
            traditional_ml_words = ["隨機森林", "random forest", "回歸", "regression", "聚類", "clustering", "傳統機器學習", "歷史數據預測", "不涉及任何文本", "不涉及文本", "不具備內容生成"]

            # 優先判定 1：是否屬於傳統非生成式 ML (精準狙擊、主動退回)
            if any(w in prompt.lower() for w in traditional_ml_words):
                if is_zh:
                    response = """⚠️ **技術類型超出指引範疇 (Out of Technological Scope)**
                    
**合規審計評判：** 您所描述的場景採用了**傳統判別式機器學習演算法（如隨機森林模型）**，且明確指出「不涉及任何文本、音頻、影像的生成」。

依據數字辦指引第一章（第 3 頁）之官方明文界定，本指引**僅適用於具備內容生成與創作能力的生成式人工智能（主要指基於 Transformer 架構的大型基礎模型）**[cite: 1, 2]。

**結論：** 本套物流需求與路線預測系統**完全不適用**本《生成式人工智能技術及應用指引》[cite: 1, 2]。本工作區依法拒絕對其進行 GenAI 風險定級，以避免為企業帶來「合規混淆風險」。建議貴司回歸普通數據治理，並參考 PCPD 香港私隱專員公署發布之通用《開發及使用人工智能道德標準指引》。"""
                else:
                    response = """⚠️ **Out of Technological Scope**
                    
**Compliance Audit Verdict:** The scenario described utilizes **traditional discriminative machine learning (e.g., Random Forest models)** and explicitly states that it involves no generation of text, audio, or video.

Per Chapter 1 (Page 3) of the official DPO guideline, this Guideline **exclusively applies to Generative AI technologies (primarily foundation models based on Transformer architectures) that possess content creation capabilities**[cite: 1, 2].

**Conclusion:** This logistics predictive model is **completely out of scope** for the *Generative AI Technical and Application Guideline*[cite: 1, 2]. The system explicitly refuses to assign a GenAI risk tier to prevent corporate compliance misalignment. We recommend referencing the general AI guidelines published by the PCPD instead."""

            # 判定 2：是否涉及其他非 AI 法規
            elif any(w in prompt.lower() for w in out_of_scope_law_words):
                if is_zh:
                    response = "⚠️ **業務範圍超出指引範疇 (Out of Scope)**\n\n您提及的問題（如勞工法例、稅務或一般薪酬管理）超出了《香港生成式人工智能技術及應用指引》的涵蓋範圍。本系統僅處理與生成式 AI 模型開發、部署、資料私隱及 AI 應用政策相關的管治審查。"
                else:
                    response = "⚠️ **Out of Scope**\n\nThe issue you mentioned (e.g., general employment laws, tax, or payroll) is outside the scope of the *Hong Kong Generative Artificial Intelligence Technical and Application Guideline*. This system only evaluates governance related to GenAI model development, deployment, data privacy, and AI policies."
            
            # 判定 3：DPO 指引範圍內的影子 AI 情境
            elif any(w in prompt.lower() for w in shadow_ai_words):
                if is_zh:
                    response = """🚨 **偵測到違規：「影子 AI」與潛在「資料外洩」風險！**
                    
基於 DPO 官方指引的 14 項內部政策規範，您的情境直接違反了「獲准使用的工具」、「獲准許裝置」以及「獲准輸入的資訊種類」等核心要求。

**依據指引，建議優先採取的兩個治理步驟：**
1. **啟動事故應變機制：** 依據政策第 14 項，評估客戶名單外洩的情況，立即要求停止使用該免費工具，並按照指引中「報告資料外洩」的流程處理，必要時通報私隱專員公署 (PCPD)。
2. **紀律處分與建立白名單：** 依據政策明訂的「違反政策可能導致的後果」進行處置，同時為員工提供已獲批准的內部安全 AI 工具清單（政策第 1 項）。"""
                else:
                    response = """🚨 **Breach Detected: "Shadow AI" and Potential "Data Breach"!**
                    
Based on the 14 mandatory internal policies from the DPO guideline, this scenario directly violates rules regarding "Permitted tools," "Permitted devices," and "Permissible types of input information."

**Top 2 Governance Actions Recommended per the Guideline:**
1. **Trigger Incident Response (Policy Item 14):** Assess the PII leak, halt the use of the unauthorized tool immediately, and execute the "data breach reporting" protocol, including notifying the PCPD if thresholds are met.
2. **Enforcement & Whitelisting (Policy Item 1):** Enforce consequences as specified in your policy for violations, and provide employees with a whitelist of officially approved, secure Al tools."""
            
            # 判定 4：一般性兜底回覆
            else:
                if is_zh:
                    response = """💡 **收到您的情境描述。**
                    
建議您切換至上方的 **「📝 14項法定內部政策」** 標籤頁，逐一檢核您的企業是否已涵蓋此情境所需的管控機制。若您的情境與 AI 管治無關，則屬於本系統的**超出範圍 (Out of Scope)**。"""
                else:
                    response = """💡 **Scenario Logged.**
                    
We recommend navigating to the **"📝 14-Point Checklist"** tab above to verify if your organisation has controls covering this situation. If your scenario is unrelated to AI governance, it is **Out of Scope** for this system."""
            
            st.markdown(response)
            current_messages.append({"role": "assistant", "content": response})

# ==========================================
# 5. 分頁二：風險與行業管治 (保持 100% 官方文字對齊)
# ==========================================
with tabs[1]:
    st.subheader("📌 依據指引第九至十頁：風險分類系統判定" if is_zh else "📌 Per Page 11: Risk Classification System")
    
    risk_profiles = {
        "Unacceptable": {
            "zh_label": "不可接受風險 (Unacceptable Risk) - 對社會構成生存性威脅、潛意識操控",
            "en_label": "Unacceptable Risk - Existential threats, subliminal manipulation",
            "zh_strategy": "全面禁止。涉及開發或部署的行為須承擔法律責任。",
            "en_strategy": "Full prohibition. Legal liability for development/deployment."
        },
        "High": {
            "zh_label": "高風險 (High Risk) - 關鍵性基礎設施系統（如醫療診斷系統、自動駕駛技術）",
            "en_label": "High Risk - Critical infrastructure systems (e.g., healthcare diagnostics, autonomous vehicles)",
            "zh_strategy": "必須進行合規性評估；必須設有人類參與的監督機制、實時監測和持續監控。",
            "en_strategy": "Conformity assessments, Human-in-the-loop requirements, Real-time monitoring."
        },
        "Limited": {
            "zh_label": "有限風險 (Limited Risk) - 帶來中等社會影響的系統（如人才招聘系統、教育人工智能應用）",
            "en_label": "Limited Risk - Systems with moderate societal impact (e.g., recruitment tools, educational AI)",
            "zh_strategy": "履行資訊透明的責任；提供用戶選擇退出的機制；每年定期進行合規審計。",
            "en_strategy": "Transparency obligations, User opt-out mechanisms, Annual compliance audits."
        },
        "Low": {
            "zh_label": "低風險 (Low Risk) - 屬於最低風險類別的應用（如垃圾郵件過濾系統、創意設計工具）",
            "en_label": "Low Risk - Minimal-risk applications (e.g., spam filters, creative tools)",
            "zh_strategy": "企業自我認證。",
            "en_strategy": "Self-certification."
        }
    }
    
    selected_tier = st.selectbox(
        "選擇預期導入的 AI 業務場景風險類別 (Select Risk Tier Profile):",
        list(risk_profiles.keys()),
        format_func=lambda x: risk_profiles[x]["zh_label"] if is_zh else risk_profiles[x]["en_label"]
    )
    
    tier_data = risk_profiles[selected_tier]
    if selected_tier == "Unacceptable":
        st.error(tier_data["zh_strategy"] if is_zh else tier_data["en_strategy"])
    elif selected_tier == "High":
        st.warning(tier_data["zh_strategy"] if is_zh else tier_data["en_strategy"])
    elif selected_tier == "Limited":
        st.info(tier_data["zh_strategy"] if is_zh else tier_data["en_strategy"])
    else:
        st.success(tier_data["zh_strategy"] if is_zh else tier_data["en_strategy"])

    st.markdown("---")
    st.subheader("📌 依據指引第 2.2.2 節：以行業為綱的香港可信人工智能原則" if is_zh else "📌 Per Section 2.2.2: Industry-Oriented Principles")
    
    industry = st.selectbox(
        "選擇您的企業所屬行業 (Select Industry Vertical):",
        ["金融 (Finance)", "醫療 (Healthcare)", "法律 (Legal)", "教育 (Education)", "新聞 (Journalism)", "旅遊 (Tourism)", "零售 (Retail)", "物流 (Logistics)", "工業 (Industry)"]
    )
    
    if industry == "金融 (Finance)":
        st.markdown(
            "### 🏦 金融 (Finance)\n"
            "- **公平性**：應確保所有潛在的候選項均能公平地得到被推薦的機會，限制通過人工設置、干預模型訓練或其他方式干預推薦權重。[cite: 1, 2]\n"
            "- **退出與人為覆核選項**：在早期階段，**應盡可能提供退出使用生成式人工智能的選項**，而不是只能加入，以及盡可能要求客戶對生成式人工智能產生的決定作出人為決定。若無法提供退出選項，銀行應提供相關渠道讓客戶要求檢視決定。[cite: 1, 2]"
        )
    elif industry == "醫療 (Healthcare)":
        st.markdown(
            "### 🏥 醫療 (Healthcare)\n"
            "- **不直接作為診斷**：生成內容**應不能直接作為診斷報告**，應由執業人員審核後作為參考。[cite: 1, 2]\n"
            "- **資料最小化與用途鎖定**：敏感資訊的收集應遵守最小化原則。相關資訊不得以任何原因改變資料用途，**用於保險、職業推薦等行業**。[cite: 1, 2]"
        )
    elif industry == "法律 (Legal)":
        st.markdown(
            "### ⚖️ 法律 (Legal)\n"
            "- **原文可追溯性**：生成內容**應附有可追溯至法律原文的引用連結**。不能直接作為法律文檔，應由執業人員審核後作為參考。[cite: 1, 2]\n"
            "- **禁止公共服務處理秘密**：避免使用**缺乏安全保密保障的公共人工智能服務**處理涉及商業秘密和私隱資訊的法律案件。[cite: 1, 2]"
        )
    elif industry == "教育 (Education)":
        st.markdown(
            "### 🎓 教育 (Education)\n"
            "- **規範而非普遍禁止**：不建議普遍禁止學生使用，但在課業中使用應取得教師的同意，同時確保生成內容能明確被識別。[cite: 1, 2]\n"
            "- **人工覆核批改**：教師用於批改作業和試卷時，**應確保最終結果經由人工審核**。[cite: 1, 2]"
        )
    elif industry == "新聞 (Journalism)":
        st.markdown(
            "### 📰 新聞 (Journalism)\n"
            "- **查證與審核**：減少模型幻覺等問題導致的生成內容失實。**生成內容必須經由事實查證和全文審核後才能用於公開報導**。[cite: 1, 2]\n"
            "- **嚴禁捏造事實**：不得使用生成式人工智能製作偏離事實、捏造事實的文字、圖像、語音和視像等內容並以各種形式混入新聞報導。[cite: 1, 2]"
        )
    elif industry == "旅遊 (Tourism)":
        st.markdown(
            "### 🧳 旅遊 (Tourism)\n"
            "- **公平推薦**：在旅遊推薦、客房預訂或智慧客服等服務中，要確保對不同客源能做到公平和無歧視性推薦。[cite: 1, 2]\n"
            "- **平衡私隱與精準度**：定期審查生成內容是否存在不實或誤導性資料，嚴防過度搜集和不當使用旅客資訊。[cite: 1, 2]"
        )
    elif industry == "零售 (Retail)":
        st.markdown(
            "### 🛍️ 零售 (Retail)\n"
            "- **算法公正性**：用於產品推薦、動態定價或顧客服務時，須確保同一區域及客群得到合理且透明的算法結果，以維持市場公正性。[cite: 1, 2]\n"
            "- **配備人手支援**：建議在顧客對生成式人工智能產生困惑或疑慮時，**配備人手支援和即時回覆機制**，以保障顧客權益。[cite: 1, 2]"
        )
    elif industry == "物流 (Logistics)":
        st.markdown(
            "### 📦 物流 (Logistics)\n"
            "- **降低偏誤風險**：在運具調度與智慧路線規劃中應使用可靠且最新的交通與地理資訊，降低偏誤風險。[cite: 1, 2]\n"
            "- **隱私控制與產業安全**：處理個人位址時必須採用適當的加密與存取控制方案。若採用自動化分揀，應定期檢視系統安全性與穩定性，避免碰撞或風險事件。[cite: 1, 2]"
        )
    elif industry == "工業 (Industry)":
        st.markdown(
            "### 🏗️ 工業 (Industry)\n"
            "- **主管工程師覆核**：若引入預測保養或自動故障診斷功能，亦應確保生成式人工智能所生成結果**能經主管工程師或品控人員覆核**。[cite: 1, 2]\n"
            "- **防止商業秘密外洩**：密切關注系統在處理**機密配方、專利技術或其他具有商業機密的信息**時的保安措施，以防止技術外洩或專利侵權。[cite: 1, 2]"
        )

# ==========================
# 6. 分頁三：14項法定內部政策 (自查表)
# ==========================
with tabs[2]:
    st.subheader("📌 採用生成式人工智能服務的機構應制訂之內部政策" if is_zh else "📌 Mandatory Internal Policy Components")
    st.markdown("依據官方指引第 25 頁（英文版第 31 頁）明文列出之 14 項要素進行自查：" if is_zh else "Self-audit based on the 14 elements explicitly listed on page 31 of the official guideline:")
    
    policy_checks = [
        st.checkbox("1. 獲准使用的工具" if is_zh else "1. Permitted tools"),
        st.checkbox("2. 獲准許的用途" if is_zh else "2. Permissible use"),
        st.checkbox("3. 政策適用性" if is_zh else "3. Policy applicability"),
        st.checkbox("4. 獲准輸入的資訊種類及數量" if is_zh else "4. Permissible types/amounts of input"),
        st.checkbox("5. 輸出資訊的獲准許用途" if is_zh else "5. Permissible use of output"),
        st.checkbox("6. 輸出資訊的獲准許儲存方式" if is_zh else "6. Permissible storage of output"),
        st.checkbox("7. 遵從其他相關內部政策" if is_zh else "7. Alignment with internal policies"),
        st.checkbox("8. 訂明禁止非法或有害活動" if is_zh else "8. Prohibit unlawful/harmful activities"),
        st.checkbox("9. 僱員擔當審查員的責任" if is_zh else "9. Employee responsibility as human reviewers"),
        st.checkbox("10. 獲准許裝置" if is_zh else "10. Permitted devices"),
        st.checkbox("11. 獲准許使用者" if is_zh else "11. Permitted users"),
        st.checkbox("12. 穩健的用戶憑證" if is_zh else "12. Robust user credentials"),
        st.checkbox("13. 保安設定" if is_zh else "13. Security settings"),
        st.checkbox("14. 事故及資料外洩應變" if is_zh else "14. Incident and data breach response")
    ]
    
    passed_counts = sum(policy_checks)
    readiness_score = (passed_counts / 14) * 100
    st.markdown("---")
    st.markdown(f"### 📊 政策完備度: **{readiness_score:.0f}%** ({passed_counts}/14)" if is_zh else f"### 📊 Policy Readiness: **{readiness_score:.0f}%** ({passed_counts}/14)")
    st.progress(readiness_score / 100)
