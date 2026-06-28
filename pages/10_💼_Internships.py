import streamlit as st
import time
from components.styles import apply_custom_styles
from components.sidebar import render_sidebar
from components.navbar import render_navbar
from data.mock_data import INTERNSHIP_RECOMMENDATIONS

st.set_page_config(
    page_title="Internships | StudentOS AI",
    page_icon="💼",
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
    render_sidebar(active_page="Placements")

with col_content:
    # Header Section
    st.markdown("""
<div style="margin-top: 10px; margin-bottom: 25px;">
<h1>💼 Internship & Course <span class="gradient-text">Recommendations</span></h1>
<p style="color: #64748B; font-size: 1rem; margin-top: 0;">AI matches your current skills, projects, and CGPA with active corporate internships and curated professional courses</p>
</div>
""", unsafe_allow_html=True)

    # Grid Layout
    filter_col, list_col = st.columns([1, 2.2])

    with filter_col:
        st.markdown("### 🔍 Career Match Filters")
        
        # Active skill list tags
        profile_skills = st.session_state.user_profile["skills"]
        st.markdown("**Your Current Skills:**")
        skills_html = '<div style="display: flex; flex-wrap: wrap; gap: 6px; margin-bottom: 15px;">'
        for sk in profile_skills:
            skills_html += f'<span class="badge" style="background: rgba(108, 99, 255, 0.15); color: #a78bfa; border: 1px solid rgba(108, 99, 255, 0.25);">{sk}</span>'
        skills_html += '</div>'
        st.markdown(skills_html, unsafe_allow_html=True)
        
        # Matching thresholds
        match_threshold = st.slider("Minimum Match Threshold (%)", min_value=50, max_value=100, value=75)
        location_pref = st.selectbox("Location Type", ["All Types", "Remote Only", "On-site Only"])
        
        st.markdown("---")
        st.markdown("#### Curated Courses & Certificates")
        st.markdown("""
<div class="glass-card" style="padding: 14px; margin-bottom: 10px;">
<span style="font-size: 0.75rem; color: #FFE66D; font-weight: 600; text-transform: uppercase;">RECOMMENDED COURSE</span>
<h4 style="margin: 4px 0 2px 0; color: #ffffff;">IBM AI Engineering</h4>
<span style="font-size: 0.8rem; color: #94a3b8;">Fills missing: Deep Learning, PyTorch</span>
</div>
<div class="glass-card" style="padding: 14px; margin-bottom: 10px;">
<span style="font-size: 0.75rem; color: #FFE66D; font-weight: 600; text-transform: uppercase;">RECOMMENDED COURSE</span>
<h4 style="margin: 4px 0 2px 0; color: #ffffff;">Docker Certified Associate</h4>
<span style="font-size: 0.8rem; color: #94a3b8;">Fills missing: Containerization, CI/CD</span>
</div>
""", unsafe_allow_html=True)

    with list_col:
        st.markdown("### 💼 Placement Recommendations")
        
        # Loop over recommended internships
        filtered_list = [i for i in INTERNSHIP_RECOMMENDATIONS if i["skills_match"] >= match_threshold]
        if location_pref == "Remote Only":
            filtered_list = [i for i in filtered_list if "remote" in i["location"].lower()]
        elif location_pref == "On-site Only":
            filtered_list = [i for i in filtered_list if "remote" not in i["location"].lower()]
            
        if filtered_list:
            for idx, intern in enumerate(filtered_list):
                match_color = "#10b981" if intern["skills_match"] >= 85 else "#f59e0b"
                
                st.markdown(f"""
<div class="glass-card" style="padding: 20px; margin-bottom: 15px;">
<div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 10px;">
<div>
<span style="font-size: 1.5rem; margin-right: 8px;">{intern['logo']}</span>
<b style="font-size: 1.2rem; color: #ffffff;">{intern['title']}</b>
<div style="font-size: 0.85rem; color: #94a3b8; margin-top: 4px;">{intern['company']} • {intern['location']}</div>
</div>
<div style="text-align: right;">
<span style="font-size: 1.15rem; font-weight: bold; color: {match_color};">{intern['skills_match']}% Match</span>
<div style="font-size: 0.8rem; color: #64748b; margin-top: 2px;">{intern['duration']} • {intern['stipend']}</div>
</div>
</div>

<div style="margin-top: 12px; margin-bottom: 15px;">
<div style="font-size: 0.82rem; color: #cbd5e1; margin-bottom: 6px; font-weight: 600;">Required Skills:</div>
{"".join(f'<span class="badge" style="background: rgba(255,255,255,0.05); color: #cbd5e1; border: 1px solid rgba(255,255,255,0.1);">{sk}</span>' for sk in intern['required_skills'])}
</div>
</div>
""", unsafe_allow_html=True)
                
                # Application simulation
                if st.button(f"Apply for {intern['title']} at {intern['company']}", key=f"apply_{idx}"):
                    with st.spinner("Submitting StudentOS verified academic transcript..."):
                        time.sleep(1)
                        st.success(f"Application Package Dispatched to {intern['company']} Talent Acquisition! 🚀")
        else:
            st.info("No internships match the selected criteria.")
