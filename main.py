import streamlit as st
import read_data # Ergänzen Ihr eigenes Modul

st.write("# EKG APP")
st.write("## Versuchsperson auswählen")

# Session State wird leer angelegt, solange er noch nicht existiert
if 'current_user' not in st.session_state:
    st.session_state.current_user = 'None'


st.write("Der Name ist: ", st.session_state.current_user) 


# Legen Sie eine neue Liste mit den Personennamen an indem Sie ihre 
# Funktionen aufrufen
person_data = read_data.load_person_data()
person_list = read_data.get_person_list()
# bzw: wenn Sie nicht zwei separate Funktionen haben
# person_names = read_data.get_person_list()

# Nutzen Sie ihre neue Liste anstelle der hard-gecodeten Lösung
st.session_state.current_user = st.selectbox(
    'Versuchsperson',
    options = person_list, key="sbVersuchsperson")