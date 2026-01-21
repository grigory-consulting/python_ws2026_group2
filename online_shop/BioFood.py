from Food import Food
from BioLabel import BioLabel

class BioFood(Food, BioLabel):
    def __init__(self, id, name, price, stock, tag, date_expiry, label):
        Food.__init__(id, name, price, stock, tag, date_expiry)
        BioLabel.__init__(label)

print(BioFood.mro())