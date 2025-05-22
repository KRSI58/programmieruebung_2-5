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

if __name__ == "__main__":
    # Test the function
    person_data = load_person_data()
    #print(person_data)
    person_list = get_person_list()
    print(person_list)