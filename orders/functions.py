from database.functions import *
from users.functions import email_validation
from uuid import uuid4
from datetime import datetime
def find_user_for_order(data):
    users = data["users"]
    # finding user
    while True:

        email = email_validation()
        if email == None:
            return None
        pass_to_date = True
        skip_try_again = False
        for person_id, person in users.items():
            if person['email'] == email:
                print("User found")

                skip_try_again = True
                return person_id

        while skip_try_again == False:
            print('User not found')
            try_again = input('Try again?(Yes/No)=')
            if try_again.lower() == 'no':
                return None
            elif try_again.lower() == 'yes':
                pass_to_date = False

                break
            else:
                print("Did not enter a valid option")

        if pass_to_date == True:
            break
def find_product_for_order(data):
    # finding product
    products = data["products"]

    while True:

        product_name = input("product_name=")
        pass_to_date = True
        skip_try_again = False
        for product_id, product in products.items():
            if product["product_name"] == product_name:
                print("Product found")

                skip_try_again = True
                return product_id

        while skip_try_again == False:
            print('Product not found')
            try_again = input('Try again?(Yes/No)=')
            if try_again.lower() == 'no':
                return None
            elif try_again.lower() == 'yes':
                pass_to_date = False

                break
            else:
                print("Did not enter a valid option")

        if pass_to_date == True:
            break

def create_order():
    print("Creating a order")
    data = read_database()

    user_order_id=find_user_for_order(data)
    product_order_id=find_product_for_order(data)
    order_id = str(uuid4())

    orders=data["orders"]

    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M")
    register_date = current_time

    data['orders'][order_id] = {
        "user_id": user_order_id,
        "product_id": product_order_id,
        "register_date": register_date
    }
    write_database(data)
    print('Done creating order!')


def delete_order():
    pass

def list_orders():
    pass

def list_order():
    # alegeti o varianta..
    # v1 faceti in 2 pasi: prima data luati`va toate id`urile si pe urma alegeti un id, 
    # v2 alternativ puteti da ca input email-ul
    pass

def update_order():
    pass