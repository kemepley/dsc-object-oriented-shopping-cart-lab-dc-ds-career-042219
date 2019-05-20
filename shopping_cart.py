class ShoppingCart():
    # write your code here
    def __init__(self, total=0, employee_discount=None, items =[]):
      self.total = total
      self.employee_discount = employee_discount
      self.items = items
    
    def add_item(self, name, price, quantity=1, prices=[]):
      self.items.append(name)
      self.total += (price * quantity)
      self.prices = prices
      for i in range(quantity):
        self.prices.append(price)
    
    def mean_item_price(self):
      return self.total / len(self.prices)

    # def median_item_price(self):
    #     sorted_prices = sorted(self.prices)
    #     if len(sorted_prices)%2!=0:
    #       idx = int((len(sorted_prices)/2)-.5)
    #       return sorted_prices[idx]
    #     else:
    #       idx1 = int(len(sorted_prices)/2)
    #       idx2 = int((len(sorted_prices/2)-1)
    #       return (sorted_prices[idx1]+sorted_prices[idx2])/2

    def apply_discount(self):
      try:
        discount_total = self.total - (self.total * (self.employee_discount/100))
        return discount_total
      except:
        print("Sorry, there is no discount to apply to your cart :(")

    def void_last_item(self):
        if len(self.items) > 0:
          self.items.pop()
          self.prices.pop()
          self.total = sum(self.prices)
        else:
          print("There are no items in your cart")