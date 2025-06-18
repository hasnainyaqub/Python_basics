class Person:
    name = "anonymous"

    # def changeName(self,name):
        # self.name = name 
        # Person.name = name
        
    @classmethod
    def changeName(cls,name):
        cls.name = name

p1 = Person()
p1.changeName("Hasnain")
print(p1.name)
print(Person.name)