import products
import store

def print_header(headline):
    """print header"""
    print("\n=================================================")
    print(headline)
    print("=================================================\n")

def list_products(store_instance):
    """list all products in store"""
    print_header("Products in store")
    for product in store_instance.get_all_products():
        product.show()

def show_amount(store_instance):
    """show total amount in store"""
    print_header("Total amount in store")
    print(f"Total items in store: {store_instance.get_total_quantity()}")

def place_order(store_instance):
    """place order"""
    print_header("Place your order")
    shopping_list = store_instance.get_all_products()

    for index, product in enumerate(shopping_list, start=1):
        print(f"{index}. ", end="")
        product.show()

    print("Enter the product number and quantity.")
    print("Enter an empty product number to finish.")

    order_list = []

    while True:
        product_number = input("Product number: ")

        if not product_number:
            break

        try:
            product_number = int(product_number)

            if product_number < 1 or product_number > len(shopping_list):
                print("Invalid product number.")
                continue

            quantity = int(input("Quantity: "))

            order_list.append(
                (shopping_list[product_number - 1], quantity)
            )

        except ValueError:
            print("Please enter valid numbers.")

    try:
        total_price = store_instance.order(order_list)
        print(f"Order cost: {total_price} dollars.")
    except ValueError as error:
        print(f"Order failed: {error}")

def start(store_instance):
    """start application, show menu"""
    while True:
        # show menu
        print_header("Welcome to BestBuy store")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("Please choose an option: ")

        # choice 1 -> show information of all products
        if choice == "1":
            list_products(store_instance)

        # choice 2 -> show total amount of all products
        elif choice == "2":
            show_amount(store_instance)

        # choice 3 -> place order
        elif choice == "3":
            place_order(store_instance)

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please choose 1, 2, 3 or 4.")


if __name__ == "__main__":
    # Setup initial stock of inventory

    product_list = [
        products.Product("MacBook Air M2", price=1450, quantity=100),
        products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        products.Product("Google Pixel 7", price=500, quantity=250),
        products.NonStockedProduct("Windows License", price=125),
        products.LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
    ]

    best_buy = store.Store(product_list)
    start(best_buy)
