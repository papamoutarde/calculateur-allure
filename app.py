import streamlit as st

# Configuration de la page
st.set_page_config(page_title="Calculateur allure - ADC Loches", page_icon="🏃")

def add_bg_logo(url):
    st.markdown(
        f"""
        <style>
        /* Arrière-plan global avec logo plus visible */
        .stApp {{
            background-image: linear-gradient(rgba(255, 255, 255, 0.4), rgba(255, 255, 255, 0.4)), 
                              url("{url}");
            background-size: 70%;
            background-repeat: no-repeat;
            background-attachment: fixed;
            background-position: center;
        }}

        /* Bloc de résultat opaque pour cacher le logo derrière le texte */
        div[data-testid="stNotification"] {{
            background-color: rgba(255, 255, 255, 1) !important;
            border: 2px solid #004a99; /* Bleu club optionnel */
            border-radius: 10px;
            padding: 20px;
            opacity: 1 !important;
            box-shadow: 0px 4px 15px rgba(0,0,0,0.1);
        }}
        
        /* Amélioration de la lisibilité des labels */
        .stNumberInput label, .stSelectbox label {{
            background-color: rgba(255,255,255,0.8);
            padding: 2px 5px;
            border-radius: 5px;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Application du logo ADC Loches
add_bg_logo("https://www.adc-loches.net/media/uploaded/sites/543/association/645fdde057530_logoadcl.JPG")

st.title("🏃 Calculateur d'allure")
st.write("Sélectionnez votre profil d'effort ou entrez vos données personnalisées.")

# --- SECTION SAISIE ---

col_vma, col_dist = st.columns(2)

with col_vma:
    vma = st.number_input("Saisissez votre VMA (km/h)", min_value=1.0, value=15.0, step=0.5)

with col_dist:
    distance = st.number_input("Distance à parcourir (m)", min_value=1.0, value=1000.0, step=10.0)

# Dictionnaire des profils d'effort
profils = {
    "Personnalisé": 100.0,
    "Endurance fondamentale (65-75%)": 70.0,
    "Allure Marathon (80-85%)": 82.0,
    "Seuil / Allure 10km (90%)": 90.0,
    "VMA courte (100-105%)": 100.0,
    "VMA Sprint (110%+)": 110.0
}

# Sélecteur de profil
choix_profil = st.selectbox("Choisir un profil d'effort :", list(profils.keys()))

# Le pourcentage est pré-rempli selon le profil mais reste modifiable
pourcentage = st.number_input(
    "Pourcentage de VMA (%)", 
    min_value=1.0, 
    max_value=250.0, 
    value=profils[choix_profil], 
    step=1.0
)

# --- SECTION CALCUL ---

if st.button("🚀 Calculer le temps"):
    try:
        # 1. Calcul de la vitesse cible
        vitesse = vma * (pourcentage / 100)
        
        # 2. Calcul du temps total
        temps_total_secondes = (distance * 3.6) / vitesse
        
        heures = int(temps_total_secondes // 3600)
        minutes = int((temps_total_secondes % 3600) // 60)
        secondes = round(temps_total_secondes % 60)

        # 3. Allure au kilomètre
        allure_secondes = 3600 / vitesse
        min_allure = int(allure_secondes // 60)
        sec_allure = round(allure_secondes % 60)

        # Affichage du bloc opaque
        st.divider()
        
        if heures > 0:
            temps_texte = f"{heures}h {minutes}min {secondes:02d}sec"
        else:
            temps_texte = f"{minutes}min {secondes:02d}sec"

        st.success(f"🎯 Pour **{distance}m** à **{pourcentage}%** de VMA :\n## **{temps_texte}**")
        
        # Détails en colonnes
        c1, c2 = st.columns(2)
        with c1:
            st.metric("Vitesse cible", f"{vitesse:.2f} km/h")
        with c2:
            st.metric("Allure au kilo", f"{min_allure}:{sec_allure:02d} min/km")

    except Exception as e:
        st.error("Calcul impossible. Vérifiez que la VMA est supérieure à 0.")

# Petit rappel en bas de page
st.caption("Outil développé pour les coureurs de l'ADC Loches.")









