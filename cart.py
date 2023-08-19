cart = []

def add_to_cart(product_name, quantity):
    for product in products_list:
        if product['name'] == product_name:
            if product['quantity'] >= quantity:
                cart.append({"name": product_name, "price": product['price'], "quantity": quantity})
                product['quantity'] -= quantity
                print(f"{quantity} {product_name}(s) ont été ajoutés au panier.")
            else:
                print(f"Stock insuffisant pour {product_name}. Stock disponible : {product['quantity']}")
            return
    print(f"Le produit {product_name} n'a pas été trouvé.")

def calculate_total_price():
    total_price = sum(item['price'] * item['quantity'] for item in cart)
    print(f"Le prix total de votre panier est de : {total_price:.2f}gourdes")
