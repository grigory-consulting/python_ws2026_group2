from Product import Product

class Book(Product):

    def __init__(self, id, name, price, stock, tag, tax = 0.07, author="", publisher="", isbn=""):
        super().__init__(id, name, price, stock, tag, tax)
        self.isbn = isbn
        self.publisher = publisher
        self.author = author 
    
