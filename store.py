"""This module defines the Store class for the BestBuy store."""

from products import Product


class Store:
    """ Store class, handles products"""
    def __init__(self, products):
        self.products = products

    def add_product(self, product):
        """Add product to store"""
        self.products.append(product)

    def remove_product(self, product):
        """Remove product from store"""
        self.products.remove(product)

    def get_total_quantity(self) -> int:
        """Return total quantity of all products in store"""
        return sum(product.quantity for product in self.products)

    def get_all_products(self) -> list[Product]:
        """Return a list of all products in store"""
        return [product for product in self.products if product.is_active()]

    def order(self, shopping_list) -> float:
        """Order shopping list with given quantity

        check if product is present in store
         return total price"""
        total_price = 0.0

        for product, quantity in shopping_list:
            if product not in self.products:
                raise ValueError("Product is not available in this store.")

            total_price += product.buy(quantity)

        return total_price

    def __contains__(self, product):
        return product in self.products

    def __add__(self, other):
        if not isinstance(other, Store):
            return NotImplemented

        return Store(self.products + other.products)


def main():
    """Main function for testing purposes"""
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
