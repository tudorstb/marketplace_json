from database.functions import *
from uuid import uuid4
def create_product():
    print('Creaing a product...')
    data = read_database()


    product_id = str(uuid4())
    product_name = input('Input new product name: ')
    category = input('Input the category of the new product: ')
    price = input('Input the price of the new product: ')


    data['products'][product_id] = {
        "product_name": product_name,
        "category": category,
        "price": price
    }
    write_database(data)
    print('Done creating product!')

def delete_product():
    pass

def list_products():
    pass

def list_product():
    # alegeti o varianta..
    # v1 faceti in 2 pasi: prima data luati`va toate id`urile si pe urma alegeti un id, 
    # v2 alternativ puteti da ca input email-ul
    pass

def update_product():
    pass