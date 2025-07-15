class Employee:
    def __init__(self,role , dept , salary):
        self.role = role 
        self.dept = dept
        self.salary = salary

    def showDetails(self):
        __details = f"Name : {self.name}\nAge : {self.age}\nRole : {self.role}\nDepartment : {self.dept}\nSalary : {self.salary}" 
        print(__details)
        
        
class engineer(Employee):
    def __init__(self,fullName,age):
        self.name = fullName 
        self.age = age
        super().__init__("Python Developer" , "AI" , "100K pkr")

eng1 = engineer("Hasnain", 16)
print(eng1.showDetails())