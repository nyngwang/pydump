
# Yup, we need to creat it outside

class Item:
    pass


def create_my_class():

    item1 = Item()
    item1.type = 'Phone'
    item1.price = 1000
    item1.quantity = 10
    item1.total_price = item1.price * item1.quantity
    
    print(item1)
    print(item1.type)
    print(item1.price)
    print(item1.quantity)
    print(item1.total_price)



