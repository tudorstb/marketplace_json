from datetime import datetime
from uuid import uuid4


from database.functions import read_database, write_database



# user template:
# {
#     "b4da16a1-b23f-42c8-aff0-371539fe1553": {
#         "name": "John Doe",
#         "email": "john_doe@gmail.com",
#         "register_date": "2022-04-13 20:44"
# }


def create_user():
    print('Creaing a user...')
    data = read_database()
    print(data)

    user_id = str(uuid4())
    name = input('Input your user name: ')
    email = input('Input your user email: ') # ar trebui o verificare ca intr`adevar avem un email valid
    now = datetime.now()
    current_time = now.strftime("%y-%m-%d %H:%M")
    register_date = current_time
    # register_date = datetime.......

    data['users'][user_id] = {
        "name": name,
        "email": email,
        "register_date": register_date
    }
    write_database(data)
    print('Done creating user!')
    
def delete_user():

    pass


def list_user():
    # alegeti o varianta..
    # v1 faceti in 2 pasi: prima data luati`va toate id`urile si pe urma alegeti un id, 
    # v2 alternativ puteti da ca input email-ul
    while True:
        way_to_find=input("Choose how to search(name/email):")
        if way_to_find=="name":
            user_to_find=input("Name=")
            break
        elif way_to_find=="email":
            user_to_find = input("Email=")
            break
        print('Did not enter a valid option')

    print('Listing user...')
    data = read_database()
    users = data["users"]
    for person_id, person in users.items():
        if person[way_to_find]==user_to_find:
            print(f'\nid={person_id}')
            print(f'name={person["name"]}')
            print(f'email={person["email"]}')
def list_users():
    print('Listing users...')
    data = read_database()
    users=data["users"]
    for person_id, person in users.items():
        print(person["name"])
    print('________________')

def update_user():
    pass