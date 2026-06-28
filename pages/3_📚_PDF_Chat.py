import streamlit as st
import time
import PyPDF2
import google.generativeai as genai
import json
from components.styles import apply_custom_styles

from components.sidebar import render_sidebar
from components.navbar import render_navbar

genai.configure(import os

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY"))

st.set_page_config(
    page_title="PDF Chat RAG | StudentOS AI",
    page_icon="📚",
    layout="wide"
)

apply_custom_styles()

if "authenticated" not in st.session_state or not st.session_state.authenticated:
    st.warning("🔒 Please authenticate first on the homepage.")
    st.stop()

# Initialize PDF lists and histories
if "pdf_files" not in st.session_state:
    st.session_state.pdf_files = []
if "pdf_texts" not in st.session_state:
    st.session_state.pdf_texts = {}
if "pdf_chat_history" not in st.session_state:
    st.session_state.pdf_chat_history = []

# ── Floating Navbar ──────────────────────────────────────────────
render_navbar()

# ─── Layout: Sidebar (col_nav) & Main Content (col_content) ─────
col_nav, col_content = st.columns([1.1, 4])

with col_nav:
    render_sidebar(active_page="PDF Chat (RAG)")

with col_content:
    # Header Section
    st.markdown("""
<div style="margin-top: 10px; margin-bottom: 25px;">
<h1>📚 Chat with PDFs <span class="gradient-text">(RAG)</span></h1>
<p style="color: #64748B; font-size: 1rem; margin-top: 0;">Upload lecture slide notes, textbooks, and syllabus files to query information grounded directly in source files</p>
</div>
""", unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1.8])

    with col1:
        st.markdown("### 📥 Document Ingestion")
        
        # Drag and Drop File Ingester
        uploaded_file = st.file_uploader("Upload PDF or Study Material", type=["pdf"])
        if uploaded_file:
            if uploaded_file.name not in [f["name"] for f in st.session_state.pdf_files]:
                new_file = {"name": uploaded_file.name, "size": f"{uploaded_file.size/1000:.1f} KB", "status": "Processing", "chunks": 0}
                st.session_state.pdf_files.append(new_file)
                st.toast(f"Uploading and extracting {uploaded_file.name}...")
                
                try:
                    pdf_reader = PyPDF2.PdfReader(uploaded_file)
                    text = ""
                    for page in pdf_reader.pages:
                        page_text = page.extract_text()
                        if page_text:
                            text += page_text + "\n"
                    
                    st.session_state.pdf_texts[uploaded_file.name] = text
                    
                    for file in st.session_state.pdf_files:
                        if file["name"] == uploaded_file.name:
                            file["status"] = "Ready"
                            file["chunks"] = len(text) // 500  # Estimate chunks based on length
                    st.toast("Document extracted & stored! ✅")
                except Exception as e:
                    st.error(f"Error parsing PDF: {e}")
                    
                st.rerun()

        # Active Documents List
        st.markdown("#### Loaded Ingestion Context")
        if st.session_state.pdf_files:
            for doc in st.session_state.pdf_files:
                badge_color = "#10b981" if doc["status"] == "Ready" else "#f59e0b"
                st.markdown(f"""
<div class="glass-card" style="padding: 12px 16px; margin-bottom: 10px;">
<div style="display: flex; justify-content: space-between; align-items: center;">
<span style="font-weight: 600; font-size: 0.95rem;">📄 {doc['name']}</span>
<span class="badge" style="background: rgba({badge_color}, 0.15); color: {badge_color}; border: 1px solid rgba({badge_color}, 0.3);">{doc['status']}</span>
</div>
<div style="display: flex; justify-content: space-between; font-size: 0.75rem; color: #94a3b8; margin-top: 8px;">
<span>Size: {doc['size']}</span>
<span>Vector Chunks: {doc['chunks']}</span>
</div>
</div>
""", unsafe_allow_html=True)
        else:
            st.info("No documents ingested yet. Upload a syllabus or slides file to start querying.")

    with col2:
        st.markdown("### 💬 Semantic RAG Chat")
        
        # Active query targets
        selected_docs = st.multiselect(
            "Direct queries to specific files:",
            [doc["name"] for doc in st.session_state.pdf_files],
            default=[doc["name"] for doc in st.session_state.pdf_files]
        )
        
        # Conversation bubble list
        chat_container = st.container(height=360)
        with chat_container:
            if not st.session_state.pdf_chat_history:
                st.info("Ask any query grounded inside the selected PDFs. Example: 'Explain deadlock conditions'")
            for msg in st.session_state.pdf_chat_history:
                if msg["role"] == "user":
                    st.markdown(f"""
<div style="background: rgba(108, 99, 255, 0.12); border-left: 4px solid #6C63FF; padding: 12px 16px; border-radius: 8px; margin-bottom: 12px;">
<b style="color: #a78bfa;">You:</b> {msg['content']}
</div>
""", unsafe_allow_html=True)
                else:
                    st.markdown(f"""
<div style="background: rgba(255, 255, 255, 0.04); border-left: 4px solid #94a3b8; padding: 12px 16px; border-radius: 8px; margin-bottom: 12px;">
<b style="color: #cbd5e1;">RAG Assistant:</b> {msg['content']}
<div style="margin-top: 10px; border-top: 1px solid rgba(255,255,255,0.05); padding-top: 6px; font-size: 0.75rem; color: #a78bfa;">
🔍 Source Chunks: <b>{msg.get('source', 'General Knowledge')}</b>
</div>
</div>
""", unsafe_allow_html=True)

        # Input zone
        with st.form("rag_chat_form", clear_on_submit=True):
            query = st.text_input("Enter your document question:")
            submit = st.form_submit_button("Semantic Search & Answer")
            
            if submit and query:
                st.session_state.pdf_chat_history.append({"role": "user", "content": query})
                
                if not selected_docs:
                    st.error("Please select at least one document to query.")
                else:
                    with st.spinner("Retrieving answers from your documents..."):
                        try:
                            # Construct context from selected documents
                            context_text = ""
                            for doc_name in selected_docs:
                                if doc_name in st.session_state.pdf_texts:
                                    context_text += f"--- Document: {doc_name} ---\n"
                                    context_text += st.session_state.pdf_texts[doc_name] + "\n\n"
                                    
                            model = genai.GenerativeModel('gemini-2.5-flash')
                            prompt = f"""
                            You are a helpful academic AI assistant that answers questions based ONLY on the provided documents.
                            
                            Here are the extracted documents context:
                            {context_text}
                            
                            Question: {query}
                            
                            If the answer is not in the context, explicitly say that you cannot find it in the provided documents. 
                            Also specify which document provided the answer if possible.
                            """
                            response = model.generate_content(prompt)
                            
                            source = ", ".join(selected_docs)
                            st.session_state.pdf_chat_history.append({
                                "role": "assistant",
                                "content": response.text.strip(),
                                "source": source
                            })
                        except Exception as e:
                            st.error(f"Error analyzing documents: {e}")
                
                st.rerun()
