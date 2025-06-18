class Complex:
    def __init__(self, real , img):
        self.real = real 
        self.img  = img

    def showNumber(self):
        print(f"{self.real},{self.img}i")

    def __add__(self,no2):
        newReal = self.real + no2.real
        newImg =self.img   + no2.img
        return Complex(newReal,newImg)

num1 = Complex(4,9)
num1.showNumber()

num2 = Complex(5,8)
num2.showNumber()

# num3 = num1.add(num2)
num3 = num1 + num2
num3.showNumber()