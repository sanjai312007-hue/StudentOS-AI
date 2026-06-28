import streamlit as st
import json
import google.generativeai as genai
from components.styles import apply_custom_styles
from data.mock_data import AI_TUTOR_RESPONSES

# Configure Gemini with the provided API key
genai.configure(import os

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY"))

from components.sidebar import render_sidebar
from components.navbar import render_navbar

st.set_page_config(
    page_title="AI Tutor | StudentOS AI",
    page_icon="🧠",
    layout="wide"
)

apply_custom_styles()

if "authenticated" not in st.session_state or not st.session_state.authenticated:
    st.warning("🔒 Please authenticate first on the homepage.")
    st.stop()

# Initialize tutor chat history
if "tutor_chat_history" not in st.session_state:
    st.session_state.tutor_chat_history = [
        {"role": "assistant", "content": "Hello! I am your personalized StudentOS AI Tutor. Select a subject and difficulty, then ask me to explain any concept!", "data": None}
    ]

# ── Floating Navbar ──────────────────────────────────────────────
render_navbar()

# ─── Layout: Sidebar (col_nav) & Main Content (col_content) ─────
col_nav, col_content = st.columns([1.1, 4])

with col_nav:
    render_sidebar(active_page="AI Workspace")

with col_content:
    # Header Section
    st.markdown("""
<div style="margin-top: 10px; margin-bottom: 25px;">
<h1>🧠 Personal <span class="gradient-text">AI Tutor</span></h1>
<p style="color: #64748B; font-size: 1rem; margin-top: 0;">Get customized, detailed academic explanations, code snippets, and practice questions</p>
</div>
""", unsafe_allow_html=True)

    # Configuration Panel (Sidebar or top columns)
    config_col1, config_col2, config_col3 = st.columns([1, 1, 1.5])
    with config_col1:
        subject = st.selectbox("Select Subject Domain", ["General CS", "Python", "DBMS", "Operating Systems", "Machine Learning", "Data Structures"])
    with config_col2:
        difficulty = st.selectbox("Difficulty Level", ["Beginner", "Intermediate", "Advanced"])
    with config_col3:
        tutor_focus = st.multiselect("Response Focus", ["Definitions", "Code Examples", "Time Complexity", "Interview Questions"], default=["Definitions", "Code Examples", "Time Complexity"])

    st.markdown("---")

    # Split screen: Chat History on left, structured response tabs on right (advanced visual layout)
    chat_col, response_col = st.columns([1.1, 1])

    with chat_col:
        st.markdown("### 💬 Classroom Chat")
        
        # Message container
        for msg in st.session_state.tutor_chat_history:
            if msg["role"] == "user":
                st.markdown(f"""
<div style="background: rgba(108, 99, 255, 0.12); border-left: 4px solid #6C63FF; padding: 12px 16px; border-radius: 8px; margin-bottom: 12px;">
<b style="color: #a78bfa;">You:</b> {msg['content']}
</div>
""", unsafe_allow_html=True)
            else:
                st.markdown(f"""
<div style="background: rgba(255, 255, 255, 0.04); border-left: 4px solid #94a3b8; padding: 12px 16px; border-radius: 8px; margin-bottom: 12px;">
<b style="color: #cbd5e1;">AI Tutor:</b> {msg['content']}
</div>
""", unsafe_allow_html=True)
                
        # Form input
        with st.form("tutor_input_form", clear_on_submit=True):
            user_query = st.text_input("Ask a question (e.g. explain Binary Search)", placeholder="Explain binary search...")
            submit = st.form_submit_button("Ask Tutor")
            
            if submit and user_query:
                # Append user msg
                st.session_state.tutor_chat_history.append({"role": "user", "content": user_query})
                
                with st.spinner("🧠 AI Tutor is thinking..."):
                    try:
                        model = genai.GenerativeModel('gemini-2.5-flash')
                        prompt = f"""
                        You are a strict, highly capable AI Tutor for a student learning {subject}.
                        The difficulty level is {difficulty}. Focus areas requested: {tutor_focus}.
                        
                        Explain the following concept or answer the question: "{user_query}"
                        
                        Return a valid JSON object exactly in this format (no markdown code blocks, just JSON text):
                        {{
                            "definition": "Detailed explanation with academic accuracy...",
                            "example": "A scenario or example illustrating the concept...",
                            "code": "```python\\n# Provide code if applicable, else empty string\\n```",
                            "complexity": "Markdown table of time/space complexity if applicable, else empty string",
                            "interview_questions": ["Question 1", "Question 2"]
                        }}
                        """
                        response = model.generate_content(prompt)
                        
                        response_text = response.text.strip()
                        if response_text.startswith("```json"):
                            response_text = response_text[7:]
                        elif response_text.startswith("```"):
                            response_text = response_text[3:]
                        if response_text.endswith("```"):
                            response_text = response_text[:-3]
                            
                        response_data = json.loads(response_text)
                        
                        ai_content = f"Here is the breakdown for **{user_query}** under **{difficulty}** level. See structured details on the right tab!"
                        st.session_state.tutor_chat_history.append({"role": "assistant", "content": ai_content, "data": response_data})
                    except Exception as e:
                        st.error(f"Error communicating with AI Engine: {e}")
                        
                st.rerun()

    with response_col:
        st.markdown("### 📋 Structured Lecture Notes")
        
        # Get last assistant message data if any
        last_assistant_msg = next((msg for msg in reversed(st.session_state.tutor_chat_history) if msg["role"] == "assistant" and msg.get("data")), None)
        
        if last_assistant_msg and last_assistant_msg.get("data"):
            data = last_assistant_msg["data"]
            
            tab1, tab2, tab3, tab4 = st.tabs(["📖 Concept Overview", "💻 Practical Implementation", "📊 Complexity & Metrics", "🎤 Placement Prep"])
            
            with tab1:
                st.markdown(data["definition"])
                st.markdown("#### Scenario / Example")
                st.markdown(data["example"])
                
                # Interactive Voice Synthesis (Text-To-Speech) Button
                text_to_speak = data["definition"].replace("`", "").replace("*", "")
                tts_html = f"""
                <div style="margin-top: 15px;">
                    <button onclick="speakText()" style="
                        background: linear-gradient(135deg, #a78bfa 0%, #6c63ff 100%);
                        color: white;
                        border: none;
                        padding: 8px 16px;
                        border-radius: 8px;
                        font-weight: bold;
                        cursor: pointer;
                        box-shadow: 0 4px 15px rgba(108, 99, 255, 0.3);
                    ">🔊 Read Aloud (Voice Assistant)</button>
                    <button onclick="window.speechSynthesis.cancel()" style="
                        background: rgba(239, 68, 68, 0.15);
                        color: #ef4444;
                        border: 1px solid rgba(239, 68, 68, 0.3);
                        padding: 8px 16px;
                        border-radius: 8px;
                        font-weight: bold;
                        cursor: pointer;
                        margin-left: 10px;
                    ">⏹️ Stop</button>
                </div>
                <script>
                    function speakText() {{
                        window.speechSynthesis.cancel();
                        var msg = new SpeechSynthesisUtterance("{text_to_speak}");
                        msg.rate = 1.0;
                        window.speechSynthesis.speak(msg);
                    }}
                </script>
                """
                st.components.v1.html(tts_html, height=60)
                
            with tab2:
                if data["code"]:
                    st.markdown(data["code"])
                else:
                    st.info("No code snippet available for this topic.")
                    
            with tab3:
                if data["complexity"]:
                    st.markdown(data["complexity"])
                else:
                    st.info("Complexity details not applicable or not found.")
                    
            with tab4:
                if data["interview_questions"]:
                    st.markdown("#### Commonly Asked Interview Questions:")
                    for q in data["interview_questions"]:
                        st.write(f"- {q}")
                else:
                    st.info("No placement prep questions currently listed.")
        else:
            st.info("💡 Ask a question in the chat on the left to generate structured notes here.")

    # Interactive Speech Recognition (Speech-To-Text) Button for User Query
    st.markdown("### 🗣️ Voice Input Control Panel")
    sttr_html = """
    <div style="background: rgba(26, 29, 41, 0.45); border: 1px solid rgba(255,255,255,0.08); padding: 18px; border-radius: 12px; margin-top: 15px;">
        <p style="margin: 0 0 10px 0; color: #a78bfa; font-weight: 600; font-size: 0.9rem;">Tap mic and ask "Explain binary search":</p>
        <button onclick="startDictation()" style="
            background: linear-gradient(135deg, #4ecdc4 0%, #20bf6b 100%);
            color: white;
            border: none;
            padding: 10px 20px;
            border-radius: 8px;
            font-weight: bold;
            cursor: pointer;
            box-shadow: 0 4px 15px rgba(78, 205, 196, 0.3);
        ">🎤 Tap to Speak Query</button>
        <span id="speech-status" style="margin-left: 15px; font-size: 0.9rem; color: #94a3b8;">Idle</span>
    </div>
    <script>
        function startDictation() {
            if (window.hasOwnProperty('webkitSpeechRecognition')) {
                var recognition = new webkitSpeechRecognition();
                recognition.continuous = false;
                recognition.interimResults = false;
                recognition.lang = "en-US";
                
                document.getElementById('speech-status').innerText = "Listening...";
                recognition.start();
                
                recognition.onresult = function(e) {
                    var text = e.results[0][0].transcript;
                    recognition.stop();
                    document.getElementById('speech-status').innerText = "Recognized: " + text;
                    
                    // Set the value of the Streamlit query input if possible, or display warning
                    alert("Speech recognized: '" + text + "'. Paste this in the query box above and ask.");
                };
                
                recognition.onerror = function(e) {
                    recognition.stop();
                    document.getElementById('speech-status').innerText = "Error encountered.";
                };
            } else {
                alert("Web Speech API not supported in this browser. Please use Chrome/Edge.");
            }
        }
    </script>
    """
    st.components.v1.html(sttr_html, height=120)


