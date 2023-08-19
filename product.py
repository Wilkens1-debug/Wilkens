products_list = []

def add_product(name, price, quantity):
    products_list.append({"name": name, "price": price, "quantity": quantity})

def show_products():
    print("\nListe des produits disponibles :")
    for product in products_list:
        print(f"Nom: {product['name']}, Prix: {product['price']}gourdes, Quantité disponible: {product['quantity']}")
