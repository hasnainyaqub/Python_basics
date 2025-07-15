class Order:
    def __init__(self,item , price):
        self.item = item
        self.price =price

    def details(self):
        print(f"Mobile : {self.item}\nPrice : {self.price}")

    def __gt__(self,gt):
        return self.price > gt.price

odr1 = Order("Redmi 13",40000)
odr2 = Order("Redmi Note 13", 55000)
odr1.details()
odr2.details()

print(f"Redmi Note 13 is expensive the Redmi 13 : {odr1 < odr2}")
