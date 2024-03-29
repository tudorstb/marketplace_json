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
def email_validation():
    # EXACT un arond
    #special ch
    #explain error
    while True:
        email = input('Input user email: ')

        if email.count('@') != -1 and email.find('.') > -1 and len(email) <= 64 and len(email) >= 5 :
            return email
        else:
            print("Invalid email entered")
            while True:
                retry = input('Try another one(Yes/No):')
                if retry.lower() == 'no':
                    return None
                if retry.lower() == 'yes':
                    break
                else:
                    print('Did not entered a valid option')

def find_email(users):
    while True:

        email=email_validation()
        if email == None:
            return None
        pass_to_date=True
        skip_try_again = False
        for person_id, person in users.items():
            if person['email'] == email:
                print("User found")
                skip_try_again=True
                return email

        while skip_try_again==False:
            print('User not found')
            try_again = input('Try again?(Yes/No)=')
            if try_again.lower() == 'no':
                return None
            elif try_again.lower() == 'yes':
                pass_to_date = False

                break
            else:
                print("Did not enter a valid option")

        if pass_to_date==True:
            break



def user_in_file(way_to_find,user_to_find):
        data = read_database()
        users = data["users"]
        found = False
        for person_id, person in users.items():
            if person[way_to_find] == user_to_find:
                del users[person_id]
                found = True
                break

        return found

def find_user():
    while True:
        way_to_find=input("Choose how to search(name/email):")
        if way_to_find=="name":
            user_to_find=input("Name=")
            if user_in_file(way_to_find,user_to_find)==True:
                return way_to_find,user_to_find
            else:
                while True:
                    retry = input("user not found ,wish to try again?(Yes/No):")
                    if retry.lower()=='no':
                        return None,None
                    elif retry.lower()=='yes':
                        find_user()
                    else:
                        print('Did not entered a valid option')
        elif way_to_find=="email":
            user_to_find = email_validation()
            if user_to_find == None:
                return None, None


            if user_in_file(way_to_find, user_to_find) == True:
                return way_to_find, user_to_find
            else:
                while True:
                    retry = input("user not found ,wish to try again?(Yes/No):")
                    if retry.lower() == 'no':
                        return None, None
                    elif retry.lower() == 'yes':
                        find_user()
                    else:
                        print('Did not entered a valid option')
        print('Did not enter a valid option')

def create_user():
    print('Creaing a user...')
    data = read_database()

    users = data["users"]



    while True:

        email=email_validation()
        if email == None:
            return None
        pass_to_date=True
        for person_id, person in users.items():
            if person['email']== email:
                print("User already registerd")
                while True:
                    try_again=input('Try again?(Yes/No)=')
                    if try_again.lower()== 'no':
                        return None
                    elif try_again.lower()=='yes':
                        pass_to_date=False
                        break
                    else:
                        print("Did not enter a valid option")
        if pass_to_date==True:
            break
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M")
    register_date = current_time
    user_id = str(uuid4())
    # register_date = datetime.......
    name = input('Input your user name: ')


    data['users'][user_id] = {
        "name": name,
        "email": email,
        "register_date": register_date
    }
    write_database(data)
    print('Done creating user!')

def delete_user():
    data = read_database()

    users = data["users"]

    email=find_email(users)
    if email==None:
        return None

    print('Deleting user...')

    found=False
    for person_id, person in users.items():
        if person['email'] == email:
            del users[person_id]
            found = True
            break
    if found == False:
        print("")

    write_database(data)

def list_user():
    # alegeti o varianta..
    # v1 faceti in 2 pasi: prima data luati`va toate id`urile si pe urma alegeti un id, 
    # v2 alternativ puteti da ca input email-ul
    way_to_find,user_to_find=find_user()

    if way_to_find == None and user_to_find == None:
        return None

    data = read_database()
    print('Listing user...')
    users = data["users"]
    for person_id, person in users.items():
        if person[way_to_find]==user_to_find:
            print(f'\nid={person_id}')
            print(f'name={person["name"]}')
            print(f'email={person["email"]}')
            #pot sa pun break??

def list_users():
    print('Listing users...')
    data = read_database()
    users=data["users"]
    for person_id, person in users.items():
        print(person["name"])
    print('________________')
#password
def update_user():
    option_list=['name','email','exit']
    data = read_database()
    users=data['users']

    email_of_user = find_email(users)
    if email_of_user == None:
        return None

    updated_name=''
    updated_email=''

    def update_option(updated_name,updated_email):
        while True:
            update_entry=input('Choose what you whis to update:')
            if update_entry.lower()=='name':
                updated_name=input("New name=")
                return updated_name,updated_email
            elif update_entry.lower()=='email':

                updated_email=email_validation()
                if update_entry == None:
                    return None
                return updated_name,updated_email
            elif update_entry.lower()=='exit':
                return updated_name,updated_email
            elif update_entry.lower()=='help':
                print(f'options-> {option_list}')
            else:
                print(f'Did not enterd a valid option-> {option_list}')
    updated_name,updated_email=update_option(updated_name,updated_email)
    while True:
        update_more = input('Update something else(yes/no):').lower()
        if update_more == 'yes':
            updated_name, updated_email = update_option(updated_name, updated_email)
        elif update_more == 'no':
            break
        else:
            print('Did not entered a valid option')

    print('Updating a user...')

    for person_id, person in users.items():
        if person['email'] == email_of_user:
            if updated_name !='':
                person["name"]=updated_name
            elif updated_email !='':
                person["email"]=updated_email
    write_database(data)
    print('Done updating the user!')