class Item:
    pay_rate = 0.8 # The pay rate after 20% discount
    def __init__(self,name: str,price: float,quantity=0):
        # Run validations to the received arguments
        assert price  >= 0, f"Price {price} is not greater than zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than zero!"
        
        # Assign to self object
        self.name = name 
        self.price = price 
        self.quantity = quantity 
    
    def calculate_total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate

# item3 = Item('1',100,1)
# item1 = Item('Phone',100,5)
# print(item1.calculate_total_price())
# item2 = Item("Laptop",1000,3)
# item2.pay_rate = 0.7
# item2.has_numpad = False
# item2.apply_discount()
# print(item2.calculate_total_price())
# print(Item.pay_rate)
# print(item1.__dict__)
# print(Item.__dict__)

item1 = Item('Phone',100,1)
item2 = Item('Laptop',1000,3)
item3 = Item('Cable',10,5)
item4 = Item('Mouse',50,5)
item5 = Item('Keyboard',75,5)