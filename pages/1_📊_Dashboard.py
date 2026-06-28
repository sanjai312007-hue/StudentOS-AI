import streamlit as st
import datetime
import random
from components.styles import apply_custom_styles
from components.navbar import render_navbar
from components.sidebar import render_sidebar
from data.mock_data import (
    DASHBOARD_STATS, UPCOMING_EVENTS, TODAYS_SCHEDULE, STUDENT_PROFILE,
    MONTHLY_STUDY_HEATMAP, WEEKLY_SCORES
)

st.set_page_config(
    page_title="Dashboard | StudentOS AI",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

apply_custom_styles()

if "authenticated" not in st.session_state or not st.session_state.authenticated:
    st.warning("🔒 Please authenticate first on the homepage.")
    st.stop()

# ── Floating Navbar ──────────────────────────────────────────────
render_navbar()

# ── Aurora Background Blobs ──────────────────────────────────────
st.markdown("""
<div class="aurora-blob-1"></div>
<div class="aurora-blob-2"></div>
<div class="aurora-blob-3"></div>
""", unsafe_allow_html=True)

# ── Main Layout: Sidebar + Content ───────────────────────────────
col_nav, col_content = st.columns([1.2, 5])

with col_nav:
    render_sidebar(active_page="Dashboard")

with col_content:
    stats = DASHBOARD_STATS
    profile = st.session_state.get("user_profile", STUDENT_PROFILE)
    now = datetime.datetime.now()
    hour = now.hour
    greeting = "Good Morning" if hour < 12 else ("Good Afternoon" if hour < 17 else "Good Evening")

    # ════════════════════════════════════════════════════════════════
    #  HERO SECTION
    # ════════════════════════════════════════════════════════════════
    st.markdown(f"""
<div class="hero-section">
<div style="display:flex;justify-content:space-between;align-items:flex-start;flex-wrap:wrap;gap:20px;">
<div style="flex:1;min-width:300px;">
<div style="font-size:0.85rem;color:#64748B;font-weight:500;margin-bottom:4px;">
👋 {greeting}
</div>
<h1 style="font-size:2.4rem;margin:0 0 8px 0;line-height:1.15;
color:#0F172A !important;font-family:'Outfit',sans-serif !important;font-weight:800;">
{profile['name']}
</h1>
<p style="font-size:0.95rem;color:#64748B;margin:0 0 18px 0;max-width:420px;">
Today is a great day to learn. You have <b style="color:#7C3AED;">{len([e for e in UPCOMING_EVENTS if e['priority']=='high'])} high-priority</b> items and
<b style="color:#2563EB;">{len(TODAYS_SCHEDULE)} study sessions</b> planned.
</p>

<!-- Today's Focus Tags -->
<div style="display:flex;gap:8px;flex-wrap:wrap;margin-bottom:20px;">
<span class="badge badge-purple">🎯 Python</span>
<span class="badge badge-blue">📚 DBMS</span>
<span class="badge badge-amber">📄 Resume</span>
<span class="badge badge-green">✅ DSA Practice</span>
</div>

<!-- Quick Action Buttons -->
<div style="display:flex;gap:10px;flex-wrap:wrap;">
<div style="
background:linear-gradient(135deg,#7C3AED,#2563EB);color:white;
padding:10px 22px;border-radius:12px;font-size:0.85rem;font-weight:600;
cursor:pointer;box-shadow:0 4px 16px rgba(124,58,237,0.3);
transition:all 0.25s;display:flex;align-items:center;gap:6px;
">🚀 Continue Learning</div>
<div style="
background:rgba(255,255,255,0.8);color:#0F172A;
padding:10px 22px;border-radius:12px;font-size:0.85rem;font-weight:600;
cursor:pointer;border:1px solid rgba(0,0,0,0.08);
transition:all 0.25s;display:flex;align-items:center;gap:6px;
">🤖 Ask AI</div>
<div style="
background:rgba(255,255,255,0.8);color:#0F172A;
padding:10px 22px;border-radius:12px;font-size:0.85rem;font-weight:600;
cursor:pointer;border:1px solid rgba(0,0,0,0.08);
transition:all 0.25s;display:flex;align-items:center;gap:6px;
">🎯 Focus Mode</div>
</div>
</div>

<!-- Goal Ring + Stats -->
<div style="display:flex;gap:20px;align-items:center;">
<!-- SVG Circular Progress -->
<div style="text-align:center;">
<svg width="120" height="120" viewBox="0 0 120 120">
<circle cx="60" cy="60" r="50" fill="none" stroke="rgba(0,0,0,0.06)" stroke-width="8"/>
<circle cx="60" cy="60" r="50" fill="none" stroke="url(#grad1)" stroke-width="8"
stroke-linecap="round" stroke-dasharray="314" stroke-dashoffset="{314 - (314 * 0.84)}"
transform="rotate(-90 60 60)"
style="transition:stroke-dashoffset 1.5s cubic-bezier(0.23,1,0.32,1)"/>
<defs>
<linearGradient id="grad1" x1="0%" y1="0%" x2="100%" y2="0%">
<stop offset="0%" style="stop-color:#7C3AED"/>
<stop offset="100%" style="stop-color:#2563EB"/>
</linearGradient>
</defs>
<text x="60" y="56" text-anchor="middle" style="font-family:'Outfit',sans-serif;font-size:26px;font-weight:800;fill:#0F172A;">84%</text>
<text x="60" y="72" text-anchor="middle" style="font-size:10px;fill:#94A3B8;font-weight:600;">WEEKLY GOAL</text>
</svg>
</div>

<!-- Mini stats -->
<div style="display:flex;flex-direction:column;gap:8px;">
<div style="background:rgba(255,255,255,0.7);border:1px solid rgba(0,0,0,0.06);border-radius:12px;padding:10px 16px;">
<div style="font-size:0.65rem;color:#94A3B8;font-weight:600;text-transform:uppercase;">Study Today</div>
<div style="font-size:1.3rem;font-weight:800;color:#0F172A;font-family:'Outfit',sans-serif;">3h 12m</div>
</div>
<div style="background:rgba(255,255,255,0.7);border:1px solid rgba(0,0,0,0.06);border-radius:12px;padding:10px 16px;">
<div style="font-size:0.65rem;color:#94A3B8;font-weight:600;text-transform:uppercase;">Current Rank</div>
<div style="font-size:1.3rem;font-weight:800;color:#0F172A;font-family:'Outfit',sans-serif;">#5 <span style="font-size:0.7rem;color:#22C55E;">↑2</span></div>
</div>
<div style="background:rgba(255,255,255,0.7);border:1px solid rgba(0,0,0,0.06);border-radius:12px;padding:10px 16px;">
<div style="font-size:0.65rem;color:#94A3B8;font-weight:600;text-transform:uppercase;">XP</div>
<div style="font-size:1.3rem;font-weight:800;color:#7C3AED;font-family:'Outfit',sans-serif;">2,450</div>
</div>
</div>
</div>
</div>
</div>
""", unsafe_allow_html=True)

    # ════════════════════════════════════════════════════════════════
    #  SMART STATS CARDS (4 across)
    # ════════════════════════════════════════════════════════════════
    st.markdown("""
<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:16px;margin-bottom:24px;">

<!-- Study Streak -->
<div class="stat-card">
<div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:10px;">
<div style="width:40px;height:40px;border-radius:12px;
background:rgba(245,158,11,0.1);display:flex;align-items:center;justify-content:center;
font-size:1.2rem;">🔥</div>
<span class="badge badge-green" style="font-size:0.65rem;">Top 5%</span>
</div>
<div style="font-size:0.72rem;color:#94A3B8;font-weight:600;text-transform:uppercase;letter-spacing:0.08em;">Study Streak</div>
<div style="font-size:2.2rem;font-weight:800;color:#0F172A;font-family:'Outfit',sans-serif;line-height:1;">12 Days</div>
<div style="display:flex;align-items:center;gap:4px;margin-top:8px;">
<span style="color:#22C55E;font-size:0.78rem;font-weight:700;">↑ 15%</span>
<span style="color:#94A3B8;font-size:0.72rem;">from last week</span>
</div>
<div style="margin-top:10px;">
<div class="progress-track"><div class="progress-fill-green" style="width:88%;"></div></div>
</div>
</div>

<!-- Weekly Study -->
<div class="stat-card">
<div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:10px;">
<div style="width:40px;height:40px;border-radius:12px;
background:rgba(37,99,235,0.1);display:flex;align-items:center;justify-content:center;
font-size:1.2rem;">📚</div>
<span style="font-size:0.68rem;color:#64748B;">Target: 25 hrs</span>
</div>
<div style="font-size:0.72rem;color:#94A3B8;font-weight:600;text-transform:uppercase;letter-spacing:0.08em;">Weekly Study</div>
<div style="font-size:2.2rem;font-weight:800;color:#0F172A;font-family:'Outfit',sans-serif;line-height:1;">22 Hours</div>
<div style="display:flex;align-items:center;gap:4px;margin-top:8px;">
<span style="color:#22C55E;font-size:0.78rem;font-weight:700;">↑ 8%</span>
<span style="color:#94A3B8;font-size:0.72rem;">from last week</span>
</div>
<div style="margin-top:10px;">
<div class="progress-track"><div class="progress-fill" style="width:88%;"></div></div>
</div>
</div>

<!-- Avg Quiz Score -->
<div class="stat-card">
<div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:10px;">
<div style="width:40px;height:40px;border-radius:12px;
background:rgba(124,58,237,0.1);display:flex;align-items:center;justify-content:center;
font-size:1.2rem;">🎯</div>
<span style="font-size:0.68rem;color:#64748B;">47 quizzes</span>
</div>
<div style="font-size:0.72rem;color:#94A3B8;font-weight:600;text-transform:uppercase;letter-spacing:0.08em;">Avg Quiz Score</div>
<div style="font-size:2.2rem;font-weight:800;color:#0F172A;font-family:'Outfit',sans-serif;line-height:1;">82%</div>
<div style="display:flex;align-items:center;gap:4px;margin-top:8px;">
<span style="color:#22C55E;font-size:0.78rem;font-weight:700;">↑ 6%</span>
<span style="color:#94A3B8;font-size:0.72rem;">improvement</span>
</div>
<div style="margin-top:10px;">
<div class="progress-track"><div class="progress-fill" style="width:82%;"></div></div>
</div>
</div>

<!-- Resume ATS -->
<div class="stat-card">
<div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:10px;">
<div style="width:40px;height:40px;border-radius:12px;
background:rgba(6,182,212,0.1);display:flex;align-items:center;justify-content:center;
font-size:1.2rem;">💼</div>
<span class="badge badge-amber" style="font-size:0.65rem;">Improve</span>
</div>
<div style="font-size:0.72rem;color:#94A3B8;font-weight:600;text-transform:uppercase;letter-spacing:0.08em;">Resume ATS</div>
<div style="font-size:2.2rem;font-weight:800;color:#0F172A;font-family:'Outfit',sans-serif;line-height:1;">78/100</div>
<div style="display:flex;align-items:center;gap:4px;margin-top:8px;">
<span style="color:#D97706;font-size:0.78rem;font-weight:700;">5 skills</span>
<span style="color:#94A3B8;font-size:0.72rem;">can be improved</span>
</div>
<div style="margin-top:10px;">
<div class="progress-track"><div class="progress-fill-amber" style="width:78%;"></div></div>
</div>
</div>

</div>
""", unsafe_allow_html=True)

    # ════════════════════════════════════════════════════════════════
    #  QUICK ACTIONS + REMINDERS ROW
    # ════════════════════════════════════════════════════════════════
    qa_col, rem_col = st.columns([2.5, 1.5])

    with qa_col:
        st.markdown("""
<h3 style="font-size:1.1rem;margin:0 0 14px 0;color:#0F172A !important;">⚡ Quick Actions</h3>
<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin-bottom:24px;">
<div class="quick-action-card">
<div style="font-size:1.6rem;margin-bottom:8px;">🧠</div>
<div style="font-size:0.82rem;font-weight:600;color:#0F172A;">Launch AI Tutor</div>
<div style="font-size:0.7rem;color:#94A3B8;margin-top:4px;">Chat with your personal AI</div>
</div>
<div class="quick-action-card">
<div style="font-size:1.6rem;margin-bottom:8px;">📝</div>
<div style="font-size:0.82rem;font-weight:600;color:#0F172A;">Start Quiz Session</div>
<div style="font-size:0.7rem;color:#94A3B8;margin-top:4px;">Test your knowledge</div>
</div>
<div class="quick-action-card">
<div style="font-size:1.6rem;margin-bottom:8px;">📄</div>
<div style="font-size:0.82rem;font-weight:600;color:#0F172A;">Upload Study PDF</div>
<div style="font-size:0.7rem;color:#94A3B8;margin-top:4px;">Chat with documents</div>
</div>
<div class="quick-action-card">
<div style="font-size:1.6rem;margin-bottom:8px;">🤖</div>
<div style="font-size:0.82rem;font-weight:600;color:#0F172A;">AI Chat (RAG)</div>
<div style="font-size:0.7rem;color:#94A3B8;margin-top:4px;">Retrieval-augmented search</div>
</div>
<div class="quick-action-card">
<div style="font-size:1.6rem;margin-bottom:8px;">🃏</div>
<div style="font-size:0.82rem;font-weight:600;color:#0F172A;">Create Flashcards</div>
<div style="font-size:0.7rem;color:#94A3B8;margin-top:4px;">Spaced repetition decks</div>
</div>
<div class="quick-action-card">
<div style="font-size:1.6rem;margin-bottom:8px;">🎯</div>
<div style="font-size:0.82rem;font-weight:600;color:#0F172A;">Focus Mode</div>
<div style="font-size:0.7rem;color:#94A3B8;margin-top:4px;">Distraction-free study</div>
</div>
</div>
""", unsafe_allow_html=True)

    with rem_col:
        st.markdown("""
<div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:14px;">
<h3 style="font-size:1.1rem;margin:0;color:#0F172A !important;">🔔 Reminders & Deadlines</h3>
<span style="font-size:0.72rem;color:#7C3AED;font-weight:600;cursor:pointer;">+ Add</span>
</div>
""", unsafe_allow_html=True)

        for event in UPCOMING_EVENTS[:4]:
            if event["priority"] == "high":
                pri_style = "background:rgba(239,68,68,0.08);color:#DC2626;border-left:3px solid #EF4444;"
                pri_label = "HIGH"
            elif event["priority"] == "medium":
                pri_style = "background:rgba(245,158,11,0.08);color:#D97706;border-left:3px solid #F59E0B;"
                pri_label = "MEDIUM"
            else:
                pri_style = "background:rgba(34,197,94,0.08);color:#16A34A;border-left:3px solid #22C55E;"
                pri_label = "LOW"

            st.markdown(f"""
<div style="{pri_style}border-radius:12px;padding:12px 14px;margin-bottom:8px;">
<div style="display:flex;justify-content:space-between;align-items:center;">
<span style="font-size:0.7rem;font-weight:700;text-transform:uppercase;letter-spacing:0.05em;">{pri_label}</span>
<span style="font-size:0.72rem;color:#94A3B8;">{event['due']}</span>
</div>
<div style="font-size:0.85rem;font-weight:600;color:#0F172A;margin-top:4px;">{event['title']}</div>
<div style="font-size:0.72rem;color:#64748B;margin-top:2px;">{event['subject']}</div>
</div>
""", unsafe_allow_html=True)

    # ════════════════════════════════════════════════════════════════
    #  CONTINUE LEARNING (Netflix-style)
    # ════════════════════════════════════════════════════════════════
    st.markdown("""
<div style="display:flex;justify-content:space-between;align-items:center;margin:8px 0 14px 0;">
<h3 style="font-size:1.1rem;margin:0;color:#0F172A !important;">📚 Continue Learning</h3>
<span style="font-size:0.78rem;color:#7C3AED;font-weight:600;cursor:pointer;">View All →</span>
</div>
""", unsafe_allow_html=True)

    courses = [
        {"name": "Python", "progress": 72, "diff": "Intermediate", "remaining": "3h 40m", "icon": "🐍", "color": "#6C63FF", "action": "Continue →"},
        {"name": "DBMS", "progress": 48, "diff": "Intermediate", "remaining": "5h 20m", "icon": "🗃️", "color": "#FF6B6B", "action": "Continue →"},
        {"name": "Operating Systems", "progress": 35, "diff": "Advanced", "remaining": "8h 10m", "icon": "⚙️", "color": "#4ECDC4", "action": "Continue →"},
        {"name": "Machine Learning", "progress": 92, "diff": "Intermediate", "remaining": "1h 00m", "icon": "🧠", "color": "#FFE66D", "action": "Review →"},
        {"name": "DSA", "progress": 55, "diff": "Advanced", "remaining": "6h 30m", "icon": "🌲", "color": "#A78BFA", "action": "Practice →"},
    ]

    course_cards_html = '<div style="display:grid;grid-template-columns:repeat(5,1fr);gap:14px;margin-bottom:24px;">'
    for c in courses:
        dash_offset = 157 - (157 * c["progress"] / 100)
        course_cards_html += f"""
        <div class="course-card">
            <div style="display:flex;align-items:center;gap:10px;margin-bottom:14px;">
                <div style="width:38px;height:38px;border-radius:10px;
                    background:rgba({','.join([str(int(c['color'][i:i+2],16)) for i in (1,3,5)])},0.12);
                    display:flex;align-items:center;justify-content:center;font-size:1.2rem;">
                    {c['icon']}
                </div>
                <div>
                    <div style="font-size:0.88rem;font-weight:700;color:#0F172A;">{c['name']}</div>
                    <div style="font-size:0.68rem;color:#94A3B8;">{c['diff']}</div>
                </div>
            </div>

            <!-- SVG Progress Ring -->
            <div style="text-align:center;margin-bottom:12px;">
                <svg width="70" height="70" viewBox="0 0 70 70">
                    <circle cx="35" cy="35" r="25" fill="none" stroke="rgba(0,0,0,0.06)" stroke-width="5"/>
                    <circle cx="35" cy="35" r="25" fill="none" stroke="{c['color']}" stroke-width="5"
                        stroke-linecap="round" stroke-dasharray="157" stroke-dashoffset="{dash_offset}"
                        transform="rotate(-90 35 35)" style="transition:stroke-dashoffset 1.5s ease;"/>
                    <text x="35" y="38" text-anchor="middle" style="font-family:'Outfit',sans-serif;font-size:14px;font-weight:800;fill:#0F172A;">{c['progress']}%</text>
                </svg>
            </div>

            <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:8px;">
                <span style="font-size:0.7rem;color:#94A3B8;">⏱ {c['remaining']} left</span>
            </div>

            <div style="
                text-align:center;padding:8px;border-radius:10px;
                background:linear-gradient(135deg,rgba(124,58,237,0.08),rgba(37,99,235,0.06));
                font-size:0.78rem;font-weight:600;color:#7C3AED;cursor:pointer;
                transition:all 0.2s;
            ">{c['action']}</div>
        </div>
        """
    course_cards_html += "</div>"
    st.markdown(course_cards_html, unsafe_allow_html=True)

    # ════════════════════════════════════════════════════════════════
    #  TODAY'S SCHEDULE + AI WORKSPACE
    # ════════════════════════════════════════════════════════════════
    sched_col, ai_col = st.columns([2.2, 1.8])

    with sched_col:
        st.markdown("""
<div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:14px;">
<h3 style="font-size:1.1rem;margin:0;color:#0F172A !important;">📅 Today's Study Schedule</h3>
<span style="font-size:0.72rem;color:#7C3AED;font-weight:600;cursor:pointer;">View Calendar →</span>
</div>
""", unsafe_allow_html=True)

        for item in TODAYS_SCHEDULE:
            if item["status"] == "completed":
                status_badge = '<span class="badge badge-green" style="font-size:0.65rem;">✓ Completed</span>'
                opacity = "0.7"
            elif item["status"] == "in_progress":
                status_badge = '<span class="badge badge-purple" style="font-size:0.65rem;">● In Progress</span>'
                opacity = "1"
            else:
                status_badge = '<span class="badge" style="font-size:0.65rem;background:rgba(0,0,0,0.04);color:#94A3B8;border:1px solid rgba(0,0,0,0.06);">Upcoming</span>'
                opacity = "0.85"

            st.markdown(f"""
<div class="glass-card" style="
padding:14px 18px !important;margin-bottom:10px !important;
display:flex;align-items:center;gap:14px;opacity:{opacity};
border-left:4px solid {item['color']} !important;
">
<div style="min-width:80px;">
<div style="font-size:0.85rem;font-weight:700;color:#0F172A;">{item['time']}</div>
<div style="font-size:0.7rem;color:#94A3B8;">{item['duration']}</div>
</div>
<div style="flex:1;">
<div style="font-size:0.9rem;font-weight:600;color:#0F172A;">{item['subject']}</div>
<div style="font-size:0.72rem;color:#64748B;text-transform:capitalize;">{item['type']}</div>
</div>
<div style="display:flex;align-items:center;gap:8px;">
<!-- Mini Progress -->
<div style="width:80px;">
<div class="progress-track" style="height:5px;">
<div class="progress-fill" style="width:{'100' if item['status']=='completed' else ('50' if item['status']=='in_progress' else '0')}%;background:{item['color']};"></div>
</div>
</div>
{status_badge}
</div>
</div>
""", unsafe_allow_html=True)

    with ai_col:
        st.markdown("""
<h3 style="font-size:1.1rem;margin:0 0 14px 0;color:#0F172A !important;">🤖 AI Workspace</h3>
<div class="glass-card" style="text-align:center;padding:30px 20px !important;">
<!-- AI Orb -->
<div class="ai-orb" style="margin-bottom:18px;"></div>
<h4 style="color:#0F172A !important;margin:0 0 4px 0;font-size:1.05rem;">StudentOS AI</h4>
<p style="color:#94A3B8 !important;font-size:0.8rem;margin:0 0 18px 0;">Your AI-powered learning companion</p>

<div style="display:grid;grid-template-columns:repeat(2,1fr);gap:8px;">
<div class="quick-action-card" style="padding:12px 8px;">
<div style="font-size:1.1rem;">📝</div>
<div style="font-size:0.72rem;font-weight:600;color:#0F172A;margin-top:4px;">Generate Notes</div>
</div>
<div class="quick-action-card" style="padding:12px 8px;">
<div style="font-size:1.1rem;">💡</div>
<div style="font-size:0.72rem;font-weight:600;color:#0F172A;margin-top:4px;">Explain Concepts</div>
</div>
<div class="quick-action-card" style="padding:12px 8px;">
<div style="font-size:1.1rem;">📊</div>
<div style="font-size:0.72rem;font-weight:600;color:#0F172A;margin-top:4px;">Create Quiz</div>
</div>
<div class="quick-action-card" style="padding:12px 8px;">
<div style="font-size:1.1rem;">🗺️</div>
<div style="font-size:0.72rem;font-weight:600;color:#0F172A;margin-top:4px;">Mind Maps</div>
</div>
<div class="quick-action-card" style="padding:12px 8px;">
<div style="font-size:1.1rem;">🎤</div>
<div style="font-size:0.72rem;font-weight:600;color:#0F172A;margin-top:4px;">Voice Tutor</div>
</div>
<div class="quick-action-card" style="padding:12px 8px;">
<div style="font-size:1.1rem;">💻</div>
<div style="font-size:0.72rem;font-weight:600;color:#0F172A;margin-top:4px;">Code Assistant</div>
</div>
</div>
</div>
""", unsafe_allow_html=True)

    # ════════════════════════════════════════════════════════════════
    #  STUDY HEATMAP + ACHIEVEMENTS + AI INSIGHTS
    # ════════════════════════════════════════════════════════════════
    heat_col, ach_col, insight_col = st.columns([1.5, 1.5, 1.2])

    with heat_col:
        st.markdown("""<h3 style="font-size:1.1rem;margin:0 0 14px 0;color:#0F172A !important;">🌡️ Study Heatmap</h3>""", unsafe_allow_html=True)

        heatmap_html = '<div class="glass-card" style="padding:18px !important;">'
        heatmap_html += '<div style="display:flex;justify-content:space-between;margin-bottom:8px;font-size:0.68rem;color:#94A3B8;">'
        for d in ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]:
            heatmap_html += f'<span style="width:16px;text-align:center;">{d}</span>'
        heatmap_html += '</div>'

        colors_map = {0:"rgba(0,0,0,0.04)",1:"rgba(124,58,237,0.12)",2:"rgba(124,58,237,0.25)",3:"rgba(124,58,237,0.4)",4:"rgba(124,58,237,0.6)",5:"rgba(124,58,237,0.8)"}
        for week_idx in range(8):
            heatmap_html += '<div style="display:flex;gap:3px;margin-bottom:3px;">'
            for day in range(7):
                val = random.choice([0,0,1,2,2,3,3,4,4,5])
                clr = colors_map.get(val, colors_map[5])
                heatmap_html += f'<div class="heatmap-cell" style="background:{clr};" title="{val}h studied"></div>'
            heatmap_html += '</div>'
        heatmap_html += '<div style="display:flex;justify-content:flex-end;align-items:center;gap:4px;margin-top:8px;font-size:0.65rem;color:#94A3B8;"><span>Less</span>'
        for i in range(6):
            heatmap_html += f'<div class="heatmap-cell" style="background:{colors_map[i]};"></div>'
        heatmap_html += '<span>More</span></div></div>'
        st.markdown(heatmap_html, unsafe_allow_html=True)

    with ach_col:
        st.markdown("""
<div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:14px;">
<h3 style="font-size:1.1rem;margin:0;color:#0F172A !important;">🏆 Achievements</h3>
<span style="font-size:0.72rem;color:#7C3AED;font-weight:600;cursor:pointer;">View All</span>
</div>
""", unsafe_allow_html=True)

        badges = [
            ("🏅", "100 Day Streak", "Gold", "#F59E0B"),
            ("🏆", "Quiz Master", "Score 90%+", "#7C3AED"),
            ("🎯", "Consistent", "4 Weeks", "#2563EB"),
            ("🌅", "Early Bird", "Morning Learner", "#06B6D4"),
        ]

        badges_html = '<div style="display:grid;grid-template-columns:repeat(2,1fr);gap:10px;">'
        for emoji, title, sub, color in badges:
            badges_html += f"""
            <div class="glass-card badge-flip-container" style="padding:16px !important;text-align:center;cursor:pointer;">
                <div class="badge-flip-inner">
                    <div class="badge-front">
                        <div style="font-size:2rem;margin-bottom:6px;">{emoji}</div>
                        <div style="font-size:0.8rem;font-weight:700;color:#0F172A;">{title}</div>
                        <div style="font-size:0.68rem;color:{color};font-weight:600;">{sub}</div>
                    </div>
                </div>
            </div>
            """
        badges_html += '</div>'
        st.markdown(badges_html, unsafe_allow_html=True)

    with insight_col:
        st.markdown("""<h3 style="font-size:1.1rem;margin:0 0 14px 0;color:#0F172A !important;">🧠 AI Insights</h3>""", unsafe_allow_html=True)

        insights = [
            ("⏰", "Peak Focus", "9AM - 11AM", "Your best study window", "#22C55E"),
            ("⚠️", "Weak Subject", "Operating Systems", "Score: 50% — needs attention", "#EF4444"),
            ("⭐", "Strong Subject", "Python", "Score: 92% — excellent", "#22C55E"),
            ("💡", "AI Recommends", "Practice SQL Today", "Based on exam proximity", "#7C3AED"),
            ("📊", "Exam Readiness", "88%", "Estimated composite score", "#2563EB"),
        ]

        for icon, label, value, desc, color in insights:
            st.markdown(f"""
<div class="glass-card" style="padding:12px 14px !important;margin-bottom:8px !important;display:flex;align-items:center;gap:10px;">
<div style="width:34px;height:34px;border-radius:10px;
background:rgba({','.join([str(int(color[i:i+2],16)) for i in (1,3,5)])},0.1);
display:flex;align-items:center;justify-content:center;font-size:1rem;flex-shrink:0;">
{icon}
</div>
<div style="flex:1;">
<div style="font-size:0.7rem;color:#94A3B8;font-weight:600;text-transform:uppercase;">{label}</div>
<div style="font-size:0.88rem;font-weight:700;color:#0F172A;">{value}</div>
<div style="font-size:0.68rem;color:#64748B;">{desc}</div>
</div>
</div>
""", unsafe_allow_html=True)

    # ════════════════════════════════════════════════════════════════
    #  LEADERBOARD + POMODORO + PERFORMANCE ROW
    # ════════════════════════════════════════════════════════════════
    lb_col, pomo_col, perf_col = st.columns([1.3, 1, 1.7])

    with lb_col:
        st.markdown("""<h3 style="font-size:1.1rem;margin:0 0 14px 0;color:#0F172A !important;">🏅 Leaderboard</h3>""", unsafe_allow_html=True)

        leaders = [
            ("🥇", "Alex K", 3250, "#F59E0B"),
            ("🥈", "Priya S", 3150, "#94A3B8"),
            ("🥉", "Sanjai R", 2980, "#CD7F32"),
            ("4", "Ravi M", 2870, "#64748B"),
            ("5", "Neha T", 2760, "#64748B"),
        ]

        st.markdown('<div class="glass-card" style="padding:16px !important;">', unsafe_allow_html=True)
        for rank, name, xp, color in leaders:
            is_you = "Sanjai" in name
            bg = "rgba(124,58,237,0.06)" if is_you else "transparent"
            border = "1px solid rgba(124,58,237,0.15)" if is_you else "none"
            st.markdown(f"""
<div style="display:flex;align-items:center;gap:10px;padding:8px 10px;border-radius:10px;margin-bottom:4px;background:{bg};border:{border};">
<span style="font-size:1.1rem;min-width:24px;">{rank}</span>
<div style="flex:1;">
<div style="font-size:0.85rem;font-weight:{'700' if is_you else '500'};color:#0F172A;">
{name} {'<span style="font-size:0.7rem;color:#7C3AED;">(You)</span>' if is_you else ''}
</div>
</div>
<span style="font-size:0.82rem;font-weight:700;color:{color};">{xp:,} XP</span>
</div>
""", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with pomo_col:
        st.markdown("""<h3 style="font-size:1.1rem;margin:0 0 14px 0;color:#0F172A !important;">⏱️ Pomodoro</h3>""", unsafe_allow_html=True)
        st.markdown("""
<div class="glass-card" style="text-align:center;padding:24px 16px !important;">
<div class="pomodoro-display">25:00</div>
<div style="font-size:0.78rem;color:#94A3B8;margin:6px 0 16px;">Focus Session</div>
<div style="display:flex;gap:8px;justify-content:center;">
<div style="
background:linear-gradient(135deg,#7C3AED,#2563EB);color:white;
padding:8px 18px;border-radius:10px;font-size:0.82rem;font-weight:600;cursor:pointer;
box-shadow:0 3px 12px rgba(124,58,237,0.3);
">▶ Start</div>
<div style="
background:rgba(0,0,0,0.04);color:#64748B;
padding:8px 14px;border-radius:10px;font-size:0.82rem;font-weight:600;cursor:pointer;
border:1px solid rgba(0,0,0,0.06);
">⏭ Skip</div>
</div>
<div style="display:flex;justify-content:center;gap:16px;margin-top:16px;">
<div style="text-align:center;">
<div style="font-size:1.1rem;font-weight:800;color:#0F172A;font-family:'Outfit',sans-serif;">4</div>
<div style="font-size:0.6rem;color:#94A3B8;">Sessions</div>
</div>
<div style="text-align:center;">
<div style="font-size:1.1rem;font-weight:800;color:#0F172A;font-family:'Outfit',sans-serif;">1h 40m</div>
<div style="font-size:0.6rem;color:#94A3B8;">Total Focus</div>
</div>
</div>
</div>
""", unsafe_allow_html=True)

    with perf_col:
        st.markdown("""<h3 style="font-size:1.1rem;margin:0 0 14px 0;color:#0F172A !important;">📊 Performance Overview</h3>""", unsafe_allow_html=True)
        st.markdown("""
<div class="glass-card" style="padding:18px !important;">
<div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:14px;">
<span style="font-size:0.82rem;font-weight:600;color:#0F172A;">Weekly Report</span>
<span style="font-size:0.72rem;color:#7C3AED;font-weight:600;cursor:pointer;">Download PDF</span>
</div>
""", unsafe_allow_html=True)

        perf_items = [
            ("Study Hours", "22 hrs", 88, "#7C3AED"),
            ("Quiz Average", "82%", 82, "#2563EB"),
            ("Assignments", "5/5", 100, "#22C55E"),
            ("Consistency", "95%", 95, "#06B6D4"),
            ("Improvement", "+18%", 78, "#F59E0B"),
        ]

        for label, value, pct, color in perf_items:
            st.markdown(f"""
<div style="margin-bottom:12px;">
<div style="display:flex;justify-content:space-between;font-size:0.8rem;margin-bottom:4px;">
<span style="color:#475569;font-weight:500;">{label}</span>
<span style="color:#0F172A;font-weight:700;">{value}</span>
</div>
<div class="progress-track">
<div style="width:{pct}%;height:100%;border-radius:99px;background:{color};transition:width 1.2s ease;"></div>
</div>
</div>
""", unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)

    # ════════════════════════════════════════════════════════════════
    #  FLOATING AI BUBBLE
    # ════════════════════════════════════════════════════════════════
    st.markdown("""
<div class="ai-bubble">
<div class="ai-bubble-btn" title="Talk with AI">🤖</div>
</div>
""", unsafe_allow_html=True)
