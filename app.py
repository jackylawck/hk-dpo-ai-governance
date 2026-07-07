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

# 初始化語言設定
if 'lang' not in st.session_state: 
    st.session_state.lang = '繁體中文'

is_zh = st.session_state.lang == '繁體中文'

# ==========================================
# 2. 側邊欄 UI 設計 (100% 依據官方文件第 2 頁持份者定義)
# ==========================================
with st.sidebar:
    st.markdown("### 🌐 UI Language / 介面語言")
    lang_choice = st.radio(
        "Select Language / 選擇語言", 
        ['繁體中文', 'English'], 
        index=0 if is_zh else 1, 
        label_visibility="collapsed"
    )
    
    if lang_choice != st.session_state.lang:
        st.session_state.lang = lang_choice
        st.rerun()
    
    st.markdown("---")
    st.markdown("### 🏛️ 官方指引核對基準" if is_zh else "### 🏛️ Official Guideline Baseline")
    st.caption(
        "本系統核心指標 100% 依據香港數字政策辦公室 (DPO) 與香港生成式人工智能研發中心 (HKGAI) 發布之《香港生成式人工智能技術及應用指引》V1.1 (2025年12月) 明文決定性編碼。" 
        if is_zh else 
        "100% deterministically coded based on the HK Digital Policy Office (DPO) & HKGAI 'Hong Kong Generative Artificial Intelligence Technical and Application Guideline' V1.1 (December 2025)."
    )
    
    st.markdown("---")
    st.markdown("### 👥 官方持份者角色映射" if is_zh else "### 👥 Stakeholder Role Mapping")
    st.caption(
        "1. 技術開發者 (Technology Developers)\n2. 服務提供者 (Service Providers)\n3. 服務使用者 (Service Users)"
        if is_zh else
        "1. Technology Developers\n2. Service Providers\n3. Service Users"
    )

# ==========================================
# 3. 主畫面標題與導言 (100% 依據官方文件第 1 頁背景)
# ==========================================
if is_zh:
    st.title("⚖️ 香港數字政策辦公室 (DPO) 《生成式人工智能技術及應用指引》智能合規工作區")
    st.markdown("### 企業導入前置風險定級與合規評分卡 (DPO 官方核心基準)")
else:
    st.title("⚖️ HK Digital Policy Office (DPO) GenAI Technical & Application Guideline Workstation")
    st.markdown("### Enterprise GenAI Pre-Deployment Audit Scorecard (Official DPO Baseline)")

# 建立分頁
tabs = st.tabs([
    "📊 風險分類系統 (Risk Classification System)" if is_zh else "📊 Risk Classification System",
    "🏢 特定行業應用原則 (Industry-Oriented Principles)" if is_zh else "🏢 Industry-Oriented Principles",
    "📝 機構內部政策指引 (Organisation Policies)" if is_zh else "📝 Organisation Policies"
])

# ==========================================
# 4. 分頁一：風險分類系統 (100% 對應官方文件第 9-10 頁「表格 1」)
# ==========================================
with tabs[0]:
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
    
    st.markdown("---")
    st.markdown("#### ⚖️ 官方規定的治理策略 (Official Governance Strategy):" if is_zh else "#### ⚖️ Official Governance Strategy:")
    
    tier_data = risk_profiles[selected_tier]
    if selected_tier == "Unacceptable":
        st.error(tier_data["zh_strategy"] if is_zh else tier_data["en_strategy"])
    elif selected_tier == "High":
        st.warning(tier_data["zh_strategy"] if is_zh else tier_data["en_strategy"])
    elif selected_tier == "Limited":
        st.info(tier_data["zh_strategy"] if is_zh else tier_data["en_strategy"])
    else:
        st.success(tier_data["zh_strategy"] if is_zh else tier_data["en_strategy"])

# ==========================================
# 5. 分頁二：特定行業應用原則 (100% 對應官方文件第 32-34 頁 / 英文版第 41-44 頁明文)
# ==========================================
with tabs[1]:
    st.subheader("📌 依據指引第 2.2.2 節：以行業為綱的香港可信人工智能原則" if is_zh else "📌 Per Section 2.2.2: Industry-Oriented Principles")
    
    industry = st.selectbox(
        "選擇您的企業所屬行業 (Select Industry Vertical):",
        ["金融 (Finance)", "醫療 (Healthcare)", "法律 (Legal)", "教育 (Education)", "新聞 (Journalism)", "旅遊 (Tourism)", "零售 (Retail)", "物流 (Logistics)", "工業 (Industry)"]
    )
    
    st.markdown("---")
    if industry == "金融 (Finance)":
        st.markdown(
            "### 🏦 金融 (Finance) - 官方文件第 32 頁明文要求：\n"
            "- **公平性**：應確保所有潛在的候選項均能公平地得到被推薦的機會，限制通過人工設置、干預模型訓練或其他方式干預推薦權重。\n"
            "- **退出與人為覆核選項**：在早期階段，**應盡可能提供退出使用生成式人工智能的選項**，而不是只能加入，以及盡可能要求客戶對生成式人工智能產生的決定作出人為決定。若無法提供退出選項，銀行應提供相關渠道讓客戶要求檢視決定。"
            if is_zh else
            "### 🏦 Finance - Page 42 Official Requirements:\n"
            "- **Fairness**: All potential candidates should have an equal opportunity to be recommended; restrict interference with recommendation weights through manual settings or model training interventions.\n"
            "- **Opt-out & Human Review**: Customers should be provided with the option to opt out of using GenAI and request human intervention on GenAI-generated decisions during the early stage of deploying customer-facing applications. If an opt-out cannot be provided, banks should provide channels for customers to request a review."
        )
    elif industry == "醫療 (Healthcare)":
        st.markdown(
            "### 🏥 醫療 (Healthcare) - 官方文件第 33 頁明文要求：\n"
            "- **不直接作為診斷**：生成內容**應不能直接作為診斷報告**，應由執業人員審核後作為參考。\n"
            "- **資料最小化與用途鎖定**：敏感資訊的收集應遵守最小化原則。相關資訊不得以任何原因改變資料用途，**用於保險、職業推薦等行業**。"
            if is_zh else
            "### 🏥 Healthcare - Page 42 Official Requirements:\n"
            "- **No Direct Diagnostic Reports**: GenAI content should not be used directly as diagnostic reports but should be reviewed by licensed professionals as a reference.\n"
            "- **Data Minimisation & Purpose Limitation**: Adhere to the principle of data minimisation for sensitive information. Data collected for healthcare purposes should not be repurposed for insurance, job recommendations, or other industries."
        )
    elif industry == "法律 (Legal)":
        st.markdown(
            "### ⚖️ 法律 (Legal) - 官方文件第 33 頁明文要求：\n"
            "- **原文可追溯性**：生成內容**應附有可追溯至法律原文的引用連結**。不能直接作為法律文檔，應由執業人員審核後作為參考。\n"
            "- **禁止公共服務處理秘密**：避免使用**缺乏安全保密保障的公共人工智能服務**處理涉及商業秘密和私隱資訊的法律案件。"
            if is_zh else
            "### ⚖️ Legal - Page 42 Official Requirements:\n"
            "- **Traceable Citations**: Generated content should include citations that trace back to the original legal texts and serve as a reference after review by legal professionals.\n"
            "- **Public Service Prohibitions**: Sensitive legal cases involving trade secrets or private information should not be processed using public AI services that lack security and confidentiality guarantees."
        )
    elif industry == "教育 (Education)":
        st.markdown(
            "### 🎓 教育 (Education) - 官方文件第 33 頁明文要求：\n"
            "- **規範而非普遍禁止**：不建議普遍禁止學生使用，但在課業中使用應取得教師的同意，同時確保生成內容能明確被識別。\n"
            "- **人工覆核批改**：教師用於批改作業和試卷時，**應確保最終結果經由人工審核**。"
            if is_zh else
            "### 🎓 Education - Page 43 Official Requirements:\n"
            "- **Regulation Over Absolute Banning**: Regulate the use and scope rather than outright banning students; students should obtain teacher approval before using AI in coursework, and content should be clearly identifiable.\n"
            "- **Human Review for Grading**: If AI is used for grading assignments and exams, final results should always be reviewed by human educators."
        )
    elif industry == "新聞 (Journalism)":
        st.markdown(
            "### 📰 新聞 (Journalism) - 官方文件第 33-34 頁明文要求：\n"
            "- **查證與審核**：減少模型幻覺等問題導致的生成內容失實，建議生成內容包含內容來源。**生成內容必須經由事實查證和全文審核後才能用於公開報導**。\n"
            "- **嚴禁捏造事實**：不得使用生成式人工智能製作偏離事實、捏造事實的文字、圖像、語音和視像等內容並以各種形式混入新聞報導。"
            if is_zh else
            "### 📰 Journalism - Page 43 Official Requirements:\n"
            "- **Mandatory Fact-Checking**: Implement safeguards to minimise factual inaccuracies; content must undergo fact-checking and full editorial review before being published, including source attributions.\n"
            "- **Strict Prohibition of Fabrication**: Generative AI should not be used to create fabricated text, images, or audio-visual content that misrepresents facts or infiltrates news reports in any form."
        )
    elif industry == "旅遊 (Tourism)":
        st.markdown(
            "### 🧳 旅遊 (Tourism) - 官方文件第 34 頁明文要求：\n"
            "- **公平推薦**：在旅遊推薦、客房預訂或智慧客服等服務中，要確保對不同客源能做到公平和無歧視性推薦。\n"
            "- **平衡私隱與精準度**：定期審查生成內容是否存在不實或誤導性資料，嚴防過度搜集和不當使用旅客資訊。"
            if is_zh else
            "### 🧳 Tourism - Page 43 Official Requirements:\n"
            "- **Fair Recommendation**: Ensure fair and non-discriminatory treatment of different customer segments in travel recommendations, hotel bookings, or AI-powered customer service.\n"
            "- **Balance Privacy & Accuracy**: Regular reviews should be conducted to identify any false or misleading information; prevent excessive data collection and misuse."
        )
    elif industry == "零售 (Retail)":
        st.markdown(
            "### 🛍️ 零售 (Retail) - 官方文件第 34 頁明文要求：\n"
            "- **算法公正性**：用於產品推薦、動態定價或顧客服務時，須確保同一區域及客群得到合理且透明的算法結果，以維持市場公正性。\n"
            "- **配備人手支援**：建議在顧客對生成式人工智能產生困惑或疑慮時，**配備人手支援和即時回覆機制**，以保障顧客權益。"
            if is_zh else
            "### 🛍️ Retail - Page 43 Official Requirements:\n"
            "- **Algorithmic Fairness**: Ensure that algorithmic outcomes remain fair and transparent across different customer segments and geographic locations to maintain market fairness.\n"
            "- **Human Support Mechanism**: Human support and real-time response mechanisms should be available to address customer concerns or confusion to safeguard consumer rights."
        )
    elif industry == "物流 (Logistics)":
        st.markdown(
            "### 📦 物流 (Logistics) - 官方文件第 34 頁明文要求：\n"
            "- **降低偏誤風險**：在運具調度與智慧路線規劃中應使用可靠且最新的交通與地理資訊，降低偏誤風險。\n"
            "- **隱私控制與產業安全**：處理個人位址時必須採用適當的加密與存取控制方案。若採用自動化分揀，應定期檢視系統安全性與穩定性，避免碰撞或風險事件。"
            if is_zh else
            "### 📦 Logistics - Page 44 Official Requirements:\n"
            "- **Minimise Bias Risks**: Rely on reliable and up-to-date traffic and geographic data to minimise bias risks in transportation scheduling and intelligent route planning.\n"
            "- **Encryption & Industrial Safety**: Handling of personal addresses must incorporate appropriate encryption and access control measures; automated sorting sorting arms must undergo regular security and stability assessments."
        )
    elif industry == "工業 (Industry)":
        st.markdown(
            "### 🏗️ 工業 (Industry) - 官方文件第 34 頁明文要求：\n"
            "- **主管工程師覆核**：若引入預測保養或自動故障診斷功能，亦應確保生成式人工智能所生成結果**能經主管工程師或品控人員覆核**。\n"
            "- **防止商業秘密外洩**：密切關注系統在處理**機密配方、專利技術或其他具有商業機密的信息**時的保安措施，以防止技術外洩或專利侵權。"
            if is_zh else
            "### 🏗️ Industry - Page 44 Official Requirements:\n"
            "- **Engineering Review**: If predictive maintenance or automated fault diagnosis functions are introduced, AI-generated results must be reviewed by supervisory engineers or quality control personnel.\n"
            "- **Trade Secret Protection**: Strong security measures must be in place, particularly when handling confidential formulas/know-hows, or other trade secrets to prevent technology leaks or patent infringement."
        )

