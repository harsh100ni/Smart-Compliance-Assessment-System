import streamlit as st

st.set_page_config(
    page_title="EV-SCAN | Emergency Vehicle Compliance",
    page_icon="🚨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load custom CSS
with open("assets/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

from pages_modules import home, dashboard, live_monitor, analysis, compliance_report, settings

PAGES = {
    "🏠  Home": home,
    "📊  Dashboard": dashboard,
    "📡  Live Monitor": live_monitor,
    "🔍  Spatiotemporal Analysis": analysis,
    "📋  Compliance Reports": compliance_report,
    "⚙️  Settings": settings,
}

# Sidebar
with st.sidebar:
    st.markdown("""
    <div class="sidebar-brand">
        <div class="brand-icon">🚨</div>
        <div class="brand-text">
            <span class="brand-title">EV-SCAN</span>
            <span class="brand-sub">Emergency Vehicle Intelligence</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="sidebar-divider"></div>', unsafe_allow_html=True)

    # Status indicator
    st.markdown("""
    <div class="status-pill active">
        <span class="status-dot"></span> System Online
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="nav-label">NAVIGATION</div>', unsafe_allow_html=True)

    selected = st.radio("", list(PAGES.keys()), label_visibility="collapsed")

    st.markdown('<div class="sidebar-divider"></div>', unsafe_allow_html=True)

    # Quick Stats
    st.markdown('<div class="nav-label">QUICK STATS</div>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="quick-stat">
            <div class="qs-value">94.2%</div>
            <div class="qs-label">Compliance</div>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="quick-stat">
            <div class="qs-value alert-val">12</div>
            <div class="qs-label">Violations</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<br>', unsafe_allow_html=True)
    st.markdown("""
    <div class="sidebar-footer">
        <div>v2.4.1 • AI-Powered</div>
        <div>© 2025 EV-SCAN</div>
    </div>
    """, unsafe_allow_html=True)

# Render selected page
PAGES[selected].show()
