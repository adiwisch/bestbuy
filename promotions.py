from abc import ABC, abstractmethod


class Promotion(ABC):
    """Abstract base class for promotions"""
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def apply_promotion(self, product, quantity) -> float:
        pass


class PercentDiscount(Promotion):
    """Promotion class that applies a percent discount to products"""
    def __init__(self, name, percent):
        super().__init__(name)
        self.percent = percent

    def apply_promotion(self, product, quantity) -> float:
        """reduce price by this promotion's percentage """
        return product.price * quantity * (1 - self.percent / 100)


class SecondHalfPrice(Promotion):
    """Promotion class that applies half price discount to every second product"""
    def apply_promotion(self, product, quantity) -> float:
        """reduce price of every second product by 50%"""
        full_price_items = (quantity + 1) // 2
        half_price_items = quantity // 2

        return (
                full_price_items * product.price
                + half_price_items * product.price * 0.5
        )


class ThirdOneFree(Promotion):
    """Promotion class that makes every third product free"""
    def apply_promotion(self, product, quantity) -> float:
        """every third product is free"""
        free_items = quantity // 3
        paid_items = quantity - free_items

        return paid_items * product.price
