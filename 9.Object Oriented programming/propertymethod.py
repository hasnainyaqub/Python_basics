class students:
    def __init__(self,chm,phy,maths):
        self.phy = phy
        self.chm = chm
        self.maths = maths


    @property
    def percentage(self):
        return (self.phy + self.chm + self.maths)/ 3 


chmmark = int(input("Enter your chemistry marks:"))
phymark = int(input("Enter your physics marks:"))
mathsmark = int(input("Enter your Maths marks:"))

st1 = students(chmmark,phymark,mathsmark)
print(st1.chm, st1.phy,st1.maths, "=" ,st1.percentage,"%")

# st1.chm = 44
# print(st1.chm, st1.phy,st1.maths ,st1.percentage)2