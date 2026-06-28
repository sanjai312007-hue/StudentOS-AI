import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from components.styles import apply_custom_styles
from components.sidebar import render_sidebar
from components.navbar import render_navbar
from data.mock_data import (
    WEEKLY_SCORES, SUBJECT_ACCURACY, STUDY_HOURS_DISTRIBUTION, MONTHLY_STUDY_HEATMAP
)

st.set_page_config(
    page_title="Performance Analytics | StudentOS AI",
    page_icon="📈",
    layout="wide"
)

apply_custom_styles()

if "authenticated" not in st.session_state or not st.session_state.authenticated:
    st.warning("🔒 Please authenticate first on the homepage.")
    st.stop()

# ── Floating Navbar ──────────────────────────────────────────────
render_navbar()

# ─── Layout: Sidebar (col_nav) & Main Content (col_content) ─────
col_nav, col_content = st.columns([1.1, 4])

with col_nav:
    render_sidebar(active_page="Analytics")

with col_content:
    # Header Section
    st.markdown("""
<div style="margin-top: 10px; margin-bottom: 25px;">
<h1>📊 Performance <span class="gradient-text">Analytics</span></h1>
<p style="color: #64748B; font-size: 1rem; margin-top: 0;">Comprehensive charts, study analytics logs, accuracy metrics, and AI-detected weak-subject recommendations</p>
</div>
""", unsafe_allow_html=True)

    # Grid Layout for Analytics
    col1, col2 = st.columns([1, 1])

    with col1:
        st.markdown("### 📈 Weekly Learning Curves")
        
        # Format line chart using Plotly
        df_scores = pd.DataFrame({
            "Weeks": WEEKLY_SCORES["weeks"] * 5,
            "Score": WEEKLY_SCORES["Python"] + WEEKLY_SCORES["DBMS"] + WEEKLY_SCORES["OS"] + WEEKLY_SCORES["ML"] + WEEKLY_SCORES["DSA"],
            "Subject": ["Python"]*8 + ["DBMS"]*8 + ["Operating Systems"]*8 + ["Machine Learning"]*8 + ["DSA"]*8
        })
        
        fig_line = px.line(
            df_scores, x="Weeks", y="Score", color="Subject",
            markers=True, template="plotly_dark",
            color_discrete_sequence=["#6C63FF", "#FF6B6B", "#4ECDC4", "#FFE66D", "#A78BFA"]
        )
        fig_line.update_layout(
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            margin=dict(l=0, r=0, t=10, b=0)
        )
        st.plotly_chart(fig_line, use_container_width=True)

    with col2:
        st.markdown("### 🎯 Accuracy per Subject")
        
        # Format bar chart using Plotly
        df_acc = pd.DataFrame({
            "Subject": SUBJECT_ACCURACY["subjects"],
            "Accuracy (%)": SUBJECT_ACCURACY["accuracy"]
        })
        
        fig_bar = px.bar(
            df_acc, x="Subject", y="Accuracy (%)", color="Subject",
            template="plotly_dark",
            color_discrete_sequence=["#6C63FF", "#FF6B6B", "#4ECDC4", "#FFE66D", "#A78BFA"]
        )
        fig_bar.update_layout(
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            margin=dict(l=0, r=0, t=10, b=0),
            showlegend=False
        )
        st.plotly_chart(fig_bar, use_container_width=True)

    col3, col4 = st.columns([1, 1.1])

    with col3:
        st.markdown("### ⏱️ Time Distribution")
        
        # Format pie chart using Plotly
        fig_pie = px.pie(
            names=STUDY_HOURS_DISTRIBUTION["subjects"],
            values=STUDY_HOURS_DISTRIBUTION["hours"],
            template="plotly_dark",
            color_discrete_sequence=STUDY_HOURS_DISTRIBUTION["colors"]
        )
        fig_pie.update_layout(
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            margin=dict(l=0, r=0, t=10, b=0)
        )
        st.plotly_chart(fig_pie, use_container_width=True)

    with col4:
        st.markdown("### 🧠 AI-Detected Weak Subjects & Improvement Actions")
        
        # Render weak subject cards with dynamic remedies
        st.markdown("""
<div class="glass-card" style="border-left: 5px solid #ff4757; padding: 16px; margin-bottom: 12px;">
<div style="display: flex; justify-content: space-between; align-items: center;">
<b style="color: #ffffff; font-size: 1.05rem;">Operating Systems (Score: 50%)</b>
<span class="badge" style="background: rgba(239, 68, 68, 0.15); color: #ef4444; border: 1px solid rgba(239, 68, 68, 0.3);">Weak</span>
</div>
<p style="font-size: 0.85rem; color: #94a3b8; margin: 8px 0;">Identified weak topic: <b>Deadlock Condition Details</b></p>
<div style="background: rgba(255,255,255,0.03); padding: 10px; border-radius: 6px; font-size: 0.8rem; color: #cbd5e1;">
💡 <b>Action Item:</b> Launch AI Tutor topic 'Deadlock' & run 10 sample MCQ problems inside Quiz module.
</div>
</div>

<div class="glass-card" style="border-left: 5px solid #2ed573; padding: 16px; margin-bottom: 12px;">
<div style="display: flex; justify-content: space-between; align-items: center;">
<b style="color: #ffffff; font-size: 1.05rem;">Machine Learning (Score: 95%)</b>
<span class="badge" style="background: rgba(16, 185, 129, 0.15); color: #10b981; border: 1px solid rgba(16, 185, 129, 0.3);">Strong</span>
</div>
<p style="font-size: 0.85rem; color: #94a3b8; margin: 8px 0;">Identified strong topic: <b>Linear Regression & KNN</b></p>
<div style="background: rgba(255,255,255,0.03); padding: 10px; border-radius: 6px; font-size: 0.8rem; color: #cbd5e1;">
💡 <b>Action Item:</b> Keep revising. Try a mock interview session for "AI Engineer" role.
</div>
</div>
""", unsafe_allow_html=True)
