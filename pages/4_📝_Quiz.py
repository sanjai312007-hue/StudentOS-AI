import streamlit as st
import time
from components.styles import apply_custom_styles
from data.mock_data import QUIZ_QUESTIONS

from components.sidebar import render_sidebar
from components.navbar import render_navbar

st.set_page_config(
    page_title="Quiz Generator | StudentOS AI",
    page_icon="📝",
    layout="wide"
)

apply_custom_styles()

if "authenticated" not in st.session_state or not st.session_state.authenticated:
    st.warning("🔒 Please authenticate first on the homepage.")
    st.stop()

# Initialize session state variables for active quizzes
if "quiz_active" not in st.session_state:
    st.session_state.quiz_active = False
if "quiz_questions" not in st.session_state:
    st.session_state.quiz_questions = []
if "current_question_idx" not in st.session_state:
    st.session_state.current_question_idx = 0
if "user_answers" not in st.session_state:
    st.session_state.user_answers = {}
if "quiz_results" not in st.session_state:
    st.session_state.quiz_results = None

# ── Floating Navbar ──────────────────────────────────────────────
render_navbar()

# ─── Layout: Sidebar (col_nav) & Main Content (col_content) ─────
col_nav, col_content = st.columns([1.1, 4])

with col_nav:
    render_sidebar(active_page="Quiz Generator")

