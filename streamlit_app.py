"""
Altersabfrage Web-App mit Streamlit
Design basierend auf IhreMakler.online CI
Farben: Türkis #17A2B8 & Dunkelblau #003f5c
"""

import streamlit as st

# Seite konfigurieren
st.set_page_config(
    page_title="Altersabfrage | IhreMakler", 
    page_icon="🏠", 
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS für IhreMakler CI mit Header, Content und Footer
st.markdown("""
<style>
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }
    
    /* Main Container */
    .main {
        background-color: #ffffff;
    }
    
    /* HEADER STYLING */
    .header-wrapper {
        background-color: #f9f9f9;
        padding: 1rem 0;
        border-bottom: 2px solid #062E52;
    }
    
    .header-container {
        display: flex;
        align-items: center;
        justify-content: flex-start;
        gap: 1.5rem;
        padding: 0 2rem;
        max-width: 100%;
    }
    
    .logo-section {
        display: flex;
        align-items: center;
        flex-shrink: 0;
    }
    
    .logo-image {
        height: 120px;
        width: auto;
        object-fit: contain;
    }
    
    .text-section {
        display: flex;
        flex-direction: column;
        justify-content: center;
        gap: 0.2rem;
    }
    
    .header-title {
        margin: 0;
        font-size: 1.8rem;
        font-weight: 700;
        color: #062E52;
        font-family: Arial, Verdana, sans-serif;
    }
    
    .header-tagline {
        margin: 0;
        font-size: 0.95rem;
        color: #3B8EA0;
        font-weight: 500;
        font-family: Arial, Verdana, sans-serif;
    }
    
    /* MAIN CONTENT */
    .main-header {
        background-color: #062E52;
        padding: 3rem 2rem;
        border-radius: 0;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
        font-family: Arial, Verdana, sans-serif;
    }
    
    .main-header h1 {
        margin: 0;
        font-size: 2.5em;
        font-weight: 700;
        font-family: Arial, Verdana, sans-serif;
    }
    
    .main-header p {
        margin: 0.8rem 0 0 0;
        font-size: 1em;
        font-weight: 300;
        font-family: Arial, Verdana, sans-serif;
    }
    
    /* BUTTONS */
    .stButton > button {
        background-color: #3B8EA0 !important;
        color: #f5f5f5 !important;
        border: none !important;
        border-radius: 4px !important;
        padding: 0.8rem 1.5rem !important;
        font-weight: 600 !important;
        font-family: Arial, Verdana, sans-serif !important;
        transition: background-color 0.3s ease !important;
    }
    
    .stButton > button:hover {
        background-color: #2d6b78 !important;
    }
    
    /* INPUT */
    .stNumberInput input {
        border-color: #062E52 !important;
        border-radius: 4px !important;
        font-family: Arial, Verdana, sans-serif !important;
    }
    
    /* RESULT BOXES */
    .result-box {
        border-left: 5px solid #3B8EA0;
        padding: 1.5rem;
        border-radius: 0;
        background-color: #f5f5f5;
        margin: 1.5rem 0;
        font-family: Arial, Verdana, sans-serif;
    }
    
    .success-box {
        border-left-color: #28a745;
        background-color: #f0f8f5;
    }
    
    .warning-box {
        border-left-color: #ffc107;
        background-color: #fff8f0;
    }
    
    /* FOOTER */
    .footer-container {
        background-color: #f9f9f9;
        border-top: 1px solid #062E52;
        padding: 2rem;
        margin-top: 3rem;
        font-family: Arial, Verdana, sans-serif;
    }
    
    .footer-content {
        display: flex;
        justify-content: space-between;
        align-items: flex-start;
        flex-wrap: wrap;
        gap: 2rem;
        margin-bottom: 2rem;
    }
    
    .footer-section {
        flex: 1;
        min-width: 200px;
    }
    
    .footer-section h4 {
        color: #062E52;
        font-size: 0.9rem;
        font-weight: 700;
        margin-bottom: 0.8rem;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        font-family: Arial, Verdana, sans-serif;
    }
    
    .footer-section ul {
        list-style: none;
        padding: 0;
    }
    
    .footer-section li {
        margin-bottom: 0.5rem;
    }
    
    .footer-section a {
        color: #062E52;
        text-decoration: none;
        font-size: 0.9rem;
        font-family: Arial, Verdana, sans-serif;
        transition: color 0.3s ease;
    }
    
    .footer-section a:hover {
        color: #3B8EA0;
        font-weight: bold;
    }
    
    .footer-bottom {
        border-top: 1px solid #d0d0d0;
        padding-top: 1.5rem;
        text-align: center;
        color: #666;
        font-size: 0.85rem;
        font-family: Arial, Verdana, sans-serif;
    }
    
    .footer-logo {
        color: #062E52;
        font-weight: 700;
    }
    
    .footer-tagline {
        color: #062E52;
        font-size: 0.85rem;
        font-style: normal;
    }
</style>
""", unsafe_allow_html=True)

# HEADER mit Logo
# HEADER mit Logo
try:
    # Versuche erst lokal zu laden
    logo_path = Path(__file__).parent / "Dateien" / "Altersabfrage" / "Logo1.png"
    if logo_path.exists():
        st.image(str(logo_path), width=400)
    else:
        raise FileNotFoundError
except (FileNotFoundError, Exception):
    # Fallback: Von GitHub laden (für Streamlit Cloud)
    st.image("https://raw.githubusercontent.com/IhreMakler/altersabfrage-app/main/Dateien/Altersabfrage/Logo1.png", width=400)

st.divider()
</div>
""", unsafe_allow_html=True)

# Beschreibung mit zentriertem Layout
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.markdown("""
    <p style="text-align: center; color: #555; margin-bottom: 2rem; font-size: 1.05em;">
    Geben Sie Ihr Alter ein und lassen Sie es überprüfen - schnell, vertraulich und zuverlässig.
    </p>
    """, unsafe_allow_html=True)

# Initialisiere Session State für Eingabe und Ergebnis
if "age_input" not in st.session_state:
    st.session_state.age_input = None
Geben Sie Ihr Alter ein und lassen Sie es überprüfen - schnell, vertraulich und zuverlässig.
    st.session_state.result_message = None
if "show_result" not in st.session_state:
    st.session_state.show_result = False

# Eingabebereich mit zentriertem Layout
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.markdown("### Altersverifikation")
    age = st.number_input(
        "Bitte geben Sie Ihr Alter ein:",
        min_value=0,
        max_value=120,
        value=None,
        step=1,
        help="Gültige Angabe: 0 bis 120 Jahre"
    )
    
    check_button = st.button("✓ Überprüfen", use_container_width=True, key="check_btn")

# Validierung und Verarbeitung
if check_button and age is not None:
    st.session_state.age_input = age
    st.session_state.show_result = True

# Ergebnis anzeigen
if st.session_state.show_result and st.session_state.age_input is not None:
    age_val = st.session_state.age_input
    st.markdown("")
    
    if age_val < 18:
        st.markdown(f"""
        <div class="result-box warning-box">
            <h3 style="color: #ff6b6b; margin-top: 0;">⛔ Altersverifikation nicht bestandenen</h3>
            <p><strong>Ihr Alter:</strong> {age_val} Jahre</p>
            <p>Leider erfüllen Sie die Altersanforderung nicht. Sie müssen mindestens 18 Jahre alt sein, um fortzufahren.</p>
            <p><small style="color: #999;">Falls Sie Fragen haben, kontaktieren Sie uns gerne.</small></p>
        </div>
        """, unsafe_allow_html=True)
    elif age_val > 18:
        st.markdown(f"""
        <div class="result-box success-box">
            <h3 style="color: #28a745; margin-top: 0;">✅ Altersverifikation bestanden</h3>
            <p><strong>Ihr Alter:</strong> {age_val} Jahre</p>
            <p>Herzlichen Glückwunsch! Sie erfüllen die Altersanforderung und können jetzt fortfahren.</p>
            <p><small style="color: #999;">Vielen Dank für Ihre Geduld. Wir freuen uns, Ihnen weiterhelfen zu können.</small></p>
        </div>
        """, unsafe_allow_html=True)
    else:  # age_val == 18
        st.markdown(f"""
        <div class="result-box success-box">
            <h3 style="color: #28a745; margin-top: 0;">✅ Altersverifikation bestanden</h3>
            <p><strong>Ihr Alter:</strong> Genau 18 Jahre</p>
            <p>Herzlichen Glückwunsch! Sie erfüllen die Altersanforderung und können jetzt fortfahren.</p>
            <p><small style="color: #999;">Vielen Dank für Ihre Geduld. Wir freuen uns, Ihnen weiterhelfen zu können.</small></p>
        </div>
        """, unsafe_allow_html=True)

# Neuerliche Eingabe
if st.session_state.show_result:
    st.markdown("")
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🔄 Neue Überprüfung", use_container_width=True):
            st.session_state.show_result = False
            st.session_state.age_input = None
            st.rerun()

# FOOTER
st.markdown("""
<style>
    .reportview-container .main footer {
        display: none;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="footer-container">
    <div class="footer-content">
        <div class="footer-section">
            <h4>Unternehmen</h4>
            <ul>
                <li><a href="https://www.ihremakler.online/team/">Unser Team</a></li>
                <li><a href="https://www.ihremakler.online/">Startseite</a></li>
                <li><a href="https://www.ihremakler.online/immobilienbewertung/">Immobilienbewertung</a></li>
            </ul>
        </div>
        <div class="footer-section">
            <h4>Services</h4>
            <ul>
                <li><a href="https://www.ihremakler.online/immobilie-verkaufen/">Immobilie verkaufen</a></li>
                <li><a href="https://www.ihremakler.online/immobilie-kaufen/">Immobilie kaufen</a></li>
                <li><a href="https://www.ihremakler.online/finanzierungsrechner/">Finanzierungsrechner</a></li>
            </ul>
        </div>
        <div class="footer-section">
            <h4>Rechtliches</h4>
            <ul>
                <li><a href="https://www.ihremakler.online/impressum/">Impressum</a></li>
                <li><a href="https://www.ihremakler.online/datenschutz/">Datenschutz</a></li>
                <li><a href="https://www.ihremakler.online/agb/">AGB</a></li>
                <li><a href="https://www.ihremakler.online/widerrufsbelehrung/">Widerrufsbelehrung</a></li>
            </ul>
        </div>
        <div class="footer-section">
            <h4>Zugang</h4>
            <ul>
                <li><a href="https://www.ihremakler.online/barrierefreiheit/">Barrierefreiheit</a></li>
                <li><a href="https://www.ihremakler.online/#kontakt">Kontakt</a></li>
            </ul>
        </div>
    </div>
    <div class="footer-bottom">
        <p style="margin: 0.5rem 0;">
            <span class="footer-logo">© 2026 Ihre Makler GmbH</span><br>
            <span class="footer-tagline">Lokal • Schnell • Fair</span>
        </p>
    </div>
</div>
""", unsafe_allow_html=True)



