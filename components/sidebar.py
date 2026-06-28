import streamlit as st

def render_sidebar(active_page="Dashboard"):
    """
    Renders a premium macOS Finder-style left sidebar with grouped navigation,
    user profile card, XP bar, and bottom settings section.
    Uses st.page_link for clean navigation without hidden button hacks.
    """
    profile = st.session_state.get("user_profile", {
        "name": "Sanjai R",
        "career_goal": "AI Engineer",
        "avatar": "🎓",
        "cgpa": 8.75,
        "study_streak": 12,
    })
    name = profile.get("name", "Sanjai R")
    goal = profile.get("career_goal", "AI Engineer")
    first = name.split()[0][0] if name else "S"

    # Hide default sidebar and Streamlit nav
    st.markdown("""
<style>
[data-testid="stSidebarNav"] { display:none !important; }
section[data-testid="stSidebar"] { display:none !important; }
/* Style page_link items to look like premium nav items */
[data-testid="stPageLink"] {
display: block !important;
padding: 0 !important;
margin-bottom: 2px !important;
}
[data-testid="stPageLink"] a {
display: flex !important;
align-items: center !important;
gap: 9px !important;
padding: 9px 12px !important;
border-radius: 11px !important;
font-size: 0.85rem !important;
font-weight: 500 !important;
color: #475569 !important;
text-decoration: none !important;
transition: all 0.2s !important;
}
[data-testid="stPageLink"] a:hover {
background: rgba(124,58,237,0.06) !important;
color: #7C3AED !important;
}
/* Sidebar logout button */
.sidebar-logout-btn > button {
background: rgba(239,68,68,0.06) !important;
color: #DC2626 !important;
border: 1px solid rgba(239,68,68,0.15) !important;
border-radius: 12px !important;
font-weight: 600 !important;
font-size: 0.85rem !important;
padding: 8px 16px !important;
width: 100% !important;
transition: all 0.2s !important;
}
.sidebar-logout-btn > button:hover {
background: rgba(239,68,68,0.12) !important;
}
</style>
""", unsafe_allow_html=True)

    # ── Profile Card ─────────────────────────────────────────────────
    st.markdown(f"""
<div style="
background: linear-gradient(135deg, rgba(124,58,237,0.08), rgba(37,99,235,0.06));
border: 1px solid rgba(124,58,237,0.15);
border-radius: 18px;
padding: 18px 14px;
text-align: center;
margin-bottom: 18px;
">
<div style="
width:52px;height:52px;border-radius:50%;
background:linear-gradient(135deg,#7C3AED,#2563EB);
display:flex;align-items:center;justify-content:center;
font-size:1.3rem;font-weight:800;color:white;
margin:0 auto 10px;
box-shadow:0 4px 14px rgba(124,58,237,0.35);
">{first}</div>
<div style="font-family:'Outfit',sans-serif;font-weight:700;font-size:0.95rem;color:#0F172A;">{name}</div>
<div style="font-size:0.72rem;color:#7C3AED;font-weight:600;text-transform:uppercase;letter-spacing:0.08em;margin-top:2px;">{goal}</div>

<!-- XP Bar -->
<div style="margin-top:12px;">
<div style="display:flex;justify-content:space-between;font-size:0.65rem;color:#94A3B8;margin-bottom:4px;">
<span>Level 7</span><span>2,450 / 3,000 XP</span>
</div>
<div style="background:rgba(0,0,0,0.06);border-radius:99px;height:5px;overflow:hidden;">
<div style="width:81%;height:100%;background:linear-gradient(90deg,#7C3AED,#2563EB);border-radius:99px;"></div>
</div>
</div>

<!-- Stats Row -->
<div style="display:flex;gap:8px;margin-top:12px;">
<div style="flex:1;background:rgba(255,255,255,0.6);border-radius:10px;padding:8px 4px;border:1px solid rgba(0,0,0,0.05);">
<div style="font-size:1rem;font-weight:800;color:#0F172A;font-family:'Outfit',sans-serif;">{profile.get('study_streak', 12)}</div>
<div style="font-size:0.6rem;color:#94A3B8;text-transform:uppercase;letter-spacing:0.05em;">Streak</div>
</div>
<div style="flex:1;background:rgba(255,255,255,0.6);border-radius:10px;padding:8px 4px;border:1px solid rgba(0,0,0,0.05);">
<div style="font-size:1rem;font-weight:800;color:#0F172A;font-family:'Outfit',sans-serif;">{profile.get('cgpa', 8.75)}</div>
<div style="font-size:0.6rem;color:#94A3B8;text-transform:uppercase;letter-spacing:0.05em;">CGPA</div>
</div>
<div style="flex:1;background:rgba(255,255,255,0.6);border-radius:10px;padding:8px 4px;border:1px solid rgba(0,0,0,0.05);">
<div style="font-size:1rem;font-weight:800;color:#0F172A;font-family:'Outfit',sans-serif;">#5</div>
<div style="font-size:0.6rem;color:#94A3B8;text-transform:uppercase;letter-spacing:0.05em;">Rank</div>
</div>
</div>
</div>
""", unsafe_allow_html=True)

    # ── Navigation Groups ─────────────────────────────────────────────
    nav_groups = {
        "WORKSPACE": [
            ("📊", "Dashboard", "pages/1_📊_Dashboard.py"),
            ("🤖", "AI Workspace", "pages/2_🧠_AI_Tutor.py"),
            ("📚", "PDF Chat (RAG)", "pages/3_📚_PDF_Chat.py"),
        ],
        "LEARNING": [
            ("📝", "Quiz Generator", "pages/4_📝_Quiz.py"),
            ("🃏", "Flashcards", "pages/5_🃏_Flashcards.py"),
            ("📅", "Study Planner", "pages/6_📅_Study_Planner.py"),
            ("📈", "Analytics", "pages/7_📈_Analytics.py"),
        ],
        "CAREER": [
            ("📄", "Resume Builder", "pages/8_📄_Resume_Builder.py"),
            ("✅", "ATS Checker", "pages/9_✅_ATS_Checker.py"),
            ("💼", "Placements", "pages/10_💼_Internships.py"),
            ("🎤", "Mock Interview", "pages/11_🎤_Mock_Interview.py"),
        ],
    }

    for group_label, items in nav_groups.items():
        st.markdown(f"""
<div style="font-size:0.63rem;font-weight:700;color:#94A3B8;
text-transform:uppercase;letter-spacing:0.1em;
padding:10px 4px 4px;">
{group_label}
</div>
""", unsafe_allow_html=True)

        for icon, label, path in items:
            is_active = active_page == label
            if is_active:
                st.markdown(f"""
<div style="
display:flex;align-items:center;gap:9px;
padding:9px 12px;border-radius:11px;margin-bottom:2px;
background:linear-gradient(135deg,rgba(124,58,237,0.10),rgba(37,99,235,0.07));
color:#7C3AED;font-size:0.85rem;font-weight:600;
border-left:3px solid #7C3AED;
">
<span>{icon}</span>
<span>{label}</span>
<div style="margin-left:auto;width:6px;height:6px;border-radius:50%;background:#7C3AED;"></div>
</div>
""", unsafe_allow_html=True)
            else:
                st.page_link(path, label=f"{icon}  {label}")

    # ── Divider ───────────────────────────────────────────────────────
    st.markdown("<div style='height:1px;background:rgba(0,0,0,0.05);margin:12px 0;'></div>", unsafe_allow_html=True)

    # ── AI Engine Status ──────────────────────────────────────────────
    st.markdown("""
<div style="
background:rgba(34,197,94,0.06);
border:1px solid rgba(34,197,94,0.15);
border-radius:12px;padding:11px 14px;
display:flex;align-items:center;gap:8px;margin-bottom:12px;
">
<div style="width:8px;height:8px;border-radius:50%;background:#22C55E;
box-shadow:0 0 8px rgba(34,197,94,0.6);flex-shrink:0;"></div>
<div>
<div style="font-size:0.78rem;font-weight:600;color:#16A34A;">AI Engine Online</div>
<div style="font-size:0.65rem;color:#94A3B8;">FastAPI · Port 8000</div>
</div>
</div>
""", unsafe_allow_html=True)

    # ── Logout ────────────────────────────────────────────────────────
    st.markdown('<div class="sidebar-logout-btn">', unsafe_allow_html=True)
    if st.button("🚪 Sign Out", key="sidebar_logout"):
        st.session_state.authenticated = False
        st.switch_page("app.py")
    st.markdown('</div>', unsafe_allow_html=True)
