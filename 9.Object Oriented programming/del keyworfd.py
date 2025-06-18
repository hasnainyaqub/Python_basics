class Delkey:
    def __init__(self,name):
        self.name = name

del1 = Delkey("Hasnain")
print(del1.name)
del del1.name
print(del1.name)