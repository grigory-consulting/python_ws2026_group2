from Product import Product
# TODO from datetime import date


class Food(Product):

    def __init__(self, id, name, price, stock, tag, date_expiry):
        super().__init__(id, name, price, stock, tag, tax=0.07)
        self.date_expiry = date_expiry 
