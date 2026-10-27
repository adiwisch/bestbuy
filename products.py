from promotions import Promotion

class Product:
    """Product class, stores name, price and quantity"""
    def __init__(self, name, price, quantity):
        if not name or not name.strip():
            raise ValueError("Product name cannot be empty.")
        if price < 0:
            raise ValueError("Price cannot be negative.")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")

        self.name = name
        self.price = float(price)
        self.quantity = quantity
        self.active = True
        self.promotion = None

    def get_quantity(self) -> int:
        """Returns quantity of product"""
        return self.quantity

    def set_quantity(self, quantity):
        """Sets quantity of product"""
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")

        self.quantity = quantity

        if self.quantity == 0:
            self.deactivate()

    def is_active(self) -> bool:
        """Returns whether product is active"""
        return self.active

    def activate(self):
        """Activate product"""
        self.active = True

    def deactivate(self):
        """Deactivate product"""
        self.active = False

    def show(self):
        """Show product information"""
        print(
            f"{self.name}, Price: {self.price:g}, "
            f"Quantity: {self.quantity}"
        )

        if self.promotion:
            print(f"Promotion: {self.promotion.name}")

    def buy(self, quantity) -> float:
        """Buy product - reduce quantity by given amount, return total price

        check active state and reasonable quantity value"""
        if not self.active:
            raise ValueError("Product is not active.")
        if quantity <= 0:
            raise ValueError("Purchase quantity must be positive.")
        if quantity > self.quantity:
            raise ValueError("Not enough products in stock.")

        if self.promotion:
            total_price = self.promotion.apply_promotion(self, quantity)
        else:
            total_price = self.price * quantity

        self.set_quantity(self.quantity - quantity)

        return float(total_price)

    def get_promotion(self):
        """Returns promotion information"""
        return self.promotion

    def set_promotion(self, promotion: Promotion):
        """Sets promotion information"""
        self.promotion = promotion

class NonStockedProduct(Product):
    """NonStockedProduct class (for something like licenses), stores name and price

     quantity is set to 0"""
    def __init__(self, name, price):
        super().__init__(name, price, quantity=0)

    def buy(self, quantity):
        """Buy product - returns total price, quantity is not reduced here"""
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")

        return self.price * quantity

    def show(self):
        """Non-stock information is shown in addition to regular product information"""
        super().show()
        print("This product is not stocked.")

class LimitedProduct(Product):
    """product with maximum order quantity"""
    def __init__(self, name, price, quantity, maximum):
        super().__init__(name, price, quantity)
        self.maximum = maximum

    def buy(self, quantity):
        """Buy product - check if desired order exceeds maximum quantity, call super.buy if not"""
        if quantity > self.maximum:
            raise ValueError(
                f"You can only buy up to {self.maximum} of this product."
            )

        return super().buy(quantity)

    def show(self):
        """Limit information is shown in addition to regular product information"""
        super().show()
        print(f"Maximum quantity per order: {self.maximum}")


def main():
    """Main function for testing purposes"""
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)

    print(bose.buy(50))
    print(mac.buy(100))
    print(mac.is_active())

    bose.show()
    mac.show()

    bose.set_quantity(1000)
    bose.show()


if __name__ == "__main__":
    main()
