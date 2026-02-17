import streamlit as st

# Configuration de la page
st.set_page_config(page_title="Calculateur allure", page_icon="🏃")

st.title("🏃 Calculateur d'allure")
st.write("Entrez vos paramètres ou utilisez les raccourcis de distance.")

# --- SECTION RACCOURCIS ---
st.write("**Distances rapides :**")
col_r1, col_r2, col_r3, col_r4, col_r5 = st.columns(5)

# On utilise une variable de session pour stocker la distance
if 'dist_val' not in st.session_state:
    st.session_state.dist_val = 1000.0

with col_r1:
    if st.button("1000m"): st.session_state.dist_val = 1000.0
with col_r2:
    if st.button("5 km"): st.session_state.dist_val = 5000.0
with col_r3:
    if st.button("10 km"): st.session_state.dist_val = 10000.0
with col_r4:
    if st.button("Semi"): st.session_state.dist_val = 21097.0
with col_r5:
    if st.button("Marathon"): st.session_state.dist_val = 42195.0

# --- CHAMPS DE SAISIE ---
vma = st.number_input("VMA (km/h)", min_value=1.0, value=15.0, step=0.5)
pourcentage = st.number_input("Pourcentage (%)", min_value=1.0, max_value=200.0, value=100.0, step=1.0)
# La distance utilise la valeur de la session state
distance = st.number_input("Distance (m)", min_value=1.0, value=st.session_state.dist_val, step=10.0, key="dist_input")

# --- CALCUL ---
if st.button("🚀 Calculer", type="primary"):
    try:
        # 1. Calcul de la vitesse cible (km/h)
        vitesse = vma * (pourcentage / 100)
        
        # 2. Calcul du temps total en secondes
        temps_total_secondes = (distance * 3.6) / vitesse
        
        # Conversion H:M:S
        heures = int(temps_total_secondes // 3600)
        minutes = int((temps_total_secondes % 3600) // 60)
        secondes = round(temps_total_secondes % 60)

        # 3. Calcul de l'allure au kilomètre
        allure_secondes = 3600 / vitesse
        min_allure = int(allure_secondes // 60)
        sec_allure = round(allure_secondes % 60)

        # --- AFFICHAGE ---
        st.divider()
        
        if heures > 0:
            temps_texte = f"{heures}h {minutes}min {secondes:02d}sec"
        else:
            temps_texte = f"{minutes}min {secondes:02d}sec"

        st.success(f"🎯 Temps à réaliser sur **{distance:,.0f}m** :  \n### **{temps_texte}**")
        
        c1, c2 = st.columns(2)
        with c1:
            st.metric("Vitesse cible", f"{vitesse:.2f} km/h")
        with c2:
            st.metric("Allure au kilo", f"{min_allure}:{sec_allure:02d} min/km")

    except Exception as e:
        st.error("Erreur de calcul. Vérifiez les données.")
