from Product import Product

class Cart:

    def __init__(self):
        # {Product:quantity }
        self.articles = {}

    def __repr__(self):
        return f"Cart({self.articles})"

    def add(self, product, quantity = 1):
        if quantity <= product.stock: 
            self.articles[product] = self.articles.get(product,0) + quantity
        # TODO What about sub?  
        # 
    
    def remove(self, product):
        del self.articles[product]
    
    def clear(self): 
        self.articles.clear()

    def total_price(self):
        total = 0
        for product in self.articles:
            total += self.articles[product] * product.price 
        
        return total 
    
    def show(self):
        
        print("Following product are currently in the shopping cart:")

        for product in self.articles:
            quantity = self.articles[product] 
            price_line = product.price*quantity
            print(f"    {product.name} x {quantity} = {price_line:.2f} €")
        
        print(f"Total price:    {self.total_price():.2f} €")

if __name__ == "__main__":
    product1 = Product("001", "MyBook", 20.99, 5 )
    product2 = Product("002", "MyDVD", 19.99, 10 )
    sc = Cart()
    sc.add(product1)
    sc.add(product2, 8)
    print(sc.total_price())
    sc.show()