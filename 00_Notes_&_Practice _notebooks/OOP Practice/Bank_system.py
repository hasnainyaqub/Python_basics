class Account:
    def __init__(self, accno, name, balance):
        self.name = name
        self.balance = balance
        self.accno = accno

    def get_balance(self):
        return self.balance
    
    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} deposited successfully. \n Your remaining balance is {self.balance}")

    
    def withdraw(self, amount):
        self.balance -= amount
        print(f"{amount} withdraw successfully. \n Your remaining balance is {self.balance}")
    
    
customer_details = (int(input("Enter your account number : ")),input("Enter your name : "),int(input("Enter your balance : ")))
print('---'* 10)
acc1 = Account(*customer_details)
print(f'Account Number : {acc1.accno}\nName : {acc1.name}\nBalance : {acc1.balance}')
print('---'* 10)
# ask from user 
user = int(input('For deposit press 1 | For withdraw press 2 : '))
print('---'* 10)
if user == 1:
    amount = int(input("Enter the amount that you want to deposit: "))
    print('---'* 10)
    acc1.deposit(amount)
elif user == 2:
    amount = int(input("Enter the amount that you want to withdraw: "))
    print('---'* 10)
    acc1.withdraw(amount)
    
else:
    print("Please choose one from '1 and 2'")
print('---'* 10)    