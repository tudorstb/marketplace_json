from database.functions import *
from users.functions import email_validation
from uuid import uuid4
from datetime import datetime
from tabulate import tabulate
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

def find_order(data):
    orders = data["orders"]
    users = data['users']
    products = data['products']
    while True:
        product_id_to_find=find_product_for_order(data)
        if product_id_to_find==None:
            return None
        user_id_to_find=find_user_for_order(data)
        if user_id_to_find == None:
            return None

        ids_to_return=[]

        for order_id, order in orders.items():
            if product_id_to_find == order["product_id"] and user_id_to_find == order['user_id']:
                ids_to_return.append(order_id)
        if ids_to_return != []:
            return ids_to_return
        print('Order not found')
        while True:
            try_again = input('Try again?(Yes/No)=')
            if try_again.lower() == 'no':
                return None
            elif try_again.lower() == 'yes':
                break
            else:
                print("Did not enter a valid option")





def create_order():
    print("Creating a order")
    data = read_database()

    user_order_id=find_user_for_order(data)
    if user_order_id==None:
        return None
    product_order_id=find_product_for_order(data)
    if product_order_id==None:
        return None
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
    data = read_database()
    users = data['users']
    products = data['products']


    pass

def list_orders():
    print('Listing orders...')
    data = read_database()
    users = data['users']
    products = data['products']
    orders = data["orders"]

    table=[]
    for order_id, order in orders.items():
        try:
            table.append([order_id,users[order['user_id']]['name'],products[order['product_id']]['product_name']])
        except:
            pass
    print(tabulate(table,headers=["order id","user","product"]))


def list_order():
    print('Listing order...')
    data = read_database()
    users = data['users']
    products = data['products']
    orders = data["orders"]

    orders_ids=find_order(data)
    if orders_ids == None:
        return None
    print("Order found\n")

    for id_to_find in orders_ids:
        for order_id, order in orders.items():
            if order_id == id_to_find:
                print(f"user={users[order['user_id']]['name']}")
                print(f"user_id={order['user_id']}")
                print(f"product={products[order['product_id']]['product_name']}")
                print(f"product_id={order['product_id']}")
                print(f"register_date={order['register_date']}\n")

def update_order():
    pass