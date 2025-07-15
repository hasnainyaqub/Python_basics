class Student:
    # defualt constructor
    def __init__(self):
        pass

    # parameterized constructor
    def __init__(self, fullname, marks):
        self.name = fullname
        self.marks = marks
        
        

s1 = Student("Hasnain", 66)
print(s1.name, s1.marks)

s2 = Student('Ali Hassan', 88)
print(s2.name, s2.marks)