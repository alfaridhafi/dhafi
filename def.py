class MenuItem:
    def __init__ (self, price, name):
        self.name = name

        self.price = price

    def info(self):
        return self.name + ":$" + self.price
    
    def get_total_price(self, count):
        total_price = count * self.price
        return get_total_price
