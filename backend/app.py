"""ACPIA — Agentic Child Protection Investigation Assistant (Streamlit UI)."""

import streamlit as st
import streamlit.components.v1 as components

from graph_viz import build_graph_html
from orchestrator import AGENT_STEPS, run_investigation

st.set_page_config(
    page_title="ACPIA — Investigation Assistant",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded",
)

CUSTOM_CSS = """
<style>
    .main-header {
        font-size: 2.2rem;
        font-weight: 700;
        color: #1a237e;
        margin-bottom: 0.2rem;
    }
    .sub-header {
        color: #546e7a;
        font-size: 1rem;
        margin-bottom: 1.5rem;
    }
    .metric-card {
        background: linear-gradient(135deg, #1a237e 0%, #283593 100%);
        padding: 1rem 1.2rem;
        border-radius: 10px;
        color: white;
        text-align: center;
    }
    .metric-card h3 {
        margin: 0;
        font-size: 1.6rem;
    }
    .metric-card p {
        margin: 0;
        opacity: 0.85;
        font-size: 0.85rem;
    }
    .severity-critical { color: #d32f2f; font-weight: 600; }
    .severity-high { color: #f57c00; font-weight: 600; }
    .severity-medium { color: #fbc02d; font-weight: 600; }
    .severity-low { color: #388e3c; font-weight: 600; }
    div[data-testid="stExpander"] {
        border: 1px solid #e0e0e0;
        border-radius: 8px;
    }
</style>
"""
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# ── Sidebar ──────────────────────────────────────────────────────────────────
with st.sidebar:
    st.image("https://img.icons8.com/fluency/96/shield.png", width=64)
    st.title("🛡 ACPIA\nAgentic Child Protection Investigation Assistant\nAI-Powered Digital Evidence Investigation Platform")
    st.caption("Hackathon MVP · Sample outputs only")
    st.divider()
    st.markdown("**Pipeline**")
    for _, name, desc in AGENT_STEPS:
        st.markdown(f"**{name}**  \n{desc}")
    st.divider()
    st.info("System Status\n🟢 Gemini Connected\n🟢 AI Agents Active\n🟢 Knowledge Graph Generated\n🟢 Timeline Reconstructed")

# ── Title ──────────────────────────────────────────────────────────────────────
st.markdown('<p class="main-header">🛡️ Agentic Child Protection Investigation Assistant</p>', unsafe_allow_html=True)
st.markdown(
    '<p class="sub-header">Upload a chat export to run the multi-agent analysis pipeline</p>',
    unsafe_allow_html=True,
)

# ── File Upload & Analyze ─────────────────────────────────────────────────────
upload_col, action_col = st.columns([3, 1])

with upload_col:
    uploaded_file = st.file_uploader(
        "Upload chat export (.txt)",
        type=["txt"],
        help="Supports WhatsApp-style chat exports",
    )

with action_col:
    st.write("")
    st.write("")
    analyze_clicked = st.button("🔍 Analyze", type="primary", use_container_width=True)

if "results" not in st.session_state:
    st.session_state.results = None
if "agent_status" not in st.session_state:
    st.session_state.agent_status = {step[0]: "pending" for step in AGENT_STEPS}

# ── Run Pipeline ───────────────────────────────────────────────────────────────
if analyze_clicked:
    if not uploaded_file:
        st.warning("Please upload a chat file before analyzing.")
    else:
        chat_text = uploaded_file.read().decode("utf-8", errors="replace")
        st.session_state.results = None
        st.session_state.agent_status = {step[0]: "pending" for step in AGENT_STEPS}

        progress_bar = st.progress(0, text="Starting investigation pipeline…")
        agent_progress_container = st.container()

        with agent_progress_container:
            st.subheader("Agent Progress")
            expanders = {}
            for step_id, name, desc in AGENT_STEPS:
                expanders[step_id] = st.expander(f"⏳ {name} — {desc}", expanded=False)

        completed = 0
        for update in run_investigation(chat_text):
            if update.get("status") == "done":
                st.session_state.results = update
                continue

            step_id = update["step_id"]
            if update["status"] == "running":
                st.session_state.agent_status[step_id] = "running"
                with expanders[step_id]:
                    st.info(f"Running {update['name']}…")

            elif update["status"] == "complete":
                st.session_state.agent_status[step_id] = "complete"
                completed += 1
                progress_bar.progress(
                    completed / len(AGENT_STEPS),
                    text=f"Completed {completed}/{len(AGENT_STEPS)} agents",
                )
                with expanders[step_id]:
                    st.success(f"✅ {update['name']} complete")
                    result = update.get("result", {})
                    if step_id == "text_agent":
                        c1, c2, c3 = st.columns(3)
                        c1.metric("Messages", result.get("message_count", 0))
                        c2.metric("Participants", len(result.get("participants", [])))
                        c3.metric("Date Range", result.get("date_range", "N/A"))
                    elif step_id == "entity_agent":
                        st.write(f"**People:** {len(result.get('people', []))} · "
                                 f"**Locations:** {len(result.get('locations', []))} · "
                                 f"**Flags:** {len(result.get('behavioral_flags', []))}")
                    elif step_id == "correlation_agent":
                        st.write(f"**Nodes:** {len(result.get('nodes', []))} · "
                                 f"**Edges:** {len(result.get('edges', []))} · "
                                 f"**Patterns:** {len(result.get('patterns', []))}")
                    elif step_id == "timeline_agent":
                        st.write(f"**Events reconstructed:** {len(result)}")
                    elif step_id == "summary_agent":
                        st.write(f"**Risk level:** {result.get('risk_level', 'N/A')}")

        progress_bar.progress(1.0, text="Analysis complete")
        st.balloons()

