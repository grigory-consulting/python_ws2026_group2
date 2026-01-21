

class Product:
    def __init__(self, id, name = "", price = 1.0 , stock = 0, tag = "", tax=0.19):
        self.id = id
        self.name = name
        self.price = price
        self.stock = stock
        self.tag = tag
        self.tax = tax
    
    def __str__(self):
        return f"{self.name} | {self.price:.2f} € | Quantity available: {self.stock}"
    
    def __repr__(self):
        return f"Product({self.id}, {self.name}, {self.price}, {self.stock}, {self.tag}, {self.tax})"
    
    def buy(self, quantity):
        if quantity>0:
            if self.stock >= quantity:
                self.stock -= quantity
            else:
                print("Not enough in the stock") # TODO later we will built in an error



if __name__ == "__main__":
    p1 = Product("001", "ProductName", 20.99,5)
    print(p1)