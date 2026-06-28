import streamlit as st
from components.styles import apply_custom_styles
from components.sidebar import render_sidebar
from components.navbar import render_navbar
from data.mock_data import FLASHCARD_DECKS

st.set_page_config(
    page_title="Smart Flashcards | StudentOS AI",
    page_icon="🃏",
    layout="wide"
)

apply_custom_styles()

if "authenticated" not in st.session_state or not st.session_state.authenticated:
    st.warning("🔒 Please authenticate first on the homepage.")
    st.stop()

# Initialize deck state variables
if "selected_deck" not in st.session_state:
    st.session_state.selected_deck = list(FLASHCARD_DECKS.keys())[0]
if "card_index" not in st.session_state:
    st.session_state.card_index = 0
if "is_flipped" not in st.session_state:
    st.session_state.is_flipped = False
if "mastered_count" not in st.session_state:
    st.session_state.mastered_count = {}

# ── Floating Navbar ──────────────────────────────────────────────
render_navbar()

# ─── Layout: Sidebar (col_nav) & Main Content (col_content) ─────
col_nav, col_content = st.columns([1.1, 4])

with col_nav:
    render_sidebar(active_page="Flashcards")

with col_content:
    # Header Section
    st.markdown("""
<div style="margin-top: 10px; margin-bottom: 25px;">
<h1>🃏 Smart <span class="gradient-text">Flashcards</span></h1>
<p style="color: #64748B; font-size: 1rem; margin-top: 0;">Revise critical concepts, formulas, and terminology using spaced-repetition active recall decks</p>
</div>
""", unsafe_allow_html=True)

    # Layout Setup
    col1, col2 = st.columns([1, 2])

    with col1:
        st.markdown("### Browse Flashcard Decks")
        
        # Deck Selector
        chosen_deck = st.selectbox(
            "Choose Flashcard Subject",
            list(FLASHCARD_DECKS.keys()),
            index=list(FLASHCARD_DECKS.keys()).index(st.session_state.selected_deck)
        )
        
        if chosen_deck != st.session_state.selected_deck:
            st.session_state.selected_deck = chosen_deck
            st.session_state.card_index = 0
            st.session_state.is_flipped = False
            st.rerun()
            
        deck = FLASHCARD_DECKS[st.session_state.selected_deck]
        deck_name = st.session_state.selected_deck
        
        # Initialize mastery count for deck if not present
        if deck_name not in st.session_state.mastered_count:
            st.session_state.mastered_count[deck_name] = [False] * len(deck)
            
        mastered_list = st.session_state.mastered_count[deck_name]
        num_mastered = sum(1 for m in mastered_list if m)
        
        st.markdown(f"""
<div class="glass-card" style="margin-top: 15px;">
<div class="stat-label">DECK SUMMARY</div>
<h4 style="margin: 8px 0; color: #ffffff;">{deck_name}</h4>
<div style="display: flex; justify-content: space-between; font-size: 0.85rem; color: #94a3b8; margin-top: 12px;">
<span>Total Cards: {len(deck)}</span>
<span style="color: #10b981;">Mastered: {num_mastered}</span>
</div>
<div style="margin-top: 10px; background: rgba(255,255,255,0.05); height: 6px; border-radius: 3px; overflow: hidden;">
<div style="background: #10b981; width: {int((num_mastered/len(deck))*100)}%; height: 100%;"></div>
</div>
</div>
""", unsafe_allow_html=True)
        
        if st.button("Reset Deck Mastery"):
            st.session_state.mastered_count[deck_name] = [False] * len(deck)
            st.session_state.card_index = 0
            st.session_state.is_flipped = False
            st.rerun()

    with col2:
        deck = FLASHCARD_DECKS[st.session_state.selected_deck]
        idx = st.session_state.card_index
        card = deck[idx]
        deck_name = st.session_state.selected_deck
        
        st.markdown(f"### Study Mode ({idx + 1} of {len(deck)})")
        
        # 3D interactive flip simulation using container and markdown custom styling
        face_text = card["back"] if st.session_state.is_flipped else card["front"]
        bg_theme = "rgba(108, 99, 255, 0.08)" if st.session_state.is_flipped else "rgba(26, 29, 41, 0.45)"
        border_theme = "#6C63FF" if st.session_state.is_flipped else "rgba(255,255,255,0.08)"
        
        st.markdown(f"""
<div class="glass-card flashcard-inner" style="background: {bg_theme}; border-color: {border_theme};">
<div>
<span style="font-size: 0.75rem; color: #6C63FF; text-transform: uppercase; font-weight: 700; letter-spacing: 0.1em; display: block; margin-bottom: 12px;">
{"ANSWER/EXPLANATION" if st.session_state.is_flipped else "QUESTION/CONCEPT"}
</span>
<div style="font-size: 1.35rem; font-weight: 600; color: #ffffff; line-height: 1.5;">{face_text}</div>
</div>
</div>
""", unsafe_allow_html=True)
        
        # Flip Actions
        col_f1, col_f2 = st.columns(2)
        with col_f1:
            if st.button("🔄 Flip Card"):
                st.session_state.is_flipped = not st.session_state.is_flipped
                st.rerun()
                
        with col_f2:
            is_curr_mastered = st.session_state.mastered_count[deck_name][idx]
            btn_label = "✅ Mastered (Know It)" if not is_curr_mastered else "❌ Unmaster (Review Later)"
            if st.button(btn_label):
                st.session_state.mastered_count[deck_name][idx] = not is_curr_mastered
                # Auto advance if marking mastered
                if not is_curr_mastered and idx < len(deck) - 1:
                    st.session_state.card_index += 1
                    st.session_state.is_flipped = False
                st.rerun()
                
        st.markdown("<div style='margin-top: 15px;'></div>", unsafe_allow_html=True)
        
        # Nav Controls
        nav_col1, nav_col2 = st.columns(2)
        with nav_col1:
            if idx > 0:
                if st.button("Previous Card"):
                    st.session_state.card_index -= 1
                    st.session_state.is_flipped = False
                    st.rerun()
        with nav_col2:
            if idx < len(deck) - 1:
                if st.button("Next Card"):
                    st.session_state.card_index += 1
                    st.session_state.is_flipped = False
                    st.rerun()
