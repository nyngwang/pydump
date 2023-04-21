
# Yup, we need to creat it outside

class Item:

    def calculate_total_price(self):
        return self.price * self.quantity




def create_my_class():

    item1 = Item()
    item1.type = 'Phone'
    item1.price = 1000
    item1.quantity = 10
    
    print(item1)
    print(item1.type)
    print(item1.price)
    print(item1.quantity)
    print(item1.calculate_total_price())



