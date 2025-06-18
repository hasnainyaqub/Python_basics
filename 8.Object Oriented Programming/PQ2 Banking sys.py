print("Welcome to the Bank of Spain")
class Account():   
    def __init__(self , bal , acc):
        self.balance = bal
        self.account_no = acc    
    # Debit

    def debitAmount(self,amount):
        self.balance -= amount
        print(f"{amount} debited successfully. \n Your remaining balance is {self.balance}")
    
    #Credit
    def crediAmount(self,amount):
        self.balance += amount
        print(f"{amount} credited successfully. \n YOur remaining balance is {self.balance}")

    #balance
    def get_balance(self):
        return self.balance
    
acc1 = Account(2120,5112579)
print("The balance in your Account =",acc1.balance)


user = input("What do you want to prefer debit or credit (use small letters) : ")

if user == "credit":
    c1 = int(input("Enter the amount that you want to credit: "))
    acc1.creditAmount(c1)
    
elif user == "debit":
    d1 = int(input("Enter the amount that you want to debit: "))
    acc1.debitAmount(d1)

else:
    print("Please choose one from 'debit and credit' (Letter should be must small)")
 


