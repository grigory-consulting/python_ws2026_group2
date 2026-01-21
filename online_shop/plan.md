# Plan - Online Shop

- class Product 
    - attributes
        - id
        - name
        - price
        - stock 
        - tag 
        - tax 
    - methods
        - __str__, __repr__
        - buy
- class Cart
    - attributes
        articles = dict(Product:quantity) of objects of class Product
    - methods 
        - add
        - remove
        - clear
        - show 
        - calculate total price
- class User 
    - attributes
        - id
        - name (all other meta-data like street, email and ....)
        - cart 
    - methods
        - pay
        - checkout 