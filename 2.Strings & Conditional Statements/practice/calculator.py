no1 = int(input("Enter the number : "))
no2 = int(input("Enter the number : "))
sym = int(input("1.addition , 2.subtraction ,3.multiplication, 4.division : "))

if sym == 1 :
     ans = no1+no2

elif sym == 2 :
    ans = no1-no2

elif sym == 3 :
    ans = no1*no2
    
elif sym == 4 :
    ans = no1/no2

print(ans) 