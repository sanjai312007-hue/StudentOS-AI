import streamlit as st
from components.styles import apply_custom_styles
from components.sidebar import render_sidebar
from components.navbar import render_navbar
from data.mock_data import RESUME_DATA

st.set_page_config(
    page_title="Resume Builder | StudentOS AI",
    page_icon="📄",
    layout="wide"
)

apply_custom_styles()

if "authenticated" not in st.session_state or not st.session_state.authenticated:
    st.warning("🔒 Please authenticate first on the homepage.")
    st.stop()

# Initialize resume active variables
if "resume_draft" not in st.session_state:
    st.session_state.resume_draft = RESUME_DATA.copy()

# ── Floating Navbar ──────────────────────────────────────────────
render_navbar()

# ─── Layout: Sidebar (col_nav) & Main Content (col_content) ─────
col_nav, col_content = st.columns([1.1, 4])

with col_nav:
    render_sidebar(active_page="Resume Builder")

with col_content:
    # Header Section
    st.markdown("""
<div style="margin-top: 10px; margin-bottom: 25px;">
<h1>📄 Professional <span class="gradient-text">Resume Builder</span></h1>
<p style="color: #64748B; font-size: 1rem; margin-top: 0;">Fill in your academic profile details and compile an elegant placement resume draft</p>
</div>
""", unsafe_allow_html=True)

    col1, col2 = st.columns([1.1, 1])

    with col1:
        st.markdown("### ✏️ Edit Profile Sections")
        
        with st.form("resume_edit_form"):
            name = st.text_input("Name", value=st.session_state.resume_draft["name"])
            email = st.text_input("Email ID", value=st.session_state.resume_draft["email"])
            phone = st.text_input("Phone Number", value=st.session_state.resume_draft["phone"])
            
            links_col1, links_col2 = st.columns(2)
            with links_col1:
                linkedin = st.text_input("LinkedIn Profile Link", value=st.session_state.resume_draft["linkedin"])
            with links_col2:
                github = st.text_input("GitHub Profile Link", value=st.session_state.resume_draft["github"])
                
            summary = st.text_area("Profile Summary Statement", value=st.session_state.resume_draft["summary"])
            
            # Skill inputs simplified
            skills_str = st.text_input("Key Skills (comma-separated)", value=", ".join(st.session_state.resume_draft["skills"]["Languages"] + st.session_state.resume_draft["skills"]["AI/ML"]))
            
            st.markdown("<div style='margin-top: 15px;'></div>", unsafe_allow_html=True)
            submit = st.form_submit_button("Update Resume Draft")
            
            if submit:
                st.session_state.resume_draft.update({
                    "name": name,
                    "email": email,
                    "phone": phone,
                    "linkedin": linkedin,
                    "github": github,
                    "summary": summary,
                })
                # parse skills back
                split_skills = [s.strip() for s in skills_str.split(",") if s.strip()]
                st.session_state.resume_draft["skills"]["Languages"] = split_skills[:4]
                st.session_state.resume_draft["skills"]["AI/ML"] = split_skills[4:]
                st.toast("Resume draft updated successfully! Check live preview on right.")
                st.rerun()

    with col2:
        st.markdown("### 📄 Live Resume Preview")
        
        draft = st.session_state.resume_draft
        
        # Elegant document styling inside glassmorphism container
        st.markdown(f"""
<div class="glass-card" style="background: #ffffff; color: #1e293b; padding: 30px; border-radius: 8px; font-family: sans-serif; box-shadow: 0 10px 25px rgba(0,0,0,0.15);">
<div style="text-align: center; border-bottom: 2px solid #6C63FF; padding-bottom: 15px; margin-bottom: 15px;">
<h2 style="color: #1e293b; margin: 0 0 5px 0; font-size: 1.8rem; font-family: sans-serif;">{draft['name']}</h2>
<div style="font-size: 0.85rem; color: #64748b;">
<span>📧 {draft['email']}</span> | <span>📞 {draft['phone']}</span>
</div>
<div style="font-size: 0.85rem; color: #6C63FF; margin-top: 4px; font-weight: 600;">
<span>{draft['linkedin']}</span> | <span>{draft['github']}</span>
</div>
</div>

<div style="margin-bottom: 15px;">
<h4 style="color: #6C63FF; text-transform: uppercase; margin: 0 0 6px 0; font-size: 0.9rem; border-bottom: 1px solid #e2e8f0; padding-bottom: 2px; font-family: sans-serif;">Summary</h4>
<p style="font-size: 0.85rem; line-height: 1.4; margin: 0; color: #334155;">{draft['summary']}</p>
</div>

<div style="margin-bottom: 15px;">
<h4 style="color: #6C63FF; text-transform: uppercase; margin: 0 0 6px 0; font-size: 0.9rem; border-bottom: 1px solid #e2e8f0; padding-bottom: 2px; font-family: sans-serif;">Education</h4>
{"".join(f'''
<div style="display: flex; justify-content: space-between; font-size: 0.85rem; margin-bottom: 4px;">
<b style="color: #1e293b;">{edu['degree']}</b>
<span style="color: #64748b;">{edu['year']}</span>
</div>
<div style="font-size: 0.82rem; color: #475569;">{edu['college']} | CGPA: {edu['cgpa']}</div>
''' for edu in draft['education'])}
</div>

<div style="margin-bottom: 15px;">
<h4 style="color: #6C63FF; text-transform: uppercase; margin: 0 0 6px 0; font-size: 0.9rem; border-bottom: 1px solid #e2e8f0; padding-bottom: 2px; font-family: sans-serif;">Skills</h4>
<div style="font-size: 0.85rem; line-height: 1.4; color: #334155;">
<div><b>Languages:</b> {", ".join(draft['skills']['Languages'])}</div>
<div><b>AI / ML:</b> {", ".join(draft['skills']['AI/ML'])}</div>
</div>
</div>

<div style="margin-bottom: 15px;">
<h4 style="color: #6C63FF; text-transform: uppercase; margin: 0 0 6px 0; font-size: 0.9rem; border-bottom: 1px solid #e2e8f0; padding-bottom: 2px; font-family: sans-serif;">Experience</h4>
{"".join(f'''
<div style="display: flex; justify-content: space-between; font-size: 0.85rem; margin-bottom: 4px;">
<b style="color: #1e293b;">{exp['role']}</b>
<span style="color: #64748b;">{exp['duration']}</span>
</div>
<div style="font-size: 0.82rem; color: #475569; font-style: italic; margin-bottom: 4px;">{exp['company']}</div>
<p style="font-size: 0.82rem; line-height: 1.4; margin: 0; color: #475569;">{exp['description']}</p>
''' for exp in draft['experience'])}
</div>
</div>
""", unsafe_allow_html=True)
        
        st.markdown("<div style='margin-top: 15px;'></div>", unsafe_allow_html=True)
        if st.button("Export Resume Draft to PDF (UI Simulation)"):
            st.success("Successfully generated & compiled PDF template. Download will begin shortly!")
