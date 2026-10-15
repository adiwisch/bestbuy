class Product:
    # constructor, check and set given parameters, set product active
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

    # get quantity
    def get_quantity(self) -> int:
        return self.quantity

    # set quantity
    def set_quantity(self, quantity):
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")

        self.quantity = quantity

        if self.quantity == 0:
            self.deactivate()

    # return active state
    def is_active(self) -> bool:
        return self.active

    # set active to true
    def activate(self):
        self.active = True

    # set active to false
    def deactivate(self):
        self.active = False

    # print product information
    def show(self):
        print(
            f"{self.name}, Price: {self.price:g}, "
            f"Quantity: {self.quantity}"
        )

    # reduce quantity by given amount, return total price
    # check active state and quantity values
    def buy(self, quantity) -> float:
        if not self.active:
            raise ValueError("Product is not active.")
        if quantity <= 0:
            raise ValueError("Purchase quantity must be positive.")
        if quantity > self.quantity:
            raise ValueError("Not enough products in stock.")

        total_price = self.price * quantity
        self.set_quantity(self.quantity - quantity)

        return float(total_price)


def main():
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