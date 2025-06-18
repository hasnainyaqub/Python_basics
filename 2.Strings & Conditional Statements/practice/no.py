a =  int(input("Enter first number :"))
b =  int(input("Enter second number :"))
c =  int(input("Enter third number :"))
d =  int(input("Enter fourth number :"))

if a>= b and a>= c and a>=d :
    print(f"{a} is greater")
elif b>= c and b>= d  :
    print(f"{b} is greater")
elif  c>= d  :
    print(f"{c} is greater")
else :
    print(f"{d} is greater")
