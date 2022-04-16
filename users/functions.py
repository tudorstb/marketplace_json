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
    pass

def list_users():
    print('Listing users...')

    pass

def update_user():
    pass