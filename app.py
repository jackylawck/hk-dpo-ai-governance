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

if 'lang' not in st.session_state: 
    st.session_state.lang = '繁體中文'
is_zh = st.session_state.lang == '繁體中文'

# ==========================================
# 2. 側邊欄 UI 設計
# ==========================================
with st.sidebar:
    st.markdown("### 🌐 UI Language / 介面語言" if is_zh else "### 🌐 UI Language")
    lang_choice = st.radio("Select Language", ['繁體中文', 'English'], index=0 if is_zh else 1, label_visibility="collapsed")
    if lang_choice != st.session_state.lang:
        st.session_state.lang = lang_choice
        st.rerun()
    
    st.markdown("---")
    st.markdown("### 🏛️ 官方指引核對基準" if is_zh else "### 🏛️ Official Baseline")
    st.caption("依據香港數字政策辦公室 (DPO) 《香港生成式人工智能技術及應用指引》V1.1 (2025年12月) 編碼。" if is_zh else "Coded based on the HK DPO Generative AI Guideline V1.1 (Dec 2025).")

# ==========================================
# 3. 主畫面標題
# ==========================================
st.title("⚖️ 香港數字政策辦公室 (DPO) AI 合規工作區" if is_zh else "⚖️ HK DPO GenAI Compliance Workstation")

tabs = st.tabs([
    "💬 智能情境問答 (Scenario Q&A)" if is_zh else "💬 Scenario Q&A",
    "📊 風險與行業管治 (Risk & Industry)" if is_zh else "📊 Risk & Industry",
    "📝 14項法定內部政策 (14-Point Checklist)" if is_zh else "📝 14-Point Checklist"
])

# ==========================================
# 4. 分頁一：智能情境問答 (Scenario Q&A)
# ==========================================
with tabs[0]:
    st.subheader("👨‍💼 AIGP 專家情境診斷引擎" if is_zh else "👨‍💼 AIGP Expert Scenario Diagnostic Engine")
    st.markdown("請描述您在企業中遇到的 AI 管治情境（例如：員工私自用個人設備註冊外部 AI...），系統將依據 DPO 官方指引為您進行風險拆解。" if is_zh else "Describe your enterprise AI governance scenario, and the system will provide a risk breakdown based on official DPO guidelines.")
    
    # 確保切換語言時，系統儲存的訊息語系正確
    if "messages_zh" not in st.session_state:
        st.session_state.messages_zh = [{"role": "assistant", "content": "您好！我是您的 AIGP 企業合規助手。請問今天有什麼 AI 導入的場景或風險挑戰需要探討？"}]
    if "messages_en" not in st.session_state:
        st.session_state.messages_en = [{"role": "assistant", "content": "Hello! I am your AIGP compliance assistant. What AI deployment scenario or risk challenge would you like to discuss today?"}]

    # 依據當前語言選擇對應的數據庫
    current_messages = st.session_state.messages_zh if is_zh else st.session_state.messages_en

    # 顯示歷史聊天紀錄
    for msg in current_messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # 處理使用者輸入
    input_placeholder = "請輸入企業情境... (如：市場部主管私自用 iPad 上傳客戶名單)" if is_zh else "Type your scenario here... (e.g., Marketing head used personal iPad to upload client data)"
    if prompt := st.chat_input(input_placeholder):
        # 儲存使用者的問題
        current_messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # 決策引擎 (中英文完全分流)
        with st.chat_message("assistant"):
            trigger_words = ["ipad", "私自", "影子", "客戶名單", "shadow", "unauthorized", "personal"]
            if any(w in prompt.lower() for w in trigger_words):
                if is_zh:
                    response = """🚨 **偵測到重大違規：「影子 AI (Shadow AI)」與「資料外洩 (Data Breach)」風險！**
                    
基於 DPO 官方指引的 14 項內部政策規範，您的情境違反了「獲准使用的工具」、「獲准許裝置」以及「獲准輸入的資訊種類」等核心要求。

**建議優先採取的兩個治理步驟（Domain IV 實務）：**
1. **立即啟動事故應變機制 (Incident Response)：** 依據第 14 項指引，評估客戶名單外洩的嚴重性，立即要求停止使用該免費工具，並視情況向私隱專員公署 (PCPD) 通報。
2. **紀律處分與建立白名單 (Enforcement & Whitelisting)：** 依據政策對違規行為進行處置，同時 HR 應協同 IT 部門，儘速提供已通過安全審查的內部企業版 AI 工具（第 1 項），消除員工繞過管控的動機。"""
                else:
                    response = """🚨 **Critical Breach Detected: "Shadow AI" and Potential "Data Breach"!**
                    
Based on the 14 mandatory internal policies from the DPO guideline, this scenario violates rules regarding "Permitted tools," "Permitted devices," and "Permissible types of input information."

**Top 2 Governance Actions Recommended (Domain IV Practice):**
1. **Trigger Incident Response (Policy Item 14):** Assess the severity of the PII leak and contain the exposure immediately. If necessary, report data breach to the PCPD.
2. **Enforcement & Whitelisting (Policy Item 1):** Enforce internal policy consequences, and work with IT to provide a secure, approved enterprise AI alternative to eliminate the motivation for Shadow AI."""
            else:
                if is_zh:
                    response = """💡 **收到您的情境描述。**
                    
這是一個典型的 AI 管治議題。從 AIGP 框架（Domain III & IV）出發，我們建議您切換至上方的 **「📝 14項法定內部政策」** 標籤頁，逐一檢核您的企業是否已經明確定義了相關管控機制。

*(提示：您可以試著輸入類似「市場部主管私自用 iPad 上傳客戶名單給免費 AI」的情境來測試系統。)*"""
                else:
                    response = """💡 **Scenario Logged.**
                    
From an AIGP governance perspective (Domains III & IV), we recommend navigating to the **"📝 14-Point Checklist"** tab above to verify if your organisation has clearly defined internal controls.

*(Hint: Try typing a scenario like "Marketing head used a personal iPad to upload client data to a free AI" to test the diagnostic engine.)*"""
            
            st.markdown(response)
            current_messages.append({"role": "assistant", "content": response})

