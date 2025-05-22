import streamlit as st
import read_data # Ergänzen Ihr eigenes Modul
from PIL import Image

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
col1, col2 = st.columns(2)
with col1:
    st.session_state.current_user = st.selectbox(
        'Versuchsperson',
        options = person_list, key="sbVersuchsperson")

        # Anlegen des Session State. Bild, wenn es kein Bild gibt
if 'picture_path' not in st.session_state:
        st.session_state.picture_path = 'data/pictures/none.jpg'

    # ...

    # Suche den Pfad zum Bild, aber nur wenn der Name bekannt ist
if st.session_state.current_user in person_list:
        st.session_state.picture_path = read_data.find_person_data_by_name(st.session_state.current_user)["picture_path"]

    # ...

    # Öffne das Bild und Zeige es an
with col2: 
    image = Image.open(st.session_state.picture_path)
    st.image(image, caption=st.session_state.current_user)