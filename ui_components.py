import streamlit as st

# =========================
# MODERN COLOR SYSTEM
# =========================

COLORS = {
    "light": {
        "bg": "#F7F9FC",
        "primary": "#4F46E5",
        "success": "#22C55E",
        "danger": "#EF4444",
        "accent": "#06B6D4",
        "card_bg": "#FFFFFF",
        "text": "#1E293B",
        "text_muted": "#64748B",
        "shadow": "rgba(0, 0, 0, 0.05)",
        "sidebar_bg": "#FFFFFF",
    },
    "dark": {
        "bg": "#0F172A",
        "primary": "#6366F1",
        "success": "#22C55E",
        "danger": "#F87171",
        "accent": "#38BDF8",
        "card_bg": "#1E293B",
        "text": "#F8FAFC",
        "text_muted": "#94A3B8",
        "shadow": "rgba(0, 0, 0, 0.3)",
        "sidebar_bg": "#0B1120",
    }
}

def inject_custom_css():
    theme = st.session_state.get('theme', 'light')
    c = COLORS[theme]
    
    css = f"""
    <style>
        /* Global Styles */
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
        
        html, body, [data-testid="stAppViewContainer"] {{
            background-color: {c['bg']} !important;
            font-family: 'Inter', sans-serif;
            color: {c['text']} !important;
        }}
        
        [data-testid="stHeader"] {{
            background: transparent;
        }}
        
        [data-testid="stSidebar"] {{
            background-color: {c['sidebar_bg']} !important;
            border-right: 1px solid {c['shadow']};
        }}
        
        /* Typography */
        h1, h2, h3, h4, h5, h6, p, span, label {{
            color: {c['text']} !important;
        }}
        
        .text-muted {{
            color: {c['text_muted']} !important;
        }}
        
        /* Card System */
        .glass-card {{
            background: {c['card_bg']};
            border-radius: 20px;
            padding: 2rem;
            box-shadow: 0 10px 25px -5px {c['shadow']};
            border: 1px solid {c['shadow']};
            margin-bottom: 2rem;
            animation: fadeIn 0.6s ease-out;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }}
        
        .glass-card:hover {{
            transform: translateY(-5px);
            box-shadow: 0 20px 30px -10px {c['shadow']};
        }}
        
        /* Buttons */
        .stButton > button {{
            background: {c['primary']} !important;
            color: white !important;
            border-radius: 12px !important;
            padding: 0.6rem 1.5rem !important;
            font-weight: 600 !important;
            border: none !important;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
            width: 100%;
        }}
        
        .stButton > button:hover {{
            filter: brightness(1.1);
            transform: scale(1.02);
            box-shadow: 0 10px 15px -3px {c['primary']}40 !important;
        }}
        
        /* Sidebar Specific */
        [data-testid="stSidebar"] .stButton > button {{
            background: transparent !important;
            border: 1px solid {c['primary']}40 !important;
            color: {c['text']} !important;
            font-size: 0.9rem !important;
        }}
        
        [data-testid="stSidebar"] .stButton > button:hover {{
            background: {c['primary']}15 !important;
            border-color: {c['primary']} !important;
        }}
        
        .logout-btn-container .stButton > button {{
            background: {c['danger']}15 !important;
            color: {c['danger']} !important;
            border: 1px solid {c['danger']}40 !important;
        }}
        
        .logout-btn-container .stButton > button:hover {{
            background: {c['danger']} !important;
            color: white !important;
            border-color: {c['danger']} !important;
        }}
        
        /* Animations */
        @keyframes fadeIn {{
            from {{ opacity: 0; transform: translateY(10px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}
        
        @keyframes pulse {{
            0% {{ transform: scale(1); box-shadow: 0 0 0 0 {c['danger']}40; }}
            70% {{ transform: scale(1.02); box-shadow: 0 0 0 15px {c['danger']}00; }}
            100% {{ transform: scale(1); box-shadow: 0 0 0 0 {c['danger']}00; }}
        }}
        
        /* Input Field Styling (used outside the login page) */
        div[data-testid="stTextInput"] input {{
            background-color: {c['bg']} !important;
            border: 1px solid {c['shadow']} !important;
            border-radius: 10px !important;
            padding: 0.75rem !important;
            color: {c['text']} !important;
        }}
        
        div[data-testid="stTextInput"] label {{
            font-weight: 600 !important;
            margin-bottom: 0.5rem !important;
            color: {c['text']} !important;
        }}
        
        /* Result Cards */
        .result-card {{
            padding: 2.5rem;
            border-radius: 24px;
            text-align: center;
            margin-top: 1.5rem;
            position: relative;
            overflow: hidden;
            border: 2px solid transparent;
        }}
        
        .result-card.fresh {{
            background: linear-gradient(135deg, {c['success']}15 0%, {c['success']}05 100%);
            border-color: {c['success']}40;
            box-shadow: 0 20px 40px -15px {c['success']}30;
        }}
        
        .result-card.rotten {{
            background: linear-gradient(135deg, {c['danger']}15 0%, {c['danger']}05 100%);
            border-color: {c['danger']}40;
            box-shadow: 0 20px 40px -15px {c['danger']}30;
            animation: pulse 2s infinite;
        }}
        
        .result-card.unknown {{
            background: linear-gradient(135deg, {c['accent']}15 0%, {c['accent']}05 100%);
            border-color: {c['accent']}40;
            box-shadow: 0 20px 40px -15px {c['accent']}30;
        }}
        
        .result-title {{
            font-size: 0.875rem;
            text-transform: uppercase;
            letter-spacing: 0.1em;
            font-weight: 700;
            margin-bottom: 0.5rem;
            opacity: 0.8;
        }}
        
        .result-status {{
            font-size: 3rem;
            font-weight: 800;
            margin-bottom: 1rem;
        }}
        
        .status-fresh {{ color: {c['success']} !important; }}
        .status-rotten {{ color: {c['danger']} !important; }}
        .status-unknown {{ color: {c['accent']} !important; }}
        
        /* Hide default streamlit elements */
        div[data-testid="stStatusWidget"] {{
            visibility: hidden;
        }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

# =========================
# LOGIN PAGE — REDESIGNED
# =========================

def inject_login_css():
    """Login-specific design system. Deliberately independent of the
    light/dark app theme -- the portal has its own identity: a dark
    "candling room" with a single warm light source, mirroring the
    literal act of candling an egg (shining light through it to see
    what's inside) as the visual metaphor for authentication itself.
    """
    css = """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,600;9..144,700&family=Space+Grotesk:wght@400;500;600;700&display=swap');

        :root {
            --ink: #14110F;
            --surface: #221D18;
            --surface-line: #3A322A;
            --ember: #E8A33D;
            --ember-soft: rgba(232, 163, 61, 0.16);
            --verdigris: #2FA98C;
            --parchment: #F3ECDF;
            --ash: #948A7C;
        }

        [data-testid="stAppViewContainer"],
        [data-testid="stAppViewContainer"] > .main,
        html, body {
            background: radial-gradient(120% 90% at 50% 0%, #241E17 0%, var(--ink) 55%, #0B0906 100%) !important;
        }

        [data-testid="stHeader"] { background: transparent !important; }
        [data-testid="stStatusWidget"] { visibility: hidden; }

        .login-shell {
            max-width: 420px;
            margin: 9vh auto 0 auto;
            padding: 3rem 2.75rem 2.75rem;
            background: var(--surface);
            border: 1px solid var(--surface-line);
            border-radius: 18px;
            box-shadow: 0 30px 60px -20px rgba(0, 0, 0, 0.6);
            animation: riseIn 0.7s cubic-bezier(0.16, 1, 0.3, 1);
        }

        @keyframes riseIn {
            from { opacity: 0; transform: translateY(18px); }
            to { opacity: 1; transform: translateY(0); }
        }

        .candle-icon { text-align: center; margin-bottom: 1.5rem; }
        .glow-halo { animation: breathe 4.5s ease-in-out infinite; transform-origin: center; }

        @keyframes breathe {
            0%, 100% { opacity: 0.45; transform: scale(1); }
            50% { opacity: 0.85; transform: scale(1.06); }
        }

        .login-heading {
            text-align: center;
            margin-bottom: 2.25rem;
        }

        .login-heading h1 {
            font-family: 'Fraunces', serif !important;
            font-weight: 600 !important;
            font-size: 1.75rem !important;
            color: var(--parchment) !important;
            margin: 0 0 0.5rem 0 !important;
            letter-spacing: -0.01em;
        }

        .login-heading p {
            font-family: 'Space Grotesk', sans-serif !important;
            color: var(--ash) !important;
            font-size: 0.95rem !important;
            margin: 0 !important;
            line-height: 1.5;
        }

        .login-shell label {
            font-family: 'Space Grotesk', sans-serif !important;
            font-size: 0.85rem !important;
            font-weight: 500 !important;
            color: var(--ash) !important;
            margin-bottom: 0.35rem !important;
        }

        .login-shell div[data-testid="stTextInput"] input {
            font-family: 'Space Grotesk', sans-serif !important;
            background: transparent !important;
            border: none !important;
            border-bottom: 1.5px solid var(--surface-line) !important;
            border-radius: 0 !important;
            padding: 0.6rem 0.1rem !important;
            color: var(--parchment) !important;
            font-size: 1rem !important;
            transition: border-color 0.25s ease;
        }

        .login-shell div[data-testid="stTextInput"] input:focus {
            border-bottom-color: var(--ember) !important;
            box-shadow: none !important;
        }

        .login-shell div[data-testid="stTextInput"] input::placeholder {
            color: var(--surface-line) !important;
        }

        .login-shell .stButton > button {
            font-family: 'Space Grotesk', sans-serif !important;
            background: var(--ember) !important;
            color: #221A0D !important;
            border: none !important;
            border-radius: 10px !important;
            padding: 0.75rem 1.5rem !important;
            font-weight: 600 !important;
            font-size: 0.95rem !important;
            margin-top: 1.75rem !important;
            transition: filter 0.25s ease, transform 0.25s ease !important;
            width: 100%;
        }

        .login-shell .stButton > button:hover {
            filter: brightness(1.08);
            transform: translateY(-1px);
        }

        .login-shell div[data-testid="stForm"] {
            border: none !important;
            padding: 0 !important;
        }

        .login-footnote {
            text-align: center;
            margin-top: 1.75rem;
            font-family: 'Space Grotesk', sans-serif;
            font-size: 0.78rem;
            color: var(--surface-line);
        }
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)


def render_login():
    inject_login_css()

    _, col, _ = st.columns([1, 2, 1])

    with col:
        st.markdown("""
            <div class="login-shell">
                <div class="candle-icon">
                    <svg width="60" height="78" viewBox="0 0 72 92" xmlns="http://www.w3.org/2000/svg">
                        <defs>
                            <radialGradient id="candling-glow" cx="50%" cy="42%" r="65%">
                                <stop offset="0%" stop-color="#FCD98A"/>
                                <stop offset="45%" stop-color="#E8A33D"/>
                                <stop offset="100%" stop-color="#8A5A1E"/>
                            </radialGradient>
                        </defs>
                        <ellipse class="glow-halo" cx="36" cy="48" rx="34" ry="30" fill="#E8A33D" opacity="0.5"/>
                        <path d="M36 4C22 4 8 34 8 56C8 76 20 88 36 88C52 88 64 76 64 56C64 34 50 4 36 4Z"
                              fill="url(#candling-glow)" stroke="#3A2410" stroke-width="1.5"/>
                    </svg>
                </div>
                <div class="login-heading">
                    <h1>Egg Quality Portal</h1>
                    <p>Sign in with your researcher credentials to access the assessment system</p>
                </div>
        """, unsafe_allow_html=True)

        with st.form("login_form", clear_on_submit=False):
            username = st.text_input("Researcher ID", placeholder="Enter your researcher ID")
            password = st.text_input("Password", type="password", placeholder="••••••••")

            submit = st.form_submit_button("Sign in", use_container_width=True)

            if submit:
                try:
                    users = st.secrets["users"]

                    if username in users and users[username]["password"] == password:
                        st.session_state.authenticated = True
                        st.session_state.username = username
                        st.session_state.role = users[username]["role"]
                        st.success("Welcome back!")
                        st.rerun()
                    else:
                        st.error("Invalid credentials")
                except Exception as e:
                    st.error("Authentication system error")

        st.markdown("""
                <div class="login-footnote">Intelligent Poultry Assessment System</div>
            </div>
        """, unsafe_allow_html=True)

# =========================
# LAYOUT COMPONENTS
# =========================

def render_hero():
    st.markdown(f"""
        <div style="background: linear-gradient(135deg, {COLORS[st.session_state.theme]['primary']} 0%, {COLORS[st.session_state.theme]['accent']} 100%); 
                    padding: 4rem 2rem; border-radius: 24px; text-align: center; color: white; margin-bottom: 3rem;
                    box-shadow: 0 20px 25px -5px {COLORS[st.session_state.theme]['primary']}30;">
            <div style="font-size: 4rem; margin-bottom: 1rem;">🥚</div>
            <h1 style="color: white !important; font-size: 2.5rem; font-weight: 800; margin: 0; letter-spacing: -0.025em;">AI-Driven Chicken Egg Quality Assessment System</h1>
            <p style="color: white !important; font-size: 1.1rem; opacity: 0.9; font-weight: 400; max-width: 800px; margin: 1rem auto 0;">
                Cost-Effective Deep Learning Framework for Quality Assessment of Chicken Eggs for Small-Scale Farming
            </p>
        </div>
    """, unsafe_allow_html=True)

def render_status_card(label, value, type="success"):
    c = COLORS[st.session_state.theme]
    border_color = c['success'] if type == "success" else c['danger']
    bg_color = f"{border_color}10"
    
    st.markdown(f"""
        <div style="background: {bg_color}; border-left: 4px solid {border_color}; padding: 1.5rem; border-radius: 12px; margin-bottom: 1rem;">
            <div style="font-size: 0.8rem; font-weight: 700; opacity: 0.6; text-transform: uppercase; color: {c['text']} !important;">{label}</div>
            <div style="font-size: 1.5rem; font-weight: 700; color: {border_color} !important;">{value}</div>
        </div>
    """, unsafe_allow_html=True)

# =========================
# RESULT CARD COMPONENTS
# =========================

def render_result_card(status, confidence):
    status = status.lower().strip()

    label = "Diagnostic Analysis Report"

    # Matches the real trained classes in label_mapping.json exactly:
    # {"dead": 0, "fertile": 1, "infertile": 2}
    if status == "fertile":
        ui_type = "fresh"
        icon = "🐣"
        display_status = "Fertile"
    elif status == "infertile":
        ui_type = "unknown"
        icon = "⚪"
        display_status = "Infertile"
    elif status == "dead":
        ui_type = "rotten"
        icon = "⚠️"
        display_status = "Dead-in-Shell"
    else:
        ui_type = "unknown"
        icon = "🔍"
        display_status = "Unclassified Sample (Requires Further Review)"

    st.markdown(f"""
        <div class="result-card {ui_type}">
            <div class="result-title">{label}</div>
            <div class="result-status status-{ui_type}" style="font-size: 1.8rem;">{icon} {display_status}</div>
            <div style="font-size: 1.1rem; font-weight: 600; opacity: 0.9;">
                Model Prediction Confidence Index: <span style="font-size: 1.4rem;">{confidence:.1%}</span>
            </div>
        </div>
    """, unsafe_allow_html=True)

# =========================
# UI THEME SYSTEM
# =========================

def render_sidebar_controls():
    with st.sidebar:
        st.markdown(f"""
            <div style="padding: 1rem 0; text-align: center;">
                <div style="font-size: 2.5rem; margin-bottom: 0.5rem;">🔬</div>
                <h3 style="margin:0;">Research Panel</h3>
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        st.markdown(f"""
            <div style="padding: 1rem; background: {COLORS[st.session_state.theme]['bg']}; border-radius: 12px; margin-bottom: 1rem;">
                <div style="font-size: 0.8rem; font-weight: 700; opacity: 0.6; text-transform: uppercase;">Active Researcher</div>
                <div style="font-weight: 700; font-size: 1.1rem;">{st.session_state.username}</div>
                <div style="font-size: 0.85rem; opacity: 0.8;">Authorization: {st.session_state.role.capitalize()}</div>
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown("#### System Configuration Module")
        is_dark = st.session_state.get('theme', 'light') == 'dark'
        if st.toggle("🌙 Enable Dark Mode", value=is_dark):
            if st.session_state.theme != 'dark':
                st.session_state.theme = 'dark'
                st.rerun()
        else:
            if st.session_state.theme != 'light':
                st.session_state.theme = 'light'
                st.rerun()
                
        st.markdown("---")
        
        st.markdown('<div class="logout-btn-container">', unsafe_allow_html=True)
        if st.button("🚫 Terminate Session", key="logout", use_container_width=True):
            st.session_state.authenticated = False
            st.session_state.username = None
            st.session_state.role = None
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown("---")
        with st.expander("📊 Model Performance (verified run)", expanded=False):
            st.markdown("""
                - Stage 2 classification accuracy: 99.84%
                - Macro ROC-AUC: 0.99995
                - Mean Average Precision: 0.99991
                - Mean inference latency: ~88.7 ms
                - Framework: TensorFlow v2.20.0
                
                *Sourced from `results/metrics_summary.json`, generated by a
                completed, reproducible training run.*
            """)
        
        with st.expander("🧩 Deep Learning Model Configuration Panel", expanded=False):
            st.markdown("""
                **Architecture:**
                - Two-stage CNN pipeline: egg detector → fertility classifier
                - Backbone: MobileNetV2 (frozen, ImageNet-pretrained) + CBAM
                  (channel + spatial attention)
                - Input Vector: [224, 224, 3]
                - Activation: Softmax (classifier) / Sigmoid (detector) / ReLU (hidden)
            """)
