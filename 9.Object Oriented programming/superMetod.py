class Car:
    def __init__(self,type):
        self.type = type 

    @staticmethod
    def start():
        print("Car started")

    @staticmethod
    def stop():
        print("Car stoped")

class MercerdesCar(Car):
    def __init__(self,name,type):
        self.name = name 
        super().__init__(type)
        super().start()

mc1 = MercerdesCar("G63 AMG" , "Desiel")
print(mc1.name)
