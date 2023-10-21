family_member = {

    "name": "Jane",

    "surname": "Doe",

    "hobbies": ["running", "sky diving", "singing"],

    "age": 35,

    "children": [

        {

            "name": "Alice",

            "age": 6

        },

        {

            "name": "Bob",

            "age": 8

        }

    ]

}
if family_member['children'][1].get('name') == 'Bob':
    print(family_member['children'][1].get('surname', 'Nosurname'))
else:
    print('No Bob')