# ── Results Sections ───────────────────────────────────────────────────────────
results = st.session_state.results

if results:
    st.divider()

    # Metrics row
    parsed = results.get("parsed", {})
    entities = results.get("entities", {})
    m1, m2, m3, m4 = st.columns(4)
    with m1:
        st.markdown(
            f'<div class="metric-card"><h3>{parsed.get("message_count", 0)}</h3>'
            f'<p>Messages Parsed</p></div>',
            unsafe_allow_html=True,
        )
    with m2:
        st.markdown(
            f'<div class="metric-card"><h3>{len(entities.get("people", []))}</h3>'
            f'<p>People Identified</p></div>',
            unsafe_allow_html=True,
        )
    with m3:
        st.markdown(
            f'<div class="metric-card"><h3>{len(results.get("timeline", []))}</h3>'
            f'<p>Timeline Events</p></div>',
            unsafe_allow_html=True,
        )
    with m4:
        risk = results.get("summary", {}).get("risk_level", "—")
        st.markdown(
            f'<div class="metric-card"><h3>{risk}</h3>'
            f'<p>Risk Level</p></div>',
            unsafe_allow_html=True,
        )

    st.write("")

    # Two-column layout for entities + graph
    left_col, right_col = st.columns([1, 1])

    with left_col:
        st.subheader("📋 Extracted Entities")
        with st.expander("People", expanded=True):
            for person in entities.get("people", []):
                st.markdown(f"**{person['name']}** — {person['role']} ({person['mentions']} mentions)")

        with st.expander("Locations"):
            for loc in entities.get("locations", []):
                st.markdown(f"**{loc['name']}** — {loc['context']}")

        with st.expander("Platforms & Handles"):
            for platform in entities.get("platforms", []):
                st.markdown(f"**{platform['name']}** — {platform['context']}")
            for handle in entities.get("handles", []):
                st.markdown(f"Handle: `{handle['value']}` on {handle['platform']} (shared by {handle['shared_by']})")

        with st.expander("Behavioral Flags"):
            for flag in entities.get("behavioral_flags", []):
                st.markdown(f"🚩 {flag}")

    with right_col:
        st.subheader("🕸️ Knowledge Graph")
        correlations = results.get("correlations", {})
        graph_html = build_graph_html(correlations)
        components.html(graph_html, height=450, scrolling=True)

        with st.expander("Detected Patterns"):
            for pattern in correlations.get("patterns", []):
                sev = pattern.get("severity", "Medium").lower()
                st.markdown(
                    f'<span class="severity-{sev}">[{pattern["severity"]}]</span> '
                    f"**{pattern['title']}** — {pattern['detail']}",
                    unsafe_allow_html=True,
                )

    st.divider()

    # Timeline
    st.subheader("📅 Timeline")
    timeline = results.get("timeline", [])
    for event in timeline:
        sev = event.get("severity", "Medium").lower()
        with st.expander(
            f"{event['date']} {event['time']} — {event['event'][:60]}…"
            if len(event["event"]) > 60
            else f"{event['date']} {event['time']} — {event['event']}",
            expanded=False,
        ):
            st.markdown(f"**Actor:** {event['actor']}")
            st.markdown(f"**Event:** {event['event']}")
            st.markdown(
                f'**Severity:** <span class="severity-{sev}">{event["severity"]}</span>',
                unsafe_allow_html=True,
            )

    st.divider()

    # Investigation Summary
    st.subheader("📝 Investigation Summary")
    summary = results.get("summary", {})
    sev = summary.get("risk_level", "Unknown").lower()

    sum_col1, sum_col2 = st.columns([2, 1])
    with sum_col1:
        risk_label = summary.get("risk_level", "N/A")
        if sev == "high" or sev == "critical":
            st.error(f"Risk Level: {risk_label}")
        elif sev == "medium":
            st.warning(f"Risk Level: {risk_label}")
        else:
            st.success(f"Risk Level: {risk_label}")
        st.info(summary.get("summary", ""))

    with sum_col2:
        st.markdown("**Key Findings**")
        for finding in summary.get("key_findings", []):
            st.markdown(f"• {finding}")

    with st.expander("Recommended Actions"):
        for action in summary.get("recommended_actions", []):
            st.markdown(f"✅ {action}")

else:
    st.divider()
    st.markdown("#### Getting Started")
    st.markdown(
        "1. Upload a `.txt` chat export (try `sample_data/sample_chat.txt`)\n"
        "2. Click **Analyze** to run the agent pipeline\n"
        "3. Review entities, knowledge graph, timeline, and summary"
    )
