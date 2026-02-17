


# Code pour l'arrière-plan
page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://github.com/papamoutarde/calculateur-allure/blob/main/645fdde057530_logoadcl.JPG?raw=true");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
}

/* Optionnel : rend le texte plus lisible en ajoutant un voile blanc sur l'image */
[data-testid="stAppViewContainer"]::before {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(255, 255, 255, 0.7); /* 0.7 = transparence (0 à 1) */
    z-index: -1;
}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)



import streamlit as st

# Configuration de la page
st.set_page_config(page_title="Calculateur allure", page_icon="🏃")

st.title("🏃 Calculateur d'allure")
st.write("Entrez vos paramètres pour calculer votre temps de passage.")

# Création des champs de saisie (remplace les Entry de tkinter)
vma = st.number_input("VMA (km/h)", min_value=1.0, value=15.0, step=0.5)
pourcentage = st.number_input("Pourcentage (%)", min_value=1.0, max_value=200.0, value=100.0, step=1.0)
distance = st.number_input("Distance (m)", min_value=1.0, value=1000.0, step=10.0)

# Le bouton de calcul
if st.button("Calculer"):
    try:
        # Calculs (ton algorithme original)
        vitesse = vma * (pourcentage / 100)
        temps_total_secondes = (distance * 3.6) / vitesse

        minutes = int(temps_total_secondes // 60)
        secondes = round(temps_total_secondes % 60)

        # Affichage du résultat (remplace le Label/messagebox)
        st.success(f"✅ Temps à réaliser : **{minutes} min {secondes:02d} sec**")
        
        # Petit bonus : la vitesse réelle en km/h
        st.info(f"Vitesse cible : {vitesse:.2f} km/h")

    except Exception as e:
        st.error("Une erreur est survenue lors du calcul.")
