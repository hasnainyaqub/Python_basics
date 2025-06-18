class SecInfo:
    def __init__(self,acc_no,acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass # add __ this for private your attr , obj

    def yourpass(self):
        print(info1.__acc_pass)

info1 = SecInfo(38394,"okbabe123")
print(info1.acc_no)
print(info1.yourpass())
# print(info1.__acc_pass)