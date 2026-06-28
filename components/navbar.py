import streamlit as st
import datetime

def render_navbar():
    """
    Renders a functional floating navbar using native Streamlit columns.
    Features: Logo, Search Input, Weather, Notification Button, AI Status, User Profile
    """
    now = datetime.datetime.now()
    hour = now.hour
    greeting = "Good Morning" if hour < 12 else ("Good Afternoon" if hour < 17 else "Good Evening")
    date_str = now.strftime("%A, %d %b %Y")
    time_str = now.strftime("%H:%M")

    profile = st.session_state.get("user_profile", {"name": "Sanjai R", "career_goal": "AI Engineer"})
    name = profile.get("name", "Sanjai R").split()[0]
    
    st.markdown("""
    <style>
    /* Styling for the floating navbar container */
    [data-testid="stHorizontalBlock"] {
        background: rgba(255, 255, 255, 0.88);
        backdrop-filter: blur(20px) saturate(180%);
        -webkit-backdrop-filter: blur(20px) saturate(180%);
        border-bottom: 1px solid rgba(0,0,0,0.06);
        padding: 10px 28px;
        border-radius: 0 0 16px 16px;
        box-shadow: 0 4px 20px rgba(15,23,42,0.05);
        align-items: center;
        margin-bottom: 24px;
        position: sticky;
        top: 0;
        z-index: 999;
    }
    
    /* Subtle animation classes */
    @keyframes pulse-green {
        0% { box-shadow: 0 0 0 0 rgba(34, 197, 94, 0.4); }
        70% { box-shadow: 0 0 0 6px rgba(34, 197, 94, 0); }
        100% { box-shadow: 0 0 0 0 rgba(34, 197, 94, 0); }
    }
    </style>
    """, unsafe_allow_html=True)

    # Use native columns to replicate the layout
    col_logo, col_search, col_space, col_weather, col_notif, col_status, col_profile = st.columns([1.5, 3, 1, 1.2, 0.6, 1.2, 1.5], gap="small")
    
    with col_logo:
        st.markdown("""
        <div style="display:flex;align-items:center;gap:8px; height: 100%;">
            <div style="width:34px;height:34px;border-radius:10px;background:linear-gradient(135deg,#7C3AED,#2563EB);display:flex;align-items:center;justify-content:center;font-size:1rem;color:white;box-shadow:0 4px 12px rgba(124,58,237,0.3);">🎓</div>
            <span style="font-family:'Outfit',sans-serif;font-weight:800;font-size:1.05rem;color:#0F172A;">StudentOS <span style="color:#7C3AED;">AI</span></span>
        </div>
        """, unsafe_allow_html=True)
        
    with col_search:
        search_query = st.text_input("Search", placeholder="🔍 Search everything... (⌘ K)", label_visibility="collapsed")
        if search_query:
            st.toast(f"Searching for: {search_query}", icon="🔍")
            
    with col_space:
        pass
        
    with col_weather:
        st.markdown(f"""
        <div style="text-align:right;">
            <div style="font-size:0.72rem;color:#94A3B8;font-weight:500;">{date_str}</div>
            <div style="font-size:0.9rem;font-weight:700;color:#0F172A;">{time_str} ☀️ 28°C</div>
        </div>
        """, unsafe_allow_html=True)
        
    with col_notif:
        with st.popover("🔔"):
            st.markdown("**Notifications (3)**")
            st.info("Your AI Tutor session is ready!")
            st.warning("Quiz due tomorrow in Data Structures.")
            st.success("You earned a 12-day streak!")
            
    with col_status:
        st.markdown("""
        <div style="display:flex;align-items:center;gap:6px;background:rgba(34,197,94,0.08);border:1px solid rgba(34,197,94,0.2);border-radius:10px;padding:6px 10px; height:100%; justify-content:center; margin-top:2px;">
            <div style="width:8px;height:8px;border-radius:50%;background:#22C55E;animation:pulse-green 2s infinite;"></div>
            <span style="font-size:0.75rem;font-weight:600;color:#16A34A;">AI Online</span>
        </div>
        """, unsafe_allow_html=True)
        
    with col_profile:
        st.markdown(f"""
        <div style="display:flex;align-items:center;gap:8px;background:rgba(255,255,255,0.8);border:1px solid rgba(0,0,0,0.07);border-radius:12px;padding:4px 10px; cursor:pointer;">
            <div style="width:28px;height:28px;border-radius:50%;background:linear-gradient(135deg,#7C3AED,#2563EB);display:flex;align-items:center;justify-content:center;font-size:0.8rem;font-weight:800;color:white;">{name[0]}</div>
            <div>
                <div style="font-size:0.8rem;font-weight:700;color:#0F172A;line-height:1.1;">{name}</div>
                <div style="font-size:0.6rem;color:#94A3B8;">Student</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
