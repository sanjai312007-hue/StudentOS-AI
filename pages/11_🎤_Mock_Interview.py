import streamlit as st
import time
from components.styles import apply_custom_styles
from components.sidebar import render_sidebar
from components.navbar import render_navbar
from data.mock_data import MOCK_INTERVIEW_QUESTIONS, INTERVIEW_FEEDBACK_SAMPLE

st.set_page_config(
    page_title="Mock Interview | StudentOS AI",
    page_icon="🎤",
    layout="wide"
)

apply_custom_styles()

if "authenticated" not in st.session_state or not st.session_state.authenticated:
    st.warning("🔒 Please authenticate first on the homepage.")
    st.stop()

# Initialize session state for interviews
if "interview_active" not in st.session_state:
    st.session_state.interview_active = False
if "interview_role" not in st.session_state:
    st.session_state.interview_role = None
if "curr_q_index" not in st.session_state:
    st.session_state.curr_q_index = 0
if "interview_responses" not in st.session_state:
    st.session_state.interview_responses = {}
if "feedback_report" not in st.session_state:
    st.session_state.feedback_report = None

# ── Floating Navbar ──────────────────────────────────────────────
render_navbar()

# ─── Layout: Sidebar (col_nav) & Main Content (col_content) ─────
col_nav, col_content = st.columns([1.1, 4])

with col_nav:
    render_sidebar(active_page="Mock Interview")

