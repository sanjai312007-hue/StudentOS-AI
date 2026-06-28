import streamlit as st
import time
from components.styles import apply_custom_styles
from data.mock_data import STUDENT_PROFILE

st.set_page_config(
    page_title="StudentOS AI — AI Learning OS",
    page_icon="🏆",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Apply global premium glassmorphic light theme
apply_custom_styles()

# Initialize session state variables
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
if "user_profile" not in st.session_state:
    st.session_state.user_profile = STUDENT_PROFILE.copy()

# Aurora background elements
st.markdown("""
<div class="aurora-blob-1"></div>
<div class="aurora-blob-2"></div>
<div class="aurora-blob-3"></div>
""", unsafe_allow_html=True)

def login_user(email, password):
    if email == "sanjai@studentos.ai" and password == "password":
        st.session_state.authenticated = True
        st.session_state.user_profile = STUDENT_PROFILE.copy()
        st.success("Successfully Authenticated! Loading Workspace...")
        time.sleep(1)
        st.switch_page("pages/1_📊_Dashboard.py")
    else:
        st.error("Invalid credentials. Try: sanjai@studentos.ai / password")

def register_user(name, email, college, dep, goal):
    st.session_state.user_profile.update({
        "name": name,
        "email": email,
        "college": college,
        "department": dep,
        "career_goal": goal
    })
    st.session_state.authenticated = True
    st.success("Account created successfully! Loading Workspace...")
    time.sleep(1)
    st.switch_page("pages/1_📊_Dashboard.py")

if not st.session_state.authenticated:
    # ─── Auth Landing Page (Split Screen Design) ─────────────────────
    col1, col2 = st.columns([1.2, 1])
    
    with col1:
        st.markdown("""
<div style="padding-right: 40px; margin-top: 50px;">
<div style="display: flex; align-items: center; gap: 8px; margin-bottom: 24px;">
<div style="
width: 38px; height: 38px; border-radius: 10px;
background: linear-gradient(135deg, #7C3AED, #2563EB);
display: flex; align-items: center; justify-content: center;
font-size: 1.1rem; box-shadow: 0 4px 12px rgba(124,58,237,0.3);
">🎓</div>
<span style="font-family: 'Outfit', sans-serif; font-weight: 800; font-size: 1.25rem; color: #0F172A; letter-spacing: -0.02em;">StudentOS <span style="color: #7C3AED;">AI</span></span>
</div>
<h1 style="font-size: 3.8rem; line-height: 1.05; margin-bottom: 20px; font-weight: 800; font-family: 'Outfit', sans-serif;">
The Ultimate <span class="gradient-text">AI Learning OS</span> for Students
</h1>
<p style="font-size: 1.15rem; color: #64748B; margin-bottom: 35px; line-height: 1.6; font-family: 'Inter', sans-serif;">
Experience a campus workspace like no other. Built with next-generation RAG models, custom quiz generation pipelines, spaced-repetition active recall flashcards, and professional career analytics.
</p>
</div>
""", unsafe_allow_html=True)
        
        # Display Feature Grid in Left Panel
        f_col1, f_col2 = st.columns(2)
        with f_col1:
            st.markdown("""
<div class="glass-card" style="padding: 20px; min-height: 150px;">
<h4 style="color: #7C3AED; margin-top: 0; display: flex; align-items: center; gap: 8px;">📚 PDF Chat (RAG)</h4>
<p style="font-size: 0.85rem; color: #64748B; margin-bottom: 0; line-height: 1.5;">Instant context retrieval on textbook chapters, research drafts, and syllabus files.</p>
</div>
<div class="glass-card" style="padding: 20px; min-height: 150px;">
<h4 style="color: #06B6D4; margin-top: 0; display: flex; align-items: center; gap: 8px;">🃏 Smart Flashcards</h4>
<p style="font-size: 0.85rem; color: #64748B; margin-bottom: 0; line-height: 1.5;">3D interactive spaced-repetition flashcards generated automatically from your class notes.</p>
</div>
""", unsafe_allow_html=True)
        with f_col2:
            st.markdown("""
<div class="glass-card" style="padding: 20px; min-height: 150px;">
<h4 style="color: #2563EB; margin-top: 0; display: flex; align-items: center; gap: 8px;">🧠 Personal AI Tutor</h4>
<p style="font-size: 0.85rem; color: #64748B; margin-bottom: 0; line-height: 1.5;">Interactive code walk-throughs, custom explanation rubrics, and dynamic voice dictation.</p>
</div>
<div class="glass-card" style="padding: 20px; min-height: 150px;">
<h4 style="color: #22C55E; margin-top: 0; display: flex; align-items: center; gap: 8px;">📅 Adaptive Planner</h4>
<p style="font-size: 0.85rem; color: #64748B; margin-bottom: 0; line-height: 1.5;">Intelligent study calendar that reschedules tasks automatically as exam timelines change.</p>
</div>
""", unsafe_allow_html=True)
            
    with col2:
        st.markdown('<div class="glass-card" style="margin-top: 50px; padding: 36px;">', unsafe_allow_html=True)
        
        # Toggle Auth Mode
        mode = st.radio("Access Academic OS", ["Login", "Register", "Recovery"], horizontal=True, label_visibility="collapsed")
        
        st.markdown("<div style='margin-top: 20px;'></div>", unsafe_allow_html=True)
        
        if mode == "Login":
            st.markdown("<h2 style='font-size: 1.6rem; margin-bottom: 6px; font-weight: 700;'>Welcome Back</h2>", unsafe_allow_html=True)
            st.markdown("<p style='font-size: 0.85rem; color: #64748B; margin-bottom: 24px;'>Access your personalized learning suite</p>", unsafe_allow_html=True)
            
            email = st.text_input("Academic Email", value="sanjai@studentos.ai")
            password = st.text_input("Password", type="password", value="password")
            
            st.markdown("<div style='margin-top: 24px;'></div>", unsafe_allow_html=True)
            if st.button("Authenticate Workspace"):
                login_user(email, password)
                
            st.markdown("""
<div style="text-align: center; margin-top: 24px; padding: 12px; border-radius: 12px; background: rgba(124, 58, 237, 0.05); border: 1px solid rgba(124, 58, 237, 0.1); color: #7C3AED; font-size: 0.8rem; font-weight: 500;">
💡 Demo Credentials: <b>sanjai@studentos.ai</b> / <b>password</b>
</div>
""", unsafe_allow_html=True)
            
        elif mode == "Register":
            st.markdown("<h2 style='font-size: 1.6rem; margin-bottom: 6px; font-weight: 700;'>Create Account</h2>", unsafe_allow_html=True)
            st.markdown("<p style='font-size: 0.85rem; color: #64748B; margin-bottom: 24px;'>Join the next-generation academic network</p>", unsafe_allow_html=True)
            
            name = st.text_input("Full Name", placeholder="e.g. Sanjai R")
            email = st.text_input("Academic Email", placeholder="e.g. sanjai@college.edu")
            college = st.text_input("College / University", placeholder="e.g. Anna University")
            col_dep, col_goal = st.columns(2)
            with col_dep:
                dep = st.text_input("Department", placeholder="e.g. CSE")
            with col_goal:
                goal = st.text_input("Career Goal", placeholder="e.g. AI Engineer")
            
            st.markdown("<div style='margin-top: 24px;'></div>", unsafe_allow_html=True)
            if st.button("Register & Ingest Profile"):
                if name and email:
                    register_user(name, email, college, dep, goal)
                else:
                    st.error("Please provide name and academic email address.")
                    
        elif mode == "Recovery":
            st.markdown("<h2 style='font-size: 1.6rem; margin-bottom: 6px; font-weight: 700;'>Account Recovery</h2>", unsafe_allow_html=True)
            st.markdown("<p style='font-size: 0.85rem; color: #64748B; margin-bottom: 24px;'>Retrieve access to your study workspace</p>", unsafe_allow_html=True)
            
            email = st.text_input("Registered Email Address", placeholder="e.g. sanjai@studentos.ai")
            st.markdown("<div style='margin-top: 24px;'></div>", unsafe_allow_html=True)
            if st.button("Send Recovery Token"):
                st.info(f"Verification token sent to: {email}")
                
        st.markdown('</div>', unsafe_allow_html=True)

else:
    st.markdown("""
<div style="text-align: center; margin-top: 100px;">
<div style="width: 80px; height: 80px; border-radius: 20px;
background: linear-gradient(135deg, #7C3AED, #2563EB);
display: flex; align-items: center; justify-content: center;
font-size: 2.2rem; box-shadow: 0 8px 24px rgba(124,58,237,0.3);
margin: 0 auto 30px;
">🎓</div>
<h1 style="font-size: 3.5rem; font-weight: 800; font-family: 'Outfit', sans-serif;"><span class="gradient-text">OS Workspace Loaded</span> 🚀</h1>
<p style="font-size: 1.2rem; color: #64748B; margin-top: 20px; max-width: 600px; margin-left: auto; margin-right: auto; line-height: 1.6;">
Welcome back, <b>{name}</b>. Your StudentOS database, chat history, and academic planner states have been verified.
</p>
</div>
""".format(name=st.session_state.user_profile["name"]), unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1.5, 2, 1.5])
    with col2:
        st.markdown("<div style='margin-top: 30px;'></div>", unsafe_allow_html=True)
        if st.button("Launch Dashboard", type="primary"):
            st.switch_page("pages/1_📊_Dashboard.py")
        st.markdown("<div style='margin-top: 10px;'></div>", unsafe_allow_html=True)
        if st.button("Disconnect Session", type="secondary"):
            st.session_state.authenticated = False
            st.rerun()
