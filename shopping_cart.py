class ShoppingCart:
    # write your code here
    def __init__(self, total=0, employee_discount=None, items=[]):
      self.total = total
      self.employee_discount = employee_discount
      self.items = items

    def add_item(self, name, price, quantity=1):
       self.total = self.total + (price*quantity)
       self.items.append({"name":name, "price":price, "quantity":quantity})
       return self.total

    def mean_item_price(self):
        subtotal = []
        for name in self.items:
            subtotal.append(name['price'] * name['quantity'])
        total_items = []
        for name in self.items:
            total_items.append(name['quantity'])
        mean_price = sum(subtotal) / sum(total_items)
        return mean_price

    def median_item_price(self):
        list_of_items = []
        for name in self.items:
            if name['quantity'] == 1:
                list_of_items.append(name['price'])
            else:
                for x in range(0, name['quantity']):
                    list_of_items.append(name['price'])
        length = len(list_of_items)
        if (length%2 == 0):
            mid_1 = int(length/2)
            mid_2 = mid_1 - 1
            median = (list_of_items[mid_1] + list_of_items[mid_2]) / 2
            return median
        mid = int(length/2)
        return list_of_items[mid]

    def apply_discount(self):
        if self.employee_discount != None:
            discount_total = self.total - (self.total * (self.employee_discount / 100))
            return discount_total
        else:
            return 'Sorry, there is no discount to apply to your cart :('

    def void_last_item(self):
        print(self.items)
        if self.items:
            removed_item = self.items.pop()
        else:
            return 'There are no items in your cart!'
        self.total -= removed_item['price']