with col_content:
    # Header Section
    st.markdown("""
<div style="margin-top: 10px; margin-bottom: 25px;">
<h1>📝 Quiz <span class="gradient-text">Generator</span></h1>
<p style="color: #64748B; font-size: 1rem; margin-top: 0;">Generate custom quizzes from your course modules and evaluate your exam preparedness</p>
</div>
""", unsafe_allow_html=True)

    if not st.session_state.quiz_active and not st.session_state.quiz_results:
        # ─── Configuration Panel ──────────────────────────────────────────
        st.markdown("### Setup Quiz Parameters")
        
        col1, col2 = st.columns([1, 1])
        
        with col1:
            subject = st.selectbox("Select Target Course/Topic", list(QUIZ_QUESTIONS.keys()))
            num_questions = st.slider("Number of Questions", min_value=3, max_value=10, value=5)
        with col2:
            difficulty = st.selectbox("Topic Difficulty Preference", ["All Levels", "Beginner", "Intermediate", "Advanced"])
            q_format = st.multiselect("Allowed Formats", ["Multiple Choice (MCQ)", "True/False", "Short Answer"], default=["Multiple Choice (MCQ)"])
            
        st.markdown("<div style='margin-top: 20px;'></div>", unsafe_allow_html=True)
        if st.button("Generate Assessment"):
            with st.spinner("Analyzing course notes & generating questions..."):
                time.sleep(1.5)
                # Filter and prepare questions
                all_qs = QUIZ_QUESTIONS[subject]
                if difficulty != "All Levels":
                    all_qs = [q for q in all_qs if q["difficulty"] == difficulty]
                
                # Fallback if no questions match
                if not all_qs:
                    all_qs = QUIZ_QUESTIONS[subject]
                    
                st.session_state.quiz_questions = all_qs[:num_questions]
                st.session_state.quiz_active = True
                st.session_state.current_question_idx = 0
                st.session_state.user_answers = {}
                st.session_state.quiz_results = None
                st.rerun()

    elif st.session_state.quiz_active:
        # ─── Quiz Session in Progress ─────────────────────────────────────
        questions = st.session_state.quiz_questions
        idx = st.session_state.current_question_idx
        q = questions[idx]
        
        # Progress indicator
        progress = (idx + 1) / len(questions)
        st.progress(progress)
        st.markdown(f"**Question {idx + 1} of {len(questions)}** • Category: `{q['difficulty']}`")
        
        # Question Card
        st.markdown(f"""
<div class="glass-card" style="margin-top: 15px; min-height: 120px;">
<h3 style="color: #ffffff; margin-top: 0; line-height: 1.4;">{q['question']}</h3>
</div>
""", unsafe_allow_html=True)
        
        # Options selection
        # Store answers as a value, default to empty
        selected_option = st.radio(
            "Choose the correct option:",
            q["options"],
            index=st.session_state.user_answers.get(idx, None),
            key=f"q_{idx}_radio"
        )
        
        # Update selected answer in state
        if selected_option is not None:
            option_idx = q["options"].index(selected_option)
            st.session_state.user_answers[idx] = option_idx
            
        st.markdown("<div style='margin-top: 30px;'></div>", unsafe_allow_html=True)
        
        nav_col1, nav_col2, nav_col3 = st.columns([1, 1, 1])
        
        with nav_col1:
            if idx > 0:
                if st.button("Previous Question"):
                    st.session_state.current_question_idx -= 1
                    st.rerun()
                    
        with nav_col3:
            if idx < len(questions) - 1:
                if st.button("Next Question"):
                    st.session_state.current_question_idx += 1
                    st.rerun()
            else:
                if st.button("Submit Assessment", type="primary"):
                    # Complete the quiz
                    score = sum(1 for i, ans in st.session_state.user_answers.items() if ans == questions[i]["answer"])
                    st.session_state.quiz_results = {
                        "score": score,
                        "total": len(questions),
                        "percentage": int((score / len(questions)) * 100)
                    }
                    st.session_state.quiz_active = False
                    st.rerun()

    elif st.session_state.quiz_results:
        # ─── Results Summary ──────────────────────────────────────────────
        results = st.session_state.quiz_results
        questions = st.session_state.quiz_questions
        
        st.markdown("### Assessment Scorecard")
        
        col1, col2 = st.columns([1, 2])
        with col1:
            st.markdown(f"""
<div class="glass-card" style="text-align: center; padding: 40px 20px;">
<div class="stat-label" style="font-size: 1.1rem;">YOUR SCORE</div>
<div class="stat-val" style="font-size: 4rem; margin: 15px 0;">{results['score']}/{results['total']}</div>
<div style="font-size: 1.5rem; font-weight: 700; color: #a78bfa; margin-bottom: 20px;">{results['percentage']}%</div>
</div>
""", unsafe_allow_html=True)
            
            if st.button("Take Another Quiz", type="primary"):
                st.session_state.quiz_results = None
                st.session_state.quiz_questions = []
                st.session_state.quiz_active = False
                st.rerun()
                
        with col2:
            st.markdown("#### Comprehensive Question Breakdown")
            
            for i, q in enumerate(questions):
                user_ans_idx = st.session_state.user_answers.get(i, -1)
                correct_ans_idx = q["answer"]
                
                is_correct = user_ans_idx == correct_ans_idx
                status_text = "✅ Correct" if is_correct else "❌ Incorrect"
                border_color = "#10b981" if is_correct else "#ef4444"
                
                user_ans_val = q["options"][user_ans_idx] if user_ans_idx != -1 else "No Answer"
                correct_ans_val = q["options"][correct_ans_idx]
                
                st.markdown(f"""
<div class="glass-card" style="border-left: 5px solid {border_color}; padding: 18px; margin-bottom: 12px;">
<div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
<span style="font-weight: 600;">Question {i+1}</span>
<span style="color: {border_color}; font-weight: 700;">{status_text}</span>
</div>
<p style="margin: 0 0 10px 0; color: #ffffff; font-size: 0.95rem;">{q['question']}</p>
<div style="font-size: 0.85rem; color: #94a3b8; margin-bottom: 8px;">
<div>Your Answer: <span style="color: {'#ffffff' if is_correct else '#ff6b6b'}">{user_ans_val}</span></div>
<div>Correct Answer: <span style="color: #10b981">{correct_ans_val}</span></div>
</div>
<div style="background: rgba(255,255,255,0.03); padding: 10px; border-radius: 6px; font-size: 0.82rem; line-height: 1.4; color: #cbd5e1;">
💡 <b>Explanation:</b> {q['explanation']}
</div>
</div>
""", unsafe_allow_html=True)

