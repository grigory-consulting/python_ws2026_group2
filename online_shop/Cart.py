from Product import Product

class Cart:

    def __init__(self):
        self.articles = {}

    def __repr__(self):
        return f"Cart({self.articles})"
    
     