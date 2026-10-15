from products import Product


class Store:
    # constructor, initialize with products
    def __init__(self, products):
        self.products = products

    # add a product
    def add_product(self, product):
        self.products.append(product)

    # remove a product
    def remove_product(self, product):
        self.products.remove(product)

    # get sum of all product quantities
    def get_total_quantity(self) -> int:
        return sum(product.get_quantity() for product in self.products)

    # get a list of all products
    def get_all_products(self) -> list[Product]:
        return [product for product in self.products if product.is_active()]

    # order a list of products, return total price
    # check if product is present in store
    def order(self, shopping_list) -> float:
        total_price = 0.0

        for product, quantity in shopping_list:
            if product not in self.products:
                raise ValueError("Product is not available in this store.")

            total_price += product.buy(quantity)

        return total_price


def main():
    product_list = [
        Product("MacBook Air M2", price=1450, quantity=100),
        Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        Product("Google Pixel 7", price=500, quantity=250),
    ]

    best_buy = Store(product_list)

    active_products = best_buy.get_all_products()
    print(best_buy.get_total_quantity())
    print(best_buy.order([(active_products[0], 1), (active_products[1], 2)]))


if __name__ == "__main__":
    main()