import streamlit as st
from orchestrator import run_debate_agent

st.set_page_config(page_title="Debate Agent", page_icon="⚖️", layout="wide")

st.markdown("""
<style>
    .stTabs [data-baseweb="tab"] { font-size: 15px; padding: 8px 20px; }
    .agent-badge {
        display: inline-block;
        background: #f0f2f6;
        border-radius: 20px;
        padding: 4px 12px;
        font-size: 13px;
        margin: 2px;
        color: #333;
    }
</style>
""", unsafe_allow_html=True)

st.title("⚖️ Debate Research Agent")
st.caption("Powered by 6 AI agents + Gemini + Tavily live search")

st.markdown("**Agents in pipeline:**")
for label in ["A1 Pro Researcher", "A2 Con Researcher", "A3 Source Validator",
              "A4 Brief Writer", "A5 Rebuttal Agent", "A6 Judge"]:
    st.markdown(f'<span class="agent-badge">{label}</span>', unsafe_allow_html=True)

st.divider()

topic = st.text_input("Enter debate topic or motion",
                      placeholder="e.g. Artificial intelligence should be regulated by governments")

col1, col2 = st.columns([1, 4])
with col1:
    run = st.button("Run Agent ▶", type="primary", use_container_width=True)

if run:
    if not topic.strip():
        st.warning("Please enter a debate topic.")
    else:
        status = st.empty()
        progress = st.progress(0)
        steps = [0]

        def update_status(msg):
            step_map = {
                "A1": 1, "A2": 2, "A3": 3, "A4": 4, "A5": 5, "A6": 6
            }
            for k, v in step_map.items():
                if k in msg:
                    progress.progress(v / 6)
            status.info(f"⏳ {msg}")

        result = run_debate_agent(topic, status_callback=update_status)

        status.success("✅ All 6 agents completed!")
        progress.progress(1.0)

        st.subheader(f"Results — {topic}")
        tab1, tab2, tab3, tab4 = st.tabs(["📄 Brief", "⚔️ Rebuttals", "🔍 Sources", "⚖️ Judge"])

        with tab1:
            col_pro, col_con = st.columns(2)
            with col_pro:
                st.markdown("### ✅ Pro arguments")
                st.write(result["pro"])
            with col_con:
                st.markdown("### ❌ Con arguments")
                st.write(result["con"])
            st.divider()
            st.markdown("### 📄 Full debate brief")
            st.write(result["brief"])

        with tab2:
            st.markdown("### ⚔️ Rebuttals")
            st.write(result["rebuttals"])

        with tab3:
            st.markdown("### 🔍 Source validation report")
            st.write(result["sources"])

        with tab4:
            st.markdown("### ⚖️ Judge's evaluation")
            st.info(result["judgment"])