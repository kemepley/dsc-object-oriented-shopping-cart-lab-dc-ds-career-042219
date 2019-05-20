class ShoppingCart:
    # write your code here
    def __init__(self, total=0, emp_discount=None, items =[]):
      self.total = total
      self.employee_discount = emp_discount
      self.items = items
    
    def add_item(self, name, price, quantity=1):
      self.items.append(name)
      self.total += (price * quantity)
      self.prices = []
      for i in range(quantity):
        self.prices.append(price)
    
    def mean_item_price(self):
       return self.total/len(self.prices)

    def median_item_price(self):
        pass

    def apply_discount(self):
       pass

    def void_last_item(self):
        pass