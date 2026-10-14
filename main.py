import products
import store


def start(best_buy):
    while True:
        print("\n=================================================")
        print("Welcome to BestBuy store\n=================================================")
        print("\n1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("Please choose an option: ")

        if choice == "1":
            print("\n=================================================")
            print("Products in store\n=================================================")
            for product in best_buy.get_all_products():
                product.show()

        elif choice == "2":
            print("\n=================================================")
            print("Total amount in store\n=================================================")
            print(f"Total items in store: {best_buy.get_total_quantity()}")

        elif choice == "3":
            print("\n=================================================")
            print("Place your order\n=================================================")
            shopping_list = best_buy.get_all_products()

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
                total_price = best_buy.order(order_list)
                print(f"Order cost: {total_price} dollars.")
            except ValueError as error:
                print(f"Order failed: {error}")

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
    ]

    best_buy = store.Store(product_list)
    start(best_buy)