from typing import List
from typeguard import typechecked
from .yes_oop import Item


class Phone(Item):
    # bag: List[Item] = []

    @typechecked
    def __init__(self,
                 name: str,
                 price: int,
                 quantity=1,
                 broken_phone=1,
                 ):
        super().__init__(name, price, quantity)
        assert broken_phone >= 0, f"broken_phone {broken_phone} should not be negative"

        self.broken_phone = broken_phone


def main():
    phone1 = Phone('hyper', 1000, 5)
    print("total price of phone {}: {}".format(
        phone1.name,
        phone1.calculate_total_price(),
    ))

    Item.view_the_bag()
    print()
    Phone.view_the_bag()
