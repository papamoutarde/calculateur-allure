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

