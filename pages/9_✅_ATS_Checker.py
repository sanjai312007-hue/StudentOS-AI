import streamlit as st
import time
from components.styles import apply_custom_styles
from components.sidebar import render_sidebar
from components.navbar import render_navbar
from data.mock_data import ATS_SCORE_DATA

st.set_page_config(
    page_title="ATS Resume Checker | StudentOS AI",
    page_icon="✅",
    layout="wide"
)

apply_custom_styles()

if "authenticated" not in st.session_state or not st.session_state.authenticated:
    st.warning("🔒 Please authenticate first on the homepage.")
    st.stop()

# Initialize state
if "analyzed_resume" not in st.session_state:
    st.session_state.analyzed_resume = False

# ── Floating Navbar ──────────────────────────────────────────────
render_navbar()

# ─── Layout: Sidebar (col_nav) & Main Content (col_content) ─────
col_nav, col_content = st.columns([1.1, 4])

with col_nav:
    render_sidebar(active_page="ATS Checker")

with col_content:
    # Header Section
    st.markdown("""
<div style="margin-top: 10px; margin-bottom: 25px;">
<h1>✅ ATS Resume <span class="gradient-text">Checker</span></h1>
<p style="color: #64748B; font-size: 1rem; margin-top: 0;">Analyze your resume formatting, keywords density, and grammar constraints against placement profiles</p>
</div>
""", unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1.2])

    with col1:
        st.markdown("### 📥 Ingest Placement Resume")
        
        # Drag & Drop Resume File Uploader
        resume_file = st.file_uploader("Upload Resume Document (PDF / DOCX)", type=["pdf", "docx"])
        
        # Target Job Role dropdown
        target_role = st.selectbox("Target Career Domain", ["AI / ML Engineer", "Python Developer", "Full Stack Developer", "Data Analyst"])
        
        st.markdown("<div style='margin-top: 15px;'></div>", unsafe_allow_html=True)
        if st.button("Perform ATS Diagnostics"):
            if resume_file:
                with st.spinner("Analyzing resume semantics & parsing keywords..."):
                    time.sleep(1.8)
                    st.session_state.analyzed_resume = True
                    st.success("ATS Analysis Complete!")
                    st.rerun()
            else:
                st.error("Please upload a resume file first.")

        # Always show demo option to explore features
        if not st.session_state.analyzed_resume:
            st.markdown("---")
            if st.button("Use Sample Resume (Demo)"):
                with st.spinner("Analyzing dummy student profile..."):
                    time.sleep(1)
                    st.session_state.analyzed_resume = True
                    st.rerun()

    with col2:
        st.markdown("### 📊 ATS Audit Summary")
        
        if st.session_state.analyzed_resume:
            score = ATS_SCORE_DATA["overall_score"]
            gauge_color = "#10b981" if score >= 80 else ("#f59e0b" if score >= 70 else "#ef4444")
            
            st.markdown(f"""
<div class="glass-card" style="text-align: center; padding: 30px 20px;">
<div class="stat-label">ATS MATCH RATE</div>
<div class="stat-val" style="font-size: 3.5rem; margin: 10px 0; color: {gauge_color};">{score}%</div>
<div style="font-size: 0.95rem; color: #94a3b8;">Job Profile Target: <b>{target_role}</b></div>
</div>
""", unsafe_allow_html=True)
            
            # Sub-score criteria grid
            sub_col1, sub_col2, sub_col3 = st.columns(3)
            with sub_col1:
                st.markdown(f"""
<div class="glass-card" style="padding: 12px; text-align: center; margin-bottom: 0;">
<div style="font-size: 0.75rem; color: #94a3b8;">FORMATTING</div>
<b style="font-size: 1.2rem; color: #10b981;">{ATS_SCORE_DATA['formatting']}%</b>
</div>
""", unsafe_allow_html=True)
            with sub_col2:
                st.markdown(f"""
<div class="glass-card" style="padding: 12px; text-align: center; margin-bottom: 0;">
<div style="font-size: 0.75rem; color: #94a3b8;">KEYWORDS</div>
<b style="font-size: 1.2rem; color: #f59e0b;">{ATS_SCORE_DATA['keywords']}%</b>
</div>
""", unsafe_allow_html=True)
            with sub_col3:
                st.markdown(f"""
<div class="glass-card" style="padding: 12px; text-align: center; margin-bottom: 0;">
<div style="font-size: 0.75rem; color: #94a3b8;">GRAMMAR</div>
<b style="font-size: 1.2rem; color: #10b981;">{ATS_SCORE_DATA['grammar']}%</b>
</div>
""", unsafe_allow_html=True)
                
            # Missing Keywords
            st.markdown("#### 🔍 Missing Critical Keywords")
            keywords_html = '<div style="display: flex; flex-wrap: wrap; gap: 8px; margin: 10px 0;">'
            for kw in ATS_SCORE_DATA["missing_keywords"]:
                keywords_html += f'<span class="badge" style="background: rgba(239, 68, 68, 0.12); color: #ef4444; border: 1px solid rgba(239, 68, 68, 0.25); padding: 6px 12px; font-size: 0.8rem;">+ {kw}</span>'
            keywords_html += '</div>'
            st.markdown(keywords_html, unsafe_allow_html=True)
            
            # Recommendations
            st.markdown("#### 💡 Structural Action Items")
            for sug in ATS_SCORE_DATA["suggestions"]:
                st.markdown(f"- {sug}")
                
            if st.button("Reset Scanner"):
                st.session_state.analyzed_resume = False
                st.rerun()
        else:
            st.info("Upload a placement resume or click 'Use Sample Resume' to run ATS matching diagnostics.")
