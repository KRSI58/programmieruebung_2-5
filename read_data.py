import json

def load_person_data():
    """A Function that knows where the person database is and returns a dictionary with the persons"""
    file = open("data/person_db.json")
    person_data = json.load(file)
    return person_data

def get_person_list():
    """A function that returns a list of persons"""
    person_data = load_person_data()
    person_list = []
    for person in person_data:
        person_list.append(person["lastname"] + " " + person["firstname"])
    return person_list

def find_person_data_by_name(name_search):
    """A function that returns the data of a person by their name"""
    person_data = load_person_data()
    for person in person_data:
        if person["lastname"] + " " + person["firstname"] == name_search:
            return person
    # If no person is found, return None
    return None

def picture_display():
        # Anlegen des Session State. Bild, wenn es kein Bild gibt
    if 'picture_path' not in st.session_state:
        st.session_state.picture_path = 'data/pictures/none.jpg'

    # ...

    # Suche den Pfad zum Bild, aber nur wenn der Name bekannt ist
    if st.session_state.current_user in person_names:
        st.session_state.picture_path = read_data.find_person_data_by_name(st.session_state.current_user)["picture_path"]

    # ...

    # Öffne das Bild und Zeige es an
    image = Image.open("../" + st.session_state.picture_path)
    st.image(image, caption=st.session_state.current_user)

    

if __name__ == "__main__":
    # Test the function
    person_data = load_person_data()
    #print(person_data)
    person_list = get_person_list()
    print(person_list)