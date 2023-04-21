# Yup, we need to creat it outside
# adv1: aggregate many things into one
import textwrap
from dataclasses import dataclass
from typing import (
    Any,
)


@dataclass
class Item:
    item: str
    price: int
    quantity: int

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

    item1 = Item('Phone', 1000, 4)
    
    print(item1)
    print(item1.price)
    print(item1.quantity)
    print(item1.calculate_total_price())



