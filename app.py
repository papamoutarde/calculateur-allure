import streamlit as st

# Configuration de la page
st.set_page_config(page_title="Calculateur allure", page_icon="🏃")

def add_bg_logo(url):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: linear-gradient(rgba(255, 255, 255, 0.85), rgba(255, 255, 255, 0.2)), 
                              url("{url}");
            background-size: 75%; /* Taille du logo */
            background-repeat: no-repeat;
            background-attachment: fixed;
            background-position: center;
        }}

        div[data-testid="stNotification"] {{
            background-color: rgba(255, 255, 255, 1) !important; /* Fond blanc pur */
            border: 2px solid #000;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Remplace par l'URL de l'image de ton club
add_bg_logo("https://www.adc-loches.net/media/uploaded/sites/543/association/645fdde057530_logoadcl.JPG")

st.title("🏃 Calculateur d'allure")
st.write("Entrez vos paramètres pour calculer votre temps de passage.")

# Champs de saisie
vma = st.number_input("VMA (km/h)", min_value=1.0, value=15.0, step=0.5)
pourcentage = st.number_input("Pourcentage (%)", min_value=1.0, max_value=200.0, value=100.0, step=1.0)
distance = st.number_input("Distance (m)", min_value=1.0, value=1000.0, step=10.0)

# Bouton de calcul
if st.button("Calculer"):
    try:
        # 1. Calcul de la vitesse cible (km/h)
        vitesse = vma * (pourcentage / 100)
        
        # 2. Calcul du temps total en secondes
        temps_total_secondes = (distance * 3.6) / vitesse
        
        # Conversion intelligente en H:M:S
        heures = int(temps_total_secondes // 3600)
        minutes = int((temps_total_secondes % 3600) // 60)
        secondes = round(temps_total_secondes % 60)

        # 3. Calcul de l'allure au kilomètre (toujours en min:sec/km)
        allure_secondes = 3600 / vitesse
        min_allure = int(allure_secondes // 60)
        sec_allure = round(allure_secondes % 60)

        # Affichage des résultats
        st.divider()
        
        # Construction du texte de temps total
        if heures > 0:
            temps_texte = f"{heures}h {minutes}min {secondes:02d}sec"
        else:
            temps_texte = f"{minutes}min {secondes:02d}sec"

        st.success(f"🎯 Temps à réaliser sur **{distance}m** :  \n### **{temps_texte}**")
        
        # Détails techniques dans des colonnes
        col1, col2 = st.columns(2)
        
        with col1:
            st.metric("Vitesse cible", f"{vitesse:.2f} km/h")
            
        with col2:
            st.metric("Allure au kilo", f"{min_allure}:{sec_allure:02d} min/km")

    except Exception as e:
        st.error("Une erreur est survenue lors du calcul. Vérifiez vos saisies.")






