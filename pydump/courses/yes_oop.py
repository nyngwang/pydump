import csv

# NOTE: `TypeGuard` from `typing` is just for type hinting.
import textwrap # TIL: built-in
from typing import List
from typeguard import typechecked


# NOTE: class is better to be created outside function.
class Item:
    # without initialization, this class attribute will not exist.
    pay_rate: int = 0.8
    bag: List = []

    @classmethod
    def view_the_bag(cls):
        for item in cls.bag:
            print(item)


    @classmethod
    def from_csv(cls):
        with open('pydump/data/item.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            cls(
                name=item.get('name'),
                price=int(item.get('price')),
                quantity=int(item.get('quantity')),
            )


    @staticmethod
    def is_integer(num):
        if isinstance(num, int) \
            or isinstance(num, float) and num.is_integer():
            return True
        return False


    @typechecked
    def __init__(self, name: str, price: int, quantity=1):
        assert len(name) > 0, f"item should not have an empty name"
        assert price > 0, f"price {price} should be positive"
        assert quantity >= 0, f"quantity {quantity} should not be negative"

        self.name = name
        self.price = price
        self.quantity = quantity

        # add the bag that belongs to the class itself.
        type(self).bag.append(self)


    def calculate_total_price(self):
        return self.price * self.quantity


    def apply_discount(self):
        self.price = self.price * type(self).pay_rate


    def __repr__(self) -> str:
        message = """\
            Item("{}", {}, {})\
        """

        return textwrap.dedent(message).format(
            self.name,
            self.quantity,
            self.calculate_total_price()
        )


def _compare_before_after_attri_init(item):
    # use `__dict__` to differentiate class/instance attributes
    print()
    msg_template_found_in = """\
        pay_rate is found in class:{}, instance:{}\
    """

    print(textwrap.dedent(msg_template_found_in).format(
        'pay_rate' in  Item.__dict__.keys(),
        'pay_rate' in  item.__dict__.keys()
    ))

    print('setting item.pay_rate is set')
    item.pay_rate = 0.8

    print(textwrap.dedent(msg_template_found_in).format(
        'pay_rate' in  Item.__dict__.keys(),
        'pay_rate' in  item.__dict__.keys()
    ))
    print()


def _get_discount_from_class_attr(item):
    print("before discount:", item.calculate_total_price())
    item.apply_discount()
    print("after discount:", int(item.calculate_total_price()))
    print()


def create_my_class():
    item1 = Item('Phone', 1000)
    _compare_before_after_attri_init(item1)
    _get_discount_from_class_attr(item1)

    Item.from_csv()
    Item.view_the_bag()

    print(Item.is_integer(1000.01))




