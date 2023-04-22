from pydump.test import check_import
from pydump.courses import (
    no_oop,
    yes_oop,
    inherit
)


if __name__ == '__main__':
    check_import.all()

    # no_oop.without_oop()
    yes_oop.create_my_class()
    inherit.create_my_class()

