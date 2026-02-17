import streamlit as st

# Configuration de la page
st.set_page_config(page_title="Calculateur allure", page_icon="🏃")

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
        
        # 2. Calcul du temps total pour la distance donnée
        temps_total_secondes = (distance * 3.6) / vitesse
        min_tot = int(temps_total_secondes // 60)
        sec_tot = round(temps_total_secondes % 60)

        # 3. Calcul de l'allure au kilomètre (temps pour 1 km)
        # Formule : 3600 / vitesse donne le nombre de secondes par km
        allure_secondes = 3600 / vitesse
        min_allure = int(allure_secondes // 60)
        sec_allure = round(allure_secondes % 60)

        # Affichage des résultats
        st.divider()
        
        # Résultat principal : Temps total
        st.success(f"🎯 Temps à réaliser sur **{distance}m** :  \n### **{min_tot} min {sec_tot:02d} sec**")
        
        # Détails techniques dans des colonnes
        col1, col2 = st.columns(2)
        
        with col1:
            st.metric("Vitesse cible", f"{vitesse:.2f} km/h")
            
        with col2:
            # Affichage de l'allure au kilo (ex: 6:00 min/km)
            st.metric("Allure au kilo", f"{min_allure}:{sec_allure:02d} min/km")

    except Exception as e:
        st.error("Une erreur est survenue lors du calcul. Vérifiez vos saisies.")
