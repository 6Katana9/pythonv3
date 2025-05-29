import json 

# CRUD - Create, Read, Update, Delete

def create_product(new_product, file):
    with open(file) as f:
        products = json.load(f)
        products.append(new_product)
    with open(file, 'w') as f:
        json.dump(products, f, indent=4)
    print('Вы успешно добавили товар!')

def read_products(file):
    with open(file) as f:
        products = json.load(f) #[{}, {}, {}, {}]
        for product in products:
            print(f"Товар: {product['title']}, стоит {product['price']}$")

read_products('shop_db.json')

def read_product(id, file):
    ...

def update_product(id, file):
    ...

def delete_product(id, file):
    ...