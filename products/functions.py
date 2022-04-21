from database.functions import *
from uuid import uuid4

def find_product_by_name(products):
    while True:

        product_name=input("product_name=")
        pass_to_date = True
        skip_try_again = False
        for product_id, product in products.items():
            if product["product_name"] == product_name:
                print("Product found")

                skip_try_again = True
                return product_name

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

def create_price():
    while True:
        price = input("Input product price: ")
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
    return price

def create_product():
    print('Creaing a product...')
    data = read_database()
    products = data["products"]

    while True:
        product_name = input('Input new product name: ')
        category = input('Input new product category: ')

        pass_to_date = True
        for product_id, product in products.items():
            if product['product_name'] == product_name :
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

    price=create_price()
    if price == None:
        return None


    product_id = str(uuid4())


    data['products'][product_id] = {
        "product_name": product_name,
        "category": category,
        "price": price
    }
    write_database(data)
    print('Done creating product!')

def user_in_file(way_to_find, product_to_find):
    data = read_database()
    users = data["products"]
    found = False
    for product_id, product in users.items():
        if product[way_to_find] == product_to_find:
            del users[product_id]
            found = True
            break

    return found

def find_product():
    while True:
        way_to_find = input("Choose how to search(product_name/category):")
        if way_to_find == "product_name":
            product_to_find = input("product_name=")
            if user_in_file(way_to_find, product_to_find) == True:
                return way_to_find, product_to_find
            else:
                while True:
                    retry = input("product not found ,wish to try again?(Yes/No):")
                    if retry.lower() == 'no':
                        return None, None
                    elif retry.lower() == 'yes':
                        find_product()
                    else:
                        print('Did not entered a valid option')
        elif way_to_find == "category":
            product_to_find=input("category=")

            if user_in_file(way_to_find, product_to_find) == True:
                return way_to_find, product_to_find
            else:
                while True:
                    retry = input("product not found ,wish to try again?(Yes/No):")
                    if retry.lower() == 'no':
                        return None, None
                    elif retry.lower() == 'yes':
                        find_product()
                    else:
                        print('Did not entered a valid option')
        print('Did not enter a valid option')

def delete_product():
    data = read_database()

    products = data["products"]

    product_name=find_product_by_name(products)
    if product_name == None:
        return None

    print('Deleting product...')

    found = False
    for product_id, product in products.items():
        if product['product_name'] == product_name:
            del products[product_id]
            found = True
            break
    if found == False:
        print("")

    write_database(data)

def list_products():
    print('Listing products...')
    data = read_database()
    products = data["products"]
    for product_id, products in products.items():
        print(products["product_name"])
    print('________________')

def list_product():
    data = read_database()

    products = data["products"]

    while True:

        product_name = input("product_name=")
        pass_to_date = True
        skip_try_again = False
        for product_id, product in products.items():
            if product["product_name"] == product_name:
                print("Product found")
                skip_try_again = True
                break

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


    print('Listing product...')

    for product_id, product in products.items():
        if product['product_name'] == product_name:
            print(f'\nid={product_id}')
            print(f'product_name={product["product_name"]}')
            print(f'category={product["category"]}')
            # pot sa pun break??

    pass

def update_product():
    option_list = ['product_name','category','price', 'exit']
    data = read_database()
    products = data['products']

    product_original_name = find_product_by_name(products)
    if product_original_name == None:
        return None

    updated_name = ''
    updated_category = ''
    updated_price=''
    def update_option(updated_name, updated_category,updated_price):
        while True:
            update_entry = input('Choose what you whis to update:')
            if update_entry.lower() == 'product_name':
                updated_name = input("New name=")
                return updated_name, updated_category ,updated_price
            elif update_entry.lower() == 'category':
                updated_category = input('New category=')
                return updated_name, updated_category ,updated_price
            elif update_entry.lower() == 'price':
                updated_price =create_price()
                if updated_price == None:
                    return None
                return updated_name, updated_category ,updated_price
            elif update_entry.lower() == 'exit':
                return updated_name, updated_category ,updated_price
            elif update_entry.lower() == 'help':
                print(f'options-> {option_list}')
            else:
                print(f'Did not enterd a valid option-> {option_list}')

    updated_name, updated_category ,updated_price= update_option(updated_name, updated_category,updated_price)
    while True:
        update_more = input('Update something else(yes/no):').lower()
        if update_more == 'yes':
            updated_name, updated_category, updated_price = update_option(updated_name, updated_category, updated_price)
        elif update_more == 'no':
            break
        else:
            print('Did not entered a valid option')

    print('Updating a user...')

    for product_id, product in products.items():
        if product['product_name'] == product_original_name:
            if updated_name != '':
                product["product_name"] = updated_name
            elif updated_category != '':
                product["category"] = updated_category
            elif updated_price != '':
                product["price"] = updated_price
    write_database(data)
    print('Done updating the product!')