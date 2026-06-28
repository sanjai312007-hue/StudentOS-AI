import streamlit as st
import time
from components.styles import apply_custom_styles
from components.sidebar import render_sidebar
from components.navbar import render_navbar
from data.mock_data import STUDY_PLAN, STUDENT_PROFILE

st.set_page_config(
    page_title="Study Planner | StudentOS AI",
    page_icon="📅",
    layout="wide"
)

apply_custom_styles()

if "authenticated" not in st.session_state or not st.session_state.authenticated:
    st.warning("🔒 Please authenticate first on the homepage.")
    st.stop()

# Initialize active planner values
if "planner_plan" not in st.session_state:
    st.session_state.planner_plan = STUDY_PLAN.copy()
if "active_day" not in st.session_state:
    st.session_state.active_day = "Monday"
if "exams_list" not in st.session_state:
    st.session_state.exams_list = [
        {"subject": "Operating Systems", "date": "2026-07-02", "days_left": 5},
        {"subject": "DBMS", "date": "2026-07-06", "days_left": 9}
    ]

# ── Floating Navbar ──────────────────────────────────────────────
render_navbar()

# ─── Layout: Sidebar (col_nav) & Main Content (col_content) ─────
col_nav, col_content = st.columns([1.1, 4])

with col_nav:
    render_sidebar(active_page="Study Planner")

with col_content:
    # Header Section
    st.markdown("""
<div style="margin-top: 10px; margin-bottom: 25px;">
<h1>📅 Smart Study <span class="gradient-text">Planner</span></h1>
<p style="color: #64748B; font-size: 1rem; margin-top: 0;">AI-driven study schedule optimization based on examination timelines, daily free slots, and weaker topics</p>
</div>
""", unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1.8])

    with col1:
        st.markdown("### ⚙️ Schedule Configuration")
        
        # Study Planner setup form
        with st.form("schedule_config_form"):
            daily_hours = st.slider("Target Daily Study (Hours)", min_value=1, max_value=8, value=3)
            weak_topics = st.multiselect("Prioritize Weak Topics", ["Deadlocks", "Normalization", "Algorithms", "Linear Regression", "Graphs"], default=["Deadlocks", "Normalization"])
            exam_approaching = st.checkbox("Optimize for Upcoming Exams", value=True)
            
            st.markdown("<div style='margin-top: 15px;'></div>", unsafe_allow_html=True)
            submit = st.form_submit_button("Optimize Schedule (AI)")
            
            if submit:
                with st.spinner("Re-allocating time parameters..."):
                    time.sleep(1.2)
                    # Mock schedule readjustment: increase OS hours because of approaching exam
                    new_plan = st.session_state.planner_plan.copy()
                    if exam_approaching:
                        new_plan["Monday"] = [
                            {"subject": "Operating Systems (Exam Prep)", "duration": f"{daily_hours-1} hrs", "time": "09:00 - 11:00", "type": "High Priority Revision", "color": "#4ECDC4", "priority": "high"},
                            {"subject": "DBMS Practice", "duration": "1 hr", "time": "14:00 - 15:00", "type": "Normal Revision", "color": "#FF6B6B", "priority": "medium"}
                        ]
                    st.session_state.planner_plan = new_plan
                    st.toast("Schedule optimized! Time allocated towards approaching exam domains.")
                    st.rerun()

        # Approaches/Milestones list
        st.markdown("#### Upcoming Academic Milestones")
        for exam in st.session_state.exams_list:
            st.markdown(f"""
<div class="glass-card" style="padding: 14px; margin-bottom: 10px; border-left: 4px solid #ef4444;">
<h4 style="margin: 0; color: #ffffff;">{exam['subject']}</h4>
<div style="display: flex; justify-content: space-between; font-size: 0.8rem; color: #94a3b8; margin-top: 6px;">
<span>Date: {exam['date']}</span>
<span style="color: #ff6b6b; font-weight: bold;">🚨 {exam['days_left']} Days Left</span>
</div>
</div>
""", unsafe_allow_html=True)

    with col2:
        st.markdown("### 📅 Weekly Calendar Schedule")
        
        # Multi-tab day selector
        days = list(st.session_state.planner_plan.keys())
        selected_day = st.radio("Select Day:", days, horizontal=True, label_visibility="collapsed")
        
        st.markdown(f"#### Allocated Blocks for {selected_day}")
        
        day_plan = st.session_state.planner_plan[selected_day]
        
        if day_plan:
            for idx, block in enumerate(day_plan):
                priority_tag = ""
                if block['priority'] == 'high':
                    priority_tag = '<span class="badge badge-high">High Priority</span>'
                elif block['priority'] == 'medium':
                    priority_tag = '<span class="badge badge-medium">Medium</span>'
                else:
                    priority_tag = '<span class="badge badge-low">Low</span>'
                    
                st.markdown(f"""
<div class="glass-card" style="border-left: 5px solid {block['color']}; padding: 18px; margin-bottom: 12px;">
<div style="display: flex; justify-content: space-between; align-items: center;">
<span style="font-weight: bold; color: #ffffff; font-size: 1.15rem;">{block['subject']}</span>
{priority_tag}
</div>
<div style="display: flex; gap: 20px; font-size: 0.85rem; color: #94a3b8; margin-top: 10px;">
<span>🕒 {block['time']} ({block['duration']})</span>
<span>📖 {block['type']}</span>
</div>
</div>
""", unsafe_allow_html=True)
        else:
            st.info("No study blocks planned for this day.")
