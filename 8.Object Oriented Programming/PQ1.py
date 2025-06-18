class StudentInfo:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val 
            
            print(sum/3)
    
s1 = StudentInfo("Hasnain",[99,88,98])
# print(f"{s1.name} {s1.marks}")
s1.get_avg()