with col_content:
    # Header Section
    st.markdown("""
<div style="margin-top: 10px; margin-bottom: 25px;">
<h1>🎤 AI Mock <span class="gradient-text">Interview</span></h1>
<p style="color: #64748B; font-size: 1rem; margin-top: 0;">Practice technical & behavioral questions, get evaluated on grammar, confidence, and context accuracy</p>
</div>
""", unsafe_allow_html=True)

    if not st.session_state.interview_active and not st.session_state.feedback_report:
        # ─── Configuration Panel ──────────────────────────────────────────
        st.markdown("### Start Placement Simulation")
        
        col1, col2 = st.columns([1, 1])
        
        with col1:
            target_role = st.selectbox("Select Interview Profile", list(MOCK_INTERVIEW_QUESTIONS.keys()))
            duration_mode = st.radio("Interview Length", ["Short (4 Questions)", "Full Length (8 Questions)"])
        with col2:
            eval_focus = st.multiselect("Active Rubrics", ["Technical Depth", "Communication Flow", "Vocabulary & Grammar", "Confidence & Tone"], default=["Technical Depth", "Communication Flow", "Vocabulary & Grammar"])
            voice_mode = st.checkbox("Enable Voice Mode (Beta Speech-to-text)", value=False)
            
        st.markdown("<div style='margin-top: 20px;'></div>", unsafe_allow_html=True)
        if st.button("Initiate Interview Room"):
            with st.spinner("Compiling technical assessment questions..."):
                time.sleep(1.2)
                st.session_state.interview_active = True
                st.session_state.interview_role = target_role
                st.session_state.curr_q_index = 0
                st.session_state.interview_responses = {}
                st.session_state.feedback_report = None
                st.rerun()

    elif st.session_state.interview_active:
        # ─── Active Interview Session ─────────────────────────────────────
        role = st.session_state.interview_role
        questions = MOCK_INTERVIEW_QUESTIONS[role]
        idx = st.session_state.curr_q_index
        q = questions[idx]
        
        # Progress Indicators
        progress = (idx + 1) / len(questions)
        st.progress(progress)
        st.markdown(f"**Question {idx + 1} of {len(questions)}** • Topic: `{q['category']}` • Time Limit: `{q['time_limit']}s`")
        
        st.markdown(f"""
<div class="glass-card" style="margin-top: 15px; border-left: 5px solid #6C63FF; padding: 24px; min-height: 120px;">
<span style="font-size: 0.75rem; color: #a78bfa; font-weight: 700; text-transform: uppercase;">INTERVIEWER QUESTION</span>
<h3 style="color: #ffffff; margin: 8px 0 0 0; line-height: 1.4;">"{q['question']}"</h3>
</div>
""", unsafe_allow_html=True)
        
        # Response Input (Text Area mimicking speech-to-text input)
        user_response = st.text_area("Your Response", height=150, placeholder="Speak or type your explanation here...")
        
        st.markdown("<div style='margin-top: 15px;'></div>", unsafe_allow_html=True)
        
        col_n1, col_n2, col_n3 = st.columns([1, 1, 1])
        
        with col_n1:
            if idx > 0:
                if st.button("Back"):
                    st.session_state.curr_q_index -= 1
                    st.rerun()
                    
        with col_n3:
            if idx < len(questions) - 1:
                if st.button("Submit & Next Question", type="primary"):
                    st.session_state.interview_responses[idx] = user_response
                    st.session_state.curr_q_index += 1
                    st.rerun()
            else:
                if st.button("Finish Interview", type="primary"):
                    st.session_state.interview_responses[idx] = user_response
                    with st.spinner("Analyzing answers, computing diagnostic metrics..."):
                        time.sleep(2)
                        st.session_state.feedback_report = INTERVIEW_FEEDBACK_SAMPLE.copy()
                        st.session_state.interview_active = False
                        st.rerun()

    elif st.session_state.feedback_report:
        # ─── Report Card Screen ───────────────────────────────────────────
        report = st.session_state.feedback_report
        
        st.markdown("### AI Performance Report Card")
        
        col1, col2 = st.columns([1, 1.8])
        
        with col1:
            st.markdown(f"""
<div class="glass-card" style="text-align: center; padding: 30px 20px; margin-bottom: 20px;">
<div class="stat-label">OVERALL EVALUATION SCORE</div>
<div class="stat-val" style="font-size: 4rem; margin: 15px 0;">{report['overall_score']}%</div>
<div style="font-size: 0.9rem; color: #10b981; font-weight: bold;">Passed Standard Criteria</div>
</div>
""", unsafe_allow_html=True)
            
            st.markdown("#### Performance Breakdown")
            st.markdown(f"""
<div class="glass-card" style="padding: 16px;">
<div style="margin-bottom: 10px;">
<div style="display: flex; justify-content: space-between; font-size: 0.85rem; color: #94a3b8; margin-bottom: 4px;">
<span>Communication</span>
<span>{report['communication']}%</span>
</div>
<div style="background: rgba(255,255,255,0.05); height: 6px; border-radius: 3px; overflow: hidden;">
<div style="background: #6C63FF; width: {report['communication']}%; height: 100%;"></div>
</div>
</div>
<div style="margin-bottom: 10px;">
<div style="display: flex; justify-content: space-between; font-size: 0.85rem; color: #94a3b8; margin-bottom: 4px;">
<span>Technical Accuracy</span>
<span>{report['technical_accuracy']}%</span>
</div>
<div style="background: rgba(255,255,255,0.05); height: 6px; border-radius: 3px; overflow: hidden;">
<div style="background: #4ECDC4; width: {report['technical_accuracy']}%; height: 100%;"></div>
</div>
</div>
<div>
<div style="display: flex; justify-content: space-between; font-size: 0.85rem; color: #94a3b8; margin-bottom: 4px;">
<span>Confidence Rate</span>
<span>{report['confidence']}%</span>
</div>
<div style="background: rgba(255,255,255,0.05); height: 6px; border-radius: 3px; overflow: hidden;">
<div style="background: #FFE66D; width: {report['confidence']}%; height: 100%;"></div>
</div>
</div>
</div>
""", unsafe_allow_html=True)
            
            if st.button("Start New Session", type="primary"):
                st.session_state.feedback_report = None
                st.session_state.interview_active = False
                st.rerun()

        with col2:
            st.markdown("#### Diagnostic Rubric Analysis")
            for category, cat_data in report["categories"].items():
                st.markdown(f"""
<div class="glass-card" style="padding: 16px; margin-bottom: 12px;">
<div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
<b style="color: #ffffff; font-size: 1.05rem;">{category} Module</b>
<span class="badge" style="background: rgba(108, 99, 255, 0.12); color: #a78bfa; border: 1px solid rgba(108, 99, 255, 0.25);">{cat_data['score']}%</span>
</div>
<p style="font-size: 0.88rem; color: #cbd5e1; margin-top: 8px; line-height: 1.4;">{cat_data['feedback']}</p>
</div>
""", unsafe_allow_html=True)
