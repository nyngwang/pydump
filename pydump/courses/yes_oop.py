
# NOTE: `TypeGuard` from `typing` is just for type hinting.
from dataclasses import dataclass
from typeguard import typechecked
import textwrap # TIL: built-in


# NOTE: class is better to be created outside function.
class Item:
    # This will be neither a class/instance attribute
    # if you don't provide a default value
    is_rigid: bool = False

    @typechecked
    def __init__(self, item: str, price: int, quantity=0):
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

    item1 = Item('Phone', 1000)
    
    print(item1)

    # use `__dict__` to differentiate class/instance attributes
    print('is_rigid' in  Item.__dict__.keys())
    print('is_rigid' in  item1.__dict__.keys())
    item1.is_rigid = True
    print('is_rigid' in  Item.__dict__.keys())
    print('is_rigid' in  item1.__dict__.keys())
    print(Item.is_rigid)
    print(item1.is_rigid)




