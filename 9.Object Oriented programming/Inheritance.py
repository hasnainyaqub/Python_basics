class car:
    
    @staticmethod
    def start():
        print("Car started")

    @staticmethod
    def stop():
        print("Car stoped")

class ToyotaCar(car):
    def __init__(self,name):
        self.name = name 
        
tcar = ToyotaCar("LC300")
print(tcar.name)
print(tcar.start())
print(tcar.stop())
