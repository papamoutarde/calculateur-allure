import streamlit as st

# Configuration de la page
st.set_page_config(page_title="Calculateur ADC Loches", page_icon="🏃")

# --- INTERFACE ET STYLE ---

# Initialisation du mode nuit dans la session
if 'dark_mode' not in st.session_state:
    st.session_state.dark_mode = False

# Sidebar pour les réglages et le logo
with st.sidebar:
    st.image("https://www.adc-loches.net/media/uploaded/sites/543/association/645fdde057530_logoadcl.JPG", width=150)
    st.title("Options")
    # Bouton pour basculer le mode nuit
    if st.button("🌙 Basculer Mode Nuit / Jour"):
        st.session_state.dark_mode = not st.session_state.dark_mode

# Application du thème dynamique (CSS)
if st.session_state.dark_mode:
    bg_color = "#1E1E1E"  # Gris très foncé
    text_color = "#FFFFFF"
    card_bg = "#2D2D2D"
else:
    bg_color = "#F5F5F5"  # Gris très clair (reposant)
    text_color = "#000000"
    card_bg = "#FFFFFF"

st.markdown(f"""
    <style>
    .stApp {{
        background-color: {bg_color};
        color: {text_color};
    }}
    /* Style des cartes de saisie */
    div[data-testid="stNumberInput"], div[data-testid="stSelectbox"] {{
        background-color: {card_bg};
        padding: 10px;
        border-radius: 10px;
        border: 1px solid #ddd;
    }}
    /* Bloc de résultat toujours bien visible */
    div[data-testid="stNotification"] {{
        background-color: #004a99 !important;
        color: white !important;
        border-radius: 15px;
    }}
    p, h1, h3, label {{
        color: {text_color} !important;
    }}
    </style>
    """, unsafe_allow_html=True)

# --- CONTENU PRINCIPAL ---

st.title("🏃 Calculateur d'allure")
st.write("Outil officiel de l'ADC Loches.")

col_vma, col_dist = st.columns(2)
with col_vma:
    vma = st.number_input("VMA (km/h)", min_value=1.0, value=15.0, step=0.5)
with col_dist:
    distance = st.number_input("Distance (m)", min_value=1.0, value=1000.0, step=10.0)

profils = {
    "Personnalisé": 100.0,
    "Endurance fondamentale (65-75%)": 70.0,
    "Allure Marathon (80-85%)": 82.0,
    "Seuil / Allure 10km (90%)": 90.0,
    "VMA courte (100-105%)": 100.0
}

choix_profil = st.selectbox("Profil d'effort :", list(profils.keys()))
pourcentage = st.number_input("Pourcentage (%)", min_value=1.0, value=profils[choix_profil], step=1.0)

if st.button("🚀 Calculer"):
    vitesse = vma * (pourcentage / 100)
    temps_total_secondes = (distance * 3.6) / vitesse
    
    minutes = int((temps_total_secondes % 3600) // 60)
    secondes = round(temps_total_secondes % 60)
    
    allure_secondes = 3600 / vitesse
    min_allure = int(allure_secondes // 60)
    sec_allure = round(allure_secondes % 60)

    st.divider()
    st.success(f"🎯 Temps à réaliser sur **{distance}m** : \n## **{minutes}min {secondes:02d}sec**")
    
    c1, c2 = st.columns(2)
    c1.metric("Vitesse", f"{vitesse:.2f} km/h")
    c2.metric("Allure", f"{min_allure}:{sec_allure:02d} min/km")

st.caption("ADC Loches - Précision et performance.")










