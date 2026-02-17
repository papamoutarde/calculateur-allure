import streamlit as st

# Configuration de la page
st.set_page_config(page_title="Calculateur ADC Loches", page_icon="🏃")

# --- INTERFACE ET STYLE ---

if 'dark_mode' not in st.session_state:
    st.session_state.dark_mode = False

# Sidebar avec le logo et le bouton mode nuit
with st.sidebar:
    st.image("https://www.adc-loches.net/media/uploaded/sites/543/association/645fdde057530_logoadcl.JPG", width=150)
    st.title("Options")
    if st.button("🌙 Basculer Mode Nuit / Jour"):
        st.session_state.dark_mode = not st.session_state.dark_mode

# Définition des couleurs selon le mode choisi
if st.session_state.dark_mode:
    bg_color = "#1E1E1E"    
    sidebar_bg = "#262730"  
    text_color = "#FFFFFF"  
    card_bg = "#2D2D2D"     
    btn_text = "#FFFFFF"    
else:
    bg_color = "#F5F5F5"
    sidebar_bg = "#FFFFFF"
    text_color = "#000000"
    card_bg = "#FFFFFF"
    btn_text = "#000000"

st.markdown(f"""
    <style>
    .stApp {{
        background-color: {bg_color};
        color: {text_color};
    }}
    
    [data-testid="stSidebar"] {{
        background-color: {sidebar_bg} !important;
    }}
    
    [data-testid="stSidebar"] .stMarkdown p, [data-testid="stSidebar"] h1 {{
        color: {text_color} !important;
    }}

    div[data-testid="stNumberInput"], div[data-testid="stSelectbox"] {{
        background-color: {card_bg};
        padding: 10px;
        border-radius: 10px;
        border: 1px solid #444;
    }}

    .stButton > button {{
        color: {btn_text} !important;
        background-color: {card_bg} !important;
        border: 1px solid #004a99 !important;
        width: 100%;
        font-weight: bold;
        height: 3em;
    }}

    div[data-testid="stNotification"] {{
        background-color: #004a99 !important;
        color: white !important;
        border-radius: 15px;
    }}
    
    label, p, h1, h2, h3 {{
        color: {text_color} !important;
    }}
    </style>
    """, unsafe_allow_html=True)

# --- CONTENU PRINCIPAL ---

st.title("🏃 Calculateur d'allure")

col_vma, col_dist = st.columns(2)
with col_vma:
    vma = st.number_input("VMA (km/h)", min_value=1.0, value=15.0, step=0.5)
with col_dist:
    distance = st.number_input("Distance totale (m)", min_value=1.0, value=1000.0, step=10.0)

# Nouvelle option pour l'intervalle des temps de passage
intervalle = st.number_input("Temps de passage tous les (m) :", min_value=10.0, value=400.0, step=50.0, help="Optionnel : réglez la distance pour chaque temps de passage (ex: 200m, 400m, 1000m)")

profils = {
    "Personnalisé": 100.0,
    "Endurance fondamentale (65-75%)": 70.0,
    "Allure Marathon (80-85%)": 82.0,
    "Seuil / Allure 10km (90%)": 90.0,
    "VMA courte (100-105%)": 100.0
}

choix_profil = st.selectbox("Profil d'effort :", list(profils.keys()))
pourcentage = st.number_input("Pourcentage (%)", min_value=1.0, value=profils[choix_profil], step=1.0)

if st.button("🚀 Calculer les temps"):
    try:
        vitesse = vma * (pourcentage / 100)
        
        # Temps total
        temps_total_sec = (distance * 3.6) / vitesse
        min_total = int(temps_total_sec // 60)
        sec_total = round(temps_total_sec % 60)
        
        st.divider()
        st.success(f"🎯 Temps total pour **{distance}m** :  \n## **{min_total}min {sec_total:02d}sec**")
        
        # --- TABLEAU DES TEMPS DE PASSAGE PERSONNALISÉ ---
        st.subheader(f"⏱️ Passages tous les {int(intervalle)}m")
        
        # On boucle par l'intervalle choisi
        for d_pass in range(int(intervalle), int(distance) + 1, int(intervalle)):
            t_pass_sec = (d_pass * 3.6) / vitesse
            m_p = int(t_pass_sec // 60)
            s_p = round(t_pass_sec % 60)
            # Calcul du numéro du passage
            num_passage = d_pass // int(intervalle)
            st.write(f"**Passage {num_passage}** ({d_pass}m) : `{m_p}min {s_p:02d}s`")
        
        # Si la distance finale n'a pas été affichée (pas un multiple de l'intervalle)
        if distance % intervalle != 0:
            st.write(f"**Arrivée** ({distance}m) : `{min_total}min {sec_total:02d}s`")

        st.divider()
        
        # Metrics techniques
        allure_secondes = 3600 / vitesse
        min_allure = int(allure_secondes // 60)
        sec_allure = round(allure_secondes % 60)
        
        c1, c2 = st.columns(2)
        c1.metric("Vitesse", f"{vitesse:.2f} km/h")
        c2.metric("Allure au km", f"{min_allure}:{sec_allure:02d}")
        
    except Exception:
        st.error("Une erreur est survenue. Vérifiez vos données de saisie.")

