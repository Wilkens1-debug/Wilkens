from product import show_products
from cart import add_to_cart, calculate_total_price

def main():
    print("Bienvenue dans notre boutique en ligne!")
    
    while True:
        print("\nMenu :")
        print("1. Chercher le produit")
        print("2. Voir le panier et le prix total")
        print("3. Fermer")
        
        choice = input("Entrez votre choix : ")
        
        if choice == "1":
            show_products()
            product_name = input("Entrez le nom du produit que vous souhaitez ajouter au panier : ")
            quantity = int(input("Entrez la quantité : "))
            add_to_cart(product_name, quantity)
        elif choice == "2":
            calculate_total_price()
        elif choice == "3":
            print("Merci d'avoir visité notre boutique en ligne!")
            break
        else:
            print("Choix invalide. Veuillez réessayer.")

if __name__ == "__main__":
    main()
