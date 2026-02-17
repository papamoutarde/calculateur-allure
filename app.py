import streamlit as st

# Configuration de la page
st.set_page_config(page_title="Calculateur ADC Loches", page_icon="🏃")

# --- INTERFACE ET STYLE ---

if 'dark_mode' not in st.session_state:
    st.session_state.dark_mode = False

with st.sidebar:
    st.image("https://www.adc-loches.net/media/uploaded/sites/543/association/645fdde057530_logoadcl.JPG", width=150)
    st.title("Options")
    if st.button("🌙 Basculer Mode Nuit / Jour"):
        st.session_state.dark_mode = not st.session_state.dark_mode

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
    .stApp {{ background-color: {bg_color}; color: {text_color}; }}
    [data-testid="stSidebar"] {{ background-color: {sidebar_bg} !important; }}
    [data-testid="stSidebar"] .stMarkdown p, [data-testid="stSidebar"] h1 {{ color: {text_color} !important; }}
    div[data-testid="stNumberInput"], div[data-testid="stSelectbox"] {{
        background-color: {card_bg}; padding: 10px; border-radius: 10px; border: 1px solid #444;
    }}
    .stButton > button {{
        color:

