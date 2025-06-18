class S2:
    college = "Mehran College PanoAKil"
    def __init__(self, fullname , marks):
        self.name = fullname
        self.marks = marks
        print("We are adding....")

s1 = S2('Hasnain', 88)
print(f'{s1.name} {s1.marks}% from {s1.college}')
s2 = S2("Maaz",98)
print(f'{s2.name} {s2.marks}% from {s2.college}')