# ==========================
# 6. 分頁三：機構內部政策指引 (100% 對應官方文件第 25 頁明文列出的 14 項內部政策要求)
# ==========================
with tabs[2]:
    st.subheader("📌 依據指引第 25 頁明文：採用生成式人工智能服務的機構應制訂之內部政策或指引項目" if is_zh else "📌 Per Page 31: Mandatory Internal Policy Components")
    st.markdown("請根據企業目前已落實的實務控制措施進行勾選：" if is_zh else "Please check all implemented corporate policy controls:")
    
    policy_checks = [
        st.checkbox("1. 獲准使用的工具（包括公眾可用的及內部開發的生成式人工智能工具或應用程式）" if is_zh else "1. Permitted tools (publicly available and internally developed)"),
        st.checkbox("2. 獲准許的用途（例如：起草、總結資訊及/或生成文本、音頻及/或視像內容）" if is_zh else "2. Permissible use (e.g., drafting, summarising, content creation)"),
        st.checkbox("3. 政策適用性" if is_zh else "3. Policy applicability"),
        st.checkbox("4. 獲准輸入的資訊種類及數量" if is_zh else "4. Permissible types and amounts of input information"),
        st.checkbox("5. 輸出資訊的獲准許用途" if is_zh else "5. Permissible use of output information"),
        st.checkbox("6. 輸出資訊的獲准許儲存方式" if is_zh else "6. Permissible storage of output information"),
        st.checkbox("7. 遵從其他相關內部政策，以確保與機構的其他相關內部政策一致" if is_zh else "7. Compliance and alignment with other relevant internal policies"),
        st.checkbox("8. 訂明僱員不能為進行非法或有害的活動使用生成式人工智能工具" if is_zh else "8. Specify that employees shall not use tools for unlawful or harmful activities"),
        st.checkbox("9. 強調僱員有責任擔當審查員，以確保生成的結果符合機構的道德價值觀及標準" if is_zh else "9. Emphasise employee responsibility as human reviewers for ethical/factual alignment"),
        st.checkbox("10. 獲准許裝置" if is_zh else "10. Permitted devices"),
        st.checkbox("11. 獲准許使用者" if is_zh else "11. Permitted users"),
        st.checkbox("12. 穩健的用戶憑證（例如：使用不重複的高強度密碼及多重認證）" if is_zh else "12. Robust user credentials (strong, unique passwords and MFA)"),
        st.checkbox("13. 保安設定（例如：關閉對話存檔或資料分享功能）" if is_zh else "13. Security settings (e.g., disabling chat history or data sharing functions)"),
        st.checkbox("14. 人工智能事故及資料外洩事故應變（例如：報告資料外洩、未獲授權輸入資料或違法輸出結果）" if is_zh else "14. Response to AI incident and data breach incident (unauthorised input/unlawful output)")
    ]
    
    # 計算完備度得分
    passed_counts = sum(policy_checks)
    total_counts = len(policy_checks)
    readiness_score = (passed_counts / total_counts) * 100
    
    st.markdown("---")
    st.markdown(f"### 📊 機構內部政策指引完備度 (Policy Readiness): **{readiness_score:.0f}%** ({passed_counts}/{total_counts})")
    st.progress(readiness_score / 100)
    
    if readiness_score == 100:
        st.success("✅ **符合標準 (Compliant)**：內部指引已 100% 完整覆蓋特區政府數字政策辦公室規定的 14 項法定要求。" if is_zh else "✅ **Compliant**: Internal guidelines 100% cover all 14 DPO-required components.")
    else:
        st.error("🚨 **存在合規缺口 (Compliance Gaps Detected)**：企業內部政策尚未完整，請根據上方未勾選項目儘速修訂員工守則，以防範影子 AI 與資料外洩風險！" if is_zh else "🚨 **Compliance Gaps Detected**: Policy is incomplete. Please remediate missing components immediately.")
