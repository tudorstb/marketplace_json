from database.functions import *
from uuid import uuid4

def create_product():
    print('Creaing a product...')
    data = read_database()
    products = data["products"]

    while True:
        product_name = input('Input new product name: ')

        pass_to_date = True
        for product_id, product in products.items():
            if product['product_name'] == product_name:
                print("User already registerd")
                while True:
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
    category = input('Input new product category: ')
    while True:
        price = input("Input new product price: ")
        try:
            price = float(price)

        except :
            print("Price imputed not accepted")
            while True:
                redo=input("Try again?(Yes/No):")

                if redo.lower()=='no':
                    return None
                if redo.lower()=='yes':
                    break
                else:
                    print('Did not enter a valid option')
        else:
            if price<0:
                print('The price must be greater then 0')
                redo = input("Try again?(Yes/No):")
                while True:
                    redo = input("Try again?(Yes/No):")

                    if redo.lower() == 'no':
                        return None
                    if redo.lower() == 'yes':
                        break
                    else:
                        print('Did not enter a valid option')
            else:
                break


    product_id = str(uuid4())


    data['products'][product_id] = {
        "product_name": product_name,
        "category": category,
        "price": price
    }
    write_database(data)
    print('Done creating product!')


def find_product():
    while True:
        way_to_find=input("Choose how to search(product_name/category):")
        if way_to_find=="product_name":
            user_to_find=input("product_name=")
            return way_to_find,user_to_find
        elif way_to_find=="category":
            user_to_find = input("category=")
            return way_to_find,user_to_find
        print('Did not enter a valid option')


def delete_product():
    # product_to_find=input('')
    # data = read_database()
    # print('Deleting user...')
    # users = data["users"]
    # for person_id, person in users.items():
    #     if person[way_to_find] == user_to_find:
    #         del users[person_id]
    #         break
    # write_database(data)
    pass
def list_products():
    print('Listing products...')
    data = read_database()
    products = data["products"]
    for product_id, products in products.items():
        print(products["product_name"])
    print('________________')

def list_product():
    # alegeti o varianta..
    # v1 faceti in 2 pasi: prima data luati`va toate id`urile si pe urma alegeti un id, 
    # v2 alternativ puteti da ca input email-ul
    pass

def update_product():
    pass