# ==========================================
# 5. 分頁二：風險與行業管治
# ==========================================
with tabs[1]:
    st.subheader("第一步：風險分類系統 (Risk Classification System)" if is_zh else "Step 1: Risk Classification System")
    st.info("📌 依據指引第九至十頁：高風險系統必須進行合規性評估；有限風險系統須提供用戶選擇退出的機制。" if is_zh else "📌 Per Page 11: High Risk systems require conformity assessments; Limited Risk requires opt-out mechanisms.")
    
    st.markdown("---")
    st.subheader("第二步：特定行業應用原則 (Industry-Oriented Principles)" if is_zh else "Step 2: Industry-Oriented Principles")
    industry = st.selectbox(
        "選擇您的企業所屬行業 (Select Industry Vertical):",
        ["金融 (Finance)", "醫療 (Healthcare)", "法律 (Legal)", "教育 (Education)", "新聞 (Journalism)", "旅遊 (Tourism)", "零售 (Retail)", "物流 (Logistics)", "工業 (Industry)"]
    )
    if "金融" in industry:
         st.markdown("- **公平性與反操縱**：限制人工干預推薦權重。\n- **強制的退出與人為介入權**：必須提供退出 (Opt-out) 選項。" if is_zh else "- **Fairness**: Restrict manual weight tampering.\n- **Mandatory Opt-out**: Provide clear options to opt out.")
    else:
         st.markdown("請參考官方指引對應章節進行特定行業的道德審核。" if is_zh else "Please refer to the official guidelines for specific ethical audits.")

# ==========================
# 6. 分頁三：14項法定內部政策 (自查表)
# ==========================
with tabs[2]:
    st.subheader("📌 採用生成式人工智能服務的機構應制訂之內部政策" if is_zh else "📌 Mandatory Internal Policy Components")
    st.markdown("請根據企業目前已落實的實務控制措施進行自查：(適合 HR/法務/IT 部門協同填寫)" if is_zh else "Self-audit checklist for HR/Legal/IT:")
    
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
    st.markdown(f"### 📊 機構內部政策指引完備度: **{readiness_score:.0f}%** ({passed_counts}/14)" if is_zh else f"### 📊 Policy Readiness Score: **{readiness_score:.0f}%** ({passed_counts}/14)")
    st.progress(readiness_score / 100)
