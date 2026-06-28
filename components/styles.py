import streamlit as st

def apply_custom_styles():
    """
    Applies the ultra-premium Apple Vision Pro / Linear / Stripe-inspired
    light-theme design system to StudentOS AI.
    Features:
    - Multi-layer aurora background with floating blobs
    - Glass cards with 18px blur, white borders, soft shadows
    - Inter + Outfit typography
    - Micro-animations: hover lift, progress fills, counter animations
    - Command palette overlay styles
    - Floating AI bubble styles
    - macOS-style sidebar styles
    """
    custom_css = """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=Outfit:wght@300;400;500;600;700;800;900&display=swap');

    /* ═══════════════════════════════════════════════════════════════
       GLOBAL RESET & BASE TYPOGRAPHY
    ═══════════════════════════════════════════════════════════════ */
    html, body, [class*="css"], .stMarkdown, p, span, div {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
        color: #0F172A;
        -webkit-font-smoothing: antialiased;
    }

    h1, h2, h3, h4, h5, h6 {
        font-family: 'Outfit', sans-serif !important;
        font-weight: 700 !important;
        color: #0F172A !important;
        letter-spacing: -0.02em;
        -webkit-text-fill-color: unset !important;
        background: none !important;
        -webkit-background-clip: unset !important;
    }

    /* ═══════════════════════════════════════════════════════════════
       MULTI-LAYER AURORA BACKGROUND
    ═══════════════════════════════════════════════════════════════ */
    .stApp {
        background-color: #FAFAFC !important;
        background-image:
            radial-gradient(ellipse 80% 60% at 10% -10%, rgba(124, 58, 237, 0.07) 0%, transparent 60%),
            radial-gradient(ellipse 60% 50% at 90% 10%, rgba(37, 99, 235, 0.06) 0%, transparent 55%),
            radial-gradient(ellipse 50% 40% at 50% 100%, rgba(6, 182, 212, 0.05) 0%, transparent 55%),
            radial-gradient(ellipse 40% 30% at 80% 80%, rgba(124, 58, 237, 0.04) 0%, transparent 50%) !important;
        background-attachment: fixed !important;
        min-height: 100vh;
    }

    /* Aurora animated floating blobs */
    .aurora-blob-1 {
        position: fixed; top: -150px; left: -100px; width: 600px; height: 600px;
        border-radius: 50%;
        background: radial-gradient(circle, rgba(124, 58, 237, 0.08) 0%, transparent 70%);
        animation: blobFloat1 18s ease-in-out infinite;
        pointer-events: none; z-index: 0;
        filter: blur(40px);
    }
    .aurora-blob-2 {
        position: fixed; top: 20%; right: -150px; width: 500px; height: 500px;
        border-radius: 50%;
        background: radial-gradient(circle, rgba(37, 99, 235, 0.07) 0%, transparent 70%);
        animation: blobFloat2 22s ease-in-out infinite;
        pointer-events: none; z-index: 0;
        filter: blur(50px);
    }
    .aurora-blob-3 {
        position: fixed; bottom: -100px; left: 30%; width: 700px; height: 400px;
        border-radius: 50%;
        background: radial-gradient(circle, rgba(6, 182, 212, 0.06) 0%, transparent 70%);
        animation: blobFloat3 25s ease-in-out infinite;
        pointer-events: none; z-index: 0;
        filter: blur(60px);
    }

    @keyframes blobFloat1 {
        0%, 100% { transform: translate(0, 0) scale(1); }
        33% { transform: translate(60px, 40px) scale(1.08); }
        66% { transform: translate(-30px, 80px) scale(0.95); }
    }
    @keyframes blobFloat2 {
        0%, 100% { transform: translate(0, 0) scale(1); }
        40% { transform: translate(-80px, 60px) scale(1.05); }
        70% { transform: translate(40px, -40px) scale(0.97); }
    }
    @keyframes blobFloat3 {
        0%, 100% { transform: translate(0, 0) scale(1); }
        30% { transform: translate(50px, -30px) scale(1.03); }
        60% { transform: translate(-60px, 20px) scale(1.08); }
    }

    /* ═══════════════════════════════════════════════════════════════
       STREAMLIT LAYOUT OVERRIDES
    ═══════════════════════════════════════════════════════════════ */
    .block-container {
        padding-top: 1rem !important;
        padding-bottom: 3rem !important;
        padding-left: 1rem !important;
        padding-right: 1rem !important;
        max-width: 100% !important;
    }

    /* Hide default Streamlit elements */
    #MainMenu { visibility: hidden; }
    footer { visibility: hidden; }
    header { visibility: hidden; }
    [data-testid="stSidebarNav"] { display: none !important; }
    [data-testid="sidebar-navs"] { display: none !important; }
    section[data-testid="stSidebar"] { display: none !important; }
    [data-testid="stDecoration"] { display: none !important; }
    [data-testid="stToolbar"] { display: none !important; }

    /* ═══════════════════════════════════════════════════════════════
       PREMIUM GLASS CARDS
    ═══════════════════════════════════════════════════════════════ */
    .glass-card {
        background: rgba(255, 255, 255, 0.78) !important;
        backdrop-filter: blur(18px) !important;
        -webkit-backdrop-filter: blur(18px) !important;
        border: 1px solid rgba(255, 255, 255, 0.85) !important;
        border-radius: 20px !important;
        padding: 24px !important;
        margin-bottom: 16px !important;
        box-shadow:
            0 1px 3px rgba(0, 0, 0, 0.04),
            0 4px 16px rgba(0, 0, 0, 0.05),
            0 20px 60px -10px rgba(15, 23, 42, 0.07) !important;
        transition: all 0.35s cubic-bezier(0.23, 1, 0.32, 1) !important;
        position: relative !important;
        overflow: hidden !important;
    }

    .glass-card:hover {
        transform: translateY(-4px) !important;
        box-shadow:
            0 2px 8px rgba(0, 0, 0, 0.05),
            0 8px 32px rgba(0, 0, 0, 0.07),
            0 30px 80px -12px rgba(124, 58, 237, 0.10) !important;
        border-color: rgba(124, 58, 237, 0.15) !important;
    }

    /* Light sweep effect on hover */
    .glass-card::after {
        content: '';
        position: absolute;
        top: 0; left: -100%;
        width: 40%; height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.4), transparent);
        transition: left 0.5s ease;
        pointer-events: none;
    }
    .glass-card:hover::after { left: 120%; }

    /* ═══════════════════════════════════════════════════════════════
       STAT CARDS
    ═══════════════════════════════════════════════════════════════ */
    .stat-card {
        background: rgba(255, 255, 255, 0.85) !important;
        backdrop-filter: blur(18px) !important;
        border: 1px solid rgba(255, 255, 255, 0.9) !important;
        border-radius: 20px !important;
        padding: 22px 24px !important;
        box-shadow: 0 2px 20px rgba(15, 23, 42, 0.06) !important;
        transition: all 0.3s cubic-bezier(0.23, 1, 0.32, 1) !important;
        position: relative;
        overflow: hidden;
    }
    .stat-card:hover {
        transform: translateY(-5px) !important;
        box-shadow: 0 12px 40px rgba(124, 58, 237, 0.12) !important;
    }

    .stat-val {
        font-size: 2.4rem !important;
        font-weight: 800 !important;
        color: #0F172A !important;
        font-family: 'Outfit', sans-serif !important;
        letter-spacing: -0.03em;
        line-height: 1;
        -webkit-text-fill-color: unset !important;
        background: none !important;
    }

    .stat-label {
        font-size: 0.72rem !important;
        color: #64748B !important;
        font-weight: 600 !important;
        text-transform: uppercase !important;
        letter-spacing: 0.09em !important;
    }

    /* ═══════════════════════════════════════════════════════════════
       GRADIENT TEXT ACCENT
    ═══════════════════════════════════════════════════════════════ */
    .gradient-text {
        background: linear-gradient(135deg, #7C3AED 0%, #2563EB 50%, #06B6D4 100%) !important;
        -webkit-background-clip: text !important;
        -webkit-text-fill-color: transparent !important;
        font-weight: 800 !important;
    }

    .gradient-text-warm {
        background: linear-gradient(135deg, #F59E0B 0%, #EF4444 100%) !important;
        -webkit-background-clip: text !important;
        -webkit-text-fill-color: transparent !important;
        font-weight: 800 !important;
    }

    /* ═══════════════════════════════════════════════════════════════
       PREMIUM SIDEBAR (Custom Column-based)
    ═══════════════════════════════════════════════════════════════ */
    .sidebar-container {
        background: rgba(255, 255, 255, 0.82) !important;
        backdrop-filter: blur(20px) !important;
        border: 1px solid rgba(0,0,0,0.06) !important;
        border-radius: 24px !important;
        padding: 20px 14px !important;
        height: calc(100vh - 100px) !important;
        position: sticky !important;
        top: 80px !important;
        overflow-y: auto !important;
        box-shadow: 0 4px 24px rgba(15,23,42,0.06) !important;
    }

    .sidebar-nav-item {
        display: flex !important;
        align-items: center !important;
        padding: 10px 12px !important;
        border-radius: 12px !important;
        margin-bottom: 3px !important;
        cursor: pointer !important;
        transition: all 0.2s ease !important;
        text-decoration: none !important;
        color: #475569 !important;
        font-size: 0.875rem !important;
        font-weight: 500 !important;
    }

    .sidebar-nav-item:hover {
        background: rgba(124, 58, 237, 0.07) !important;
        color: #7C3AED !important;
    }

    .sidebar-nav-item.active {
        background: linear-gradient(135deg, rgba(124, 58, 237, 0.1), rgba(37, 99, 235, 0.08)) !important;
        color: #7C3AED !important;
        font-weight: 600 !important;
        border-left: 3px solid #7C3AED !important;
    }

    .sidebar-section-label {
        font-size: 0.68rem !important;
        font-weight: 700 !important;
        color: #94A3B8 !important;
        text-transform: uppercase !important;
        letter-spacing: 0.1em !important;
        padding: 12px 12px 6px !important;
    }

    /* ═══════════════════════════════════════════════════════════════
       FLOATING NAVBAR
    ═══════════════════════════════════════════════════════════════ */
    .floating-navbar {
        position: sticky !important;
        top: 0 !important;
        z-index: 999 !important;
        background: rgba(255, 255, 255, 0.85) !important;
        backdrop-filter: blur(20px) saturate(180%) !important;
        -webkit-backdrop-filter: blur(20px) saturate(180%) !important;
        border-bottom: 1px solid rgba(0, 0, 0, 0.06) !important;
        padding: 12px 24px !important;
        margin-bottom: 0 !important;
    }

    /* ═══════════════════════════════════════════════════════════════
       PREMIUM BUTTONS
    ═══════════════════════════════════════════════════════════════ */
    div.stButton > button {
        background: #7C3AED !important;
        color: #ffffff !important;
        border: none !important;
        padding: 10px 20px !important;
        border-radius: 12px !important;
        font-weight: 600 !important;
        font-size: 0.875rem !important;
        letter-spacing: 0.01em !important;
        transition: all 0.25s cubic-bezier(0.23, 1, 0.32, 1) !important;
        box-shadow: 0 2px 8px rgba(124, 58, 237, 0.25) !important;
        width: 100% !important;
    }

    div.stButton > button:hover {
        background: #6D28D9 !important;
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 20px rgba(124, 58, 237, 0.35) !important;
    }

    div.stButton > button:active {
        transform: translateY(0px) scale(0.98) !important;
    }

    /* Secondary button variant override */
    div.stButton > button[kind="secondary"] {
        background: rgba(124, 58, 237, 0.08) !important;
        color: #7C3AED !important;
        box-shadow: none !important;
        border: 1px solid rgba(124, 58, 237, 0.2) !important;
    }

    /* ═══════════════════════════════════════════════════════════════
       INPUTS
    ═══════════════════════════════════════════════════════════════ */
    div[data-baseweb="input"] > div,
    div[data-baseweb="textarea"] > div,
    div[data-baseweb="select"] > div:first-child {
        background-color: rgba(255, 255, 255, 0.9) !important;
        border: 1.5px solid rgba(0, 0, 0, 0.1) !important;
        border-radius: 12px !important;
        color: #0F172A !important;
        transition: all 0.25s ease !important;
    }

    div[data-baseweb="input"]:focus-within > div,
    div[data-baseweb="textarea"]:focus-within > div {
        border-color: #7C3AED !important;
        box-shadow: 0 0 0 3px rgba(124, 58, 237, 0.12) !important;
    }

    input, textarea {
        color: #0F172A !important;
    }

    /* ═══════════════════════════════════════════════════════════════
       BADGES & TAGS
    ═══════════════════════════════════════════════════════════════ */
    .badge {
        display: inline-flex !important;
        align-items: center !important;
        padding: 3px 10px !important;
        border-radius: 20px !important;
        font-size: 0.72rem !important;
        font-weight: 700 !important;
        text-transform: uppercase !important;
        letter-spacing: 0.06em !important;
    }
    .badge-purple { background: rgba(124,58,237,0.10); color: #7C3AED; border: 1px solid rgba(124,58,237,0.2); }
    .badge-blue   { background: rgba(37,99,235,0.10);  color: #2563EB; border: 1px solid rgba(37,99,235,0.2); }
    .badge-green  { background: rgba(34,197,94,0.10);  color: #16A34A; border: 1px solid rgba(34,197,94,0.2); }
    .badge-amber  { background: rgba(245,158,11,0.10); color: #D97706; border: 1px solid rgba(245,158,11,0.2); }
    .badge-red    { background: rgba(239,68,68,0.10);  color: #DC2626; border: 1px solid rgba(239,68,68,0.2); }
    .badge-high   { background: rgba(239,68,68,0.10);  color: #DC2626; border: 1px solid rgba(239,68,68,0.2); }
    .badge-medium { background: rgba(245,158,11,0.10); color: #D97706; border: 1px solid rgba(245,158,11,0.2); }
    .badge-low    { background: rgba(34,197,94,0.10);  color: #16A34A; border: 1px solid rgba(34,197,94,0.2); }

    /* ═══════════════════════════════════════════════════════════════
       PROGRESS BARS
    ═══════════════════════════════════════════════════════════════ */
    .progress-track {
        background: rgba(0,0,0,0.06);
        border-radius: 99px;
        height: 6px;
        overflow: hidden;
    }
    .progress-fill {
        height: 100%;
        border-radius: 99px;
        background: linear-gradient(90deg, #7C3AED, #2563EB);
        transition: width 1.2s cubic-bezier(0.23, 1, 0.32, 1);
    }
    .progress-fill-green { background: linear-gradient(90deg, #22C55E, #06B6D4); }
    .progress-fill-amber { background: linear-gradient(90deg, #F59E0B, #EF4444); }

    /* ═══════════════════════════════════════════════════════════════
       FLOATING AI BUBBLE
    ═══════════════════════════════════════════════════════════════ */
    .ai-bubble {
        position: fixed !important;
        bottom: 28px !important;
        right: 28px !important;
        z-index: 9999 !important;
    }

    .ai-bubble-btn {
        width: 58px !important; height: 58px !important;
        border-radius: 50% !important;
        background: linear-gradient(135deg, #7C3AED, #2563EB) !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        font-size: 1.5rem !important;
        cursor: pointer !important;
        box-shadow: 0 4px 20px rgba(124, 58, 237, 0.4) !important;
        animation: aiBreath 3s ease-in-out infinite !important;
        border: none !important;
        color: white !important;
        transition: all 0.3s ease !important;
    }

    .ai-bubble-btn:hover {
        transform: scale(1.12) !important;
        box-shadow: 0 8px 32px rgba(124, 58, 237, 0.55) !important;
    }

    @keyframes aiBreath {
        0%, 100% { box-shadow: 0 4px 20px rgba(124,58,237,0.35), 0 0 0 0 rgba(124,58,237,0.2); }
        50% { box-shadow: 0 6px 28px rgba(124,58,237,0.45), 0 0 0 12px rgba(124,58,237,0); }
    }

    /* ═══════════════════════════════════════════════════════════════
       COMMAND PALETTE (Ctrl+K)
    ═══════════════════════════════════════════════════════════════ */
    .cmd-palette-overlay {
        position: fixed !important;
        inset: 0 !important;
        background: rgba(15, 23, 42, 0.4) !important;
        backdrop-filter: blur(4px) !important;
        z-index: 10000 !important;
        display: flex !important;
        align-items: flex-start !important;
        justify-content: center !important;
        padding-top: 15vh !important;
    }

    .cmd-palette-box {
        background: rgba(255,255,255,0.97) !important;
        border-radius: 20px !important;
        width: min(640px, 90vw) !important;
        box-shadow: 0 32px 80px rgba(15,23,42,0.25) !important;
        overflow: hidden !important;
        border: 1px solid rgba(0,0,0,0.06) !important;
    }

    /* ═══════════════════════════════════════════════════════════════
       COURSE NETFLIX CARDS
    ═══════════════════════════════════════════════════════════════ */
    .course-card {
        background: rgba(255, 255, 255, 0.9) !important;
        border: 1px solid rgba(0, 0, 0, 0.06) !important;
        border-radius: 18px !important;
        padding: 20px !important;
        transition: all 0.35s cubic-bezier(0.23, 1, 0.32, 1) !important;
        cursor: pointer !important;
        box-shadow: 0 2px 12px rgba(15,23,42,0.05) !important;
        overflow: hidden !important;
        position: relative !important;
    }
    .course-card:hover {
        transform: translateY(-6px) scale(1.01) !important;
        box-shadow: 0 16px 48px rgba(124, 58, 237, 0.13) !important;
        border-color: rgba(124, 58, 237, 0.2) !important;
    }

    /* ═══════════════════════════════════════════════════════════════
       HEATMAP SQUARES
    ═══════════════════════════════════════════════════════════════ */
    .heatmap-cell {
        width: 13px; height: 13px;
        border-radius: 3px;
        display: inline-block;
        transition: transform 0.15s ease;
    }
    .heatmap-cell:hover { transform: scale(1.5); }

    /* ═══════════════════════════════════════════════════════════════
       ACHIEVEMENT BADGE FLIP
    ═══════════════════════════════════════════════════════════════ */
    .badge-flip-container {
        perspective: 800px;
        width: 100%;
    }
    .badge-flip-inner {
        transition: transform 0.6s cubic-bezier(0.23, 1, 0.32, 1);
        transform-style: preserve-3d;
        position: relative;
    }
    .badge-flip-container:hover .badge-flip-inner {
        transform: rotateY(180deg);
    }
    .badge-front, .badge-back {
        backface-visibility: hidden;
    }
    .badge-back {
        transform: rotateY(180deg);
        position: absolute;
        top: 0; left: 0; width: 100%;
    }

    /* ═══════════════════════════════════════════════════════════════
       PLOTLY CHARTS
    ═══════════════════════════════════════════════════════════════ */
    .js-plotly-plot .plotly {
        border-radius: 16px !important;
    }

    /* ═══════════════════════════════════════════════════════════════
       TABS
    ═══════════════════════════════════════════════════════════════ */
    button[data-baseweb="tab"] {
        color: #64748B !important;
        font-weight: 600 !important;
        font-size: 0.875rem !important;
        background: none !important;
        border-bottom: 2px solid transparent !important;
        padding: 8px 16px !important;
        transition: all 0.2s ease !important;
    }
    button[aria-selected="true"] {
        color: #7C3AED !important;
        border-bottom-color: #7C3AED !important;
    }

    /* ═══════════════════════════════════════════════════════════════
       SCROLLBAR
    ═══════════════════════════════════════════════════════════════ */
    ::-webkit-scrollbar { width: 6px; height: 6px; }
    ::-webkit-scrollbar-track { background: transparent; }
    ::-webkit-scrollbar-thumb { background: rgba(124,58,237,0.2); border-radius: 99px; }
    ::-webkit-scrollbar-thumb:hover { background: rgba(124,58,237,0.4); }

    /* ═══════════════════════════════════════════════════════════════
       STMETRIC OVERRIDES
    ═══════════════════════════════════════════════════════════════ */
    [data-testid="stMetricValue"] { font-family: 'Outfit', sans-serif !important; color: #0F172A !important; }
    [data-testid="stMetricLabel"] { color: #64748B !important; font-size: 0.8rem !important; }
    [data-testid="stMetricDelta"] { font-size: 0.8rem !important; }

    /* ═══════════════════════════════════════════════════════════════
       TIMELINE
    ═══════════════════════════════════════════════════════════════ */
    .timeline-item {
        border-left: 2px solid rgba(124,58,237,0.25);
        padding-left: 18px;
        margin-left: 8px;
        margin-bottom: 18px;
        position: relative;
    }
    .timeline-item::before {
        content: '';
        position: absolute;
        left: -6px; top: 4px;
        width: 10px; height: 10px;
        border-radius: 50%;
        background: #ffffff;
        border: 2px solid #7C3AED;
    }

    /* ═══════════════════════════════════════════════════════════════
       NUMBER COUNTER ANIMATION (JS-driven)
    ═══════════════════════════════════════════════════════════════ */
    .counter-animate {
        transition: all 0.8s ease;
    }

    /* ═══════════════════════════════════════════════════════════════
       HERO SECTION
    ═══════════════════════════════════════════════════════════════ */
    .hero-section {
        background: linear-gradient(135deg,
            rgba(124,58,237,0.06) 0%,
            rgba(37,99,235,0.04) 50%,
            rgba(6,182,212,0.04) 100%);
        border: 1px solid rgba(124,58,237,0.1);
        border-radius: 28px;
        padding: 36px 40px;
        position: relative;
        overflow: hidden;
        margin-bottom: 24px;
    }
    .hero-section::before {
        content: '';
        position: absolute;
        top: -60px; right: -60px;
        width: 300px; height: 300px;
        border-radius: 50%;
        background: radial-gradient(circle, rgba(124,58,237,0.08) 0%, transparent 70%);
        pointer-events: none;
    }

    /* ═══════════════════════════════════════════════════════════════
       POMODORO WIDGET
    ═══════════════════════════════════════════════════════════════ */
    .pomodoro-display {
        font-family: 'Outfit', monospace !important;
        font-size: 3rem !important;
        font-weight: 800 !important;
        color: #0F172A !important;
        letter-spacing: -0.02em;
        text-align: center;
    }

    /* ═══════════════════════════════════════════════════════════════
       QUICK ACTION BUTTONS (custom icon buttons)
    ═══════════════════════════════════════════════════════════════ */
    .quick-action-card {
        background: rgba(255,255,255,0.9);
        border: 1px solid rgba(0,0,0,0.06);
        border-radius: 16px;
        padding: 18px 14px;
        text-align: center;
        cursor: pointer;
        transition: all 0.3s cubic-bezier(0.23, 1, 0.32, 1);
        box-shadow: 0 2px 8px rgba(15,23,42,0.04);
    }
    .quick-action-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 12px 32px rgba(124,58,237,0.12);
        border-color: rgba(124,58,237,0.2);
        background: rgba(124,58,237,0.04);
    }

    /* ═══════════════════════════════════════════════════════════════
       AI ORB ANIMATION
    ═══════════════════════════════════════════════════════════════ */
    .ai-orb {
        width: 80px; height: 80px;
        border-radius: 50%;
        background: conic-gradient(from 0deg, #7C3AED, #2563EB, #06B6D4, #7C3AED);
        animation: orbSpin 4s linear infinite, orbPulse 3s ease-in-out infinite;
        box-shadow: 0 0 30px rgba(124,58,237,0.3), 0 0 60px rgba(37,99,235,0.2);
        margin: 0 auto;
    }
    @keyframes orbSpin {
        from { filter: hue-rotate(0deg); }
        to   { filter: hue-rotate(360deg); }
    }
    @keyframes orbPulse {
        0%, 100% { transform: scale(1); box-shadow: 0 0 30px rgba(124,58,237,0.3); }
        50% { transform: scale(1.08); box-shadow: 0 0 50px rgba(124,58,237,0.5); }
    }

    /* Stradio & selectbox label color fix */
    .stRadio label, .stCheckbox label, .stSelectbox label,
    .stSlider label, .stMultiSelect label, .stFileUploader label {
        color: #0F172A !important;
    }
    p, li, span { color: #334155 !important; }
    </style>
    """

    # JavaScript for micro-interactions
    custom_js = """
    <script>
    // Counter animation
    function animateCounters() {
        document.querySelectorAll('[data-counter]').forEach(el => {
            const target = parseInt(el.dataset.counter);
            let current = 0;
            const step = target / 60;
            const timer = setInterval(() => {
                current = Math.min(current + step, target);
                el.textContent = Math.round(current);
                if (current >= target) clearInterval(timer);
            }, 16);
        });
    }

    // Cursor spotlight effect
    document.addEventListener('mousemove', (e) => {
        const hero = document.querySelector('.hero-section');
        if (!hero) return;
        const rect = hero.getBoundingClientRect();
        const x = ((e.clientX - rect.left) / rect.width) * 100;
        const y = ((e.clientY - rect.top) / rect.height) * 100;
        hero.style.background = `radial-gradient(ellipse 60% 50% at ${x}% ${y}%, rgba(124,58,237,0.08) 0%, rgba(37,99,235,0.04) 40%, transparent 70%), linear-gradient(135deg, rgba(124,58,237,0.05) 0%, rgba(37,99,235,0.03) 100%)`;
    });

    // Button ripple effect
    document.addEventListener('click', function(e) {
        const btn = e.target.closest('button');
        if (!btn) return;
        const ripple = document.createElement('span');
        const rect = btn.getBoundingClientRect();
        ripple.style.cssText = `
            position:absolute;border-radius:50%;transform:scale(0);
            animation:ripple 0.5s linear;background:rgba(255,255,255,0.3);
            width:60px;height:60px;left:${e.clientX-rect.left-30}px;
            top:${e.clientY-rect.top-30}px;pointer-events:none;
        `;
        btn.style.position = 'relative';
        btn.style.overflow = 'hidden';
        btn.appendChild(ripple);
        setTimeout(() => ripple.remove(), 600);
    });

    // Command Palette (Ctrl+K)
    document.addEventListener('keydown', (e) => {
        if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
            e.preventDefault();
            const existing = document.getElementById('cmd-palette');
            if (existing) { existing.remove(); return; }
            const overlay = document.createElement('div');
            overlay.id = 'cmd-palette';
            overlay.style.cssText = `
                position:fixed;inset:0;background:rgba(15,23,42,0.5);
                backdrop-filter:blur(6px);z-index:10000;
                display:flex;align-items:flex-start;justify-content:center;padding-top:15vh;
            `;
            overlay.innerHTML = `
                <div style="background:rgba(255,255,255,0.98);border-radius:20px;width:min(580px,90vw);
                    box-shadow:0 32px 80px rgba(15,23,42,0.25);overflow:hidden;
                    border:1px solid rgba(0,0,0,0.08);animation:cmdSlide 0.2s ease;">
                    <div style="padding:16px 20px;border-bottom:1px solid rgba(0,0,0,0.06);
                        display:flex;align-items:center;gap:10px;">
                        <span style="font-size:1.1rem;">🔍</span>
                        <input id="cmd-input" placeholder="Search anything — modules, AI commands, files..."
                            style="flex:1;border:none;outline:none;font-size:1rem;
                            font-family:Inter,sans-serif;color:#0F172A;background:transparent;" autofocus>
                        <kbd style="font-size:0.7rem;background:#F1F5F9;border:1px solid #E2E8F0;
                            border-radius:6px;padding:2px 6px;color:#64748B;">ESC</kbd>
                    </div>
                    <div style="padding:8px 12px;max-height:340px;overflow-y:auto;">
                        ${['📊 Dashboard','🧠 AI Tutor','📚 PDF Chat (RAG)','📝 Quiz Generator',
                           '🃏 Flashcards','📅 Study Planner','📈 Analytics',
                           '📄 Resume Builder','✅ ATS Checker','💼 Placements','🎤 Mock Interview',
                           '⚙️ Settings','🎯 Focus Mode','🎵 Focus Music'].map(item => `
                            <div style="padding:10px 12px;border-radius:10px;cursor:pointer;
                                color:#334155;font-size:0.875rem;
                                transition:background 0.15s;display:flex;align-items:center;gap:10px;"
                                onmouseover="this.style.background='rgba(124,58,237,0.07)'"
                                onmouseout="this.style.background='transparent'">
                                ${item}
                            </div>`).join('')}
                    </div>
                    <div style="padding:10px 20px;background:#FAFAFC;
                        border-top:1px solid rgba(0,0,0,0.05);font-size:0.75rem;color:#94A3B8;
                        display:flex;gap:16px;">
                        <span>↑↓ Navigate</span><span>↵ Select</span><span>ESC Close</span>
                    </div>
                </div>
            `;
            overlay.addEventListener('click', (ev) => {
                if (ev.target === overlay) overlay.remove();
            });
            document.addEventListener('keydown', (ev) => {
                if (ev.key === 'Escape') overlay.remove();
            }, {once:true});
            document.body.appendChild(overlay);
            document.getElementById('cmd-input')?.focus();
        }
    });

    // CSS for ripple animation
    if (!document.getElementById('ripple-style')) {
        const s = document.createElement('style');
        s.id = 'ripple-style';
        s.textContent = `
            @keyframes ripple { to { transform:scale(4); opacity:0; } }
            @keyframes cmdSlide { from { opacity:0; transform:translateY(-20px); } to { opacity:1; transform:translateY(0); } }
        `;
        document.head.appendChild(s);
    }

    // Auto-init
    setTimeout(animateCounters, 300);
    </script>
    """

    st.markdown(custom_css + custom_js, unsafe_allow_html=True)
