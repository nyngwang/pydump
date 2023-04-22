
# NOTE: `TypeGuard` from `typing` is just for type hinting.
from dataclasses import dataclass
from typeguard import typechecked
import textwrap # TIL: built-in


# NOTE: class is better to be created outside function.
@dataclass
class Item:
    @typechecked
    def __init__(self, item: str, price: int, quantity: int):
        assert len(item) > 0, f"item should not have an empty name"
        assert price > 0, f"price {price} should be positive"
        assert quantity >= 0, f"quantity {quantity} should not be negative"

        self.item = item
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity

    def __str__(self) -> str:

        message = """
            Hi, thanks for purchasing {}!
            quantity: {}
            total price: {}
        """

        return textwrap.dedent(message).format(
            self.item,
            self.quantity,
            self.calculate_total_price()
        )



def create_my_class():

    item1 = Item('Phone', 1000, 10)
    
    print(item1)
    print(item1.price)
    print(item1.quantity)
    print(item1.calculate_total_price())



