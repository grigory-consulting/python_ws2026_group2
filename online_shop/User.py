
from Product import Product
from Cart import Cart


class User:

    def __init__(self,id,name):
        self.id = id
        self.name = name
        self.cart = Cart()
    
    def __repr__(self):
        return f"User({self.id}, {self.name})"
    
    def checkout_and_pay(self):



        total_price = self.cart.total_price()

        for product in self.cart.articles:
            quantity = self.cart.articles[product]
            product.buy(quantity)
        self.cart.clear()

        if total_price <= 1e-4:
            print("No articles in the cart")

        print(f"{self.name} has places an order with a total value of {total_price:.2f} €." )
        return total_price 

if __name__ == "__main__":
    laptop = Product("001", "Laptop", 999.00, 10)
    anna = User("u001", "Anna")
    anna.cart.add(laptop, 2)
    anna.cart.show()
    total_val = anna.checkout_and_pay()
    print("Total value:", total_val)
    anna.cart.show()
    print(laptop)