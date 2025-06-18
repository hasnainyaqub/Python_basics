
print("Apply for ID Card ")
age = int(input("Enter your age :"))

if(age >= 18):
    print("Yes you are eligible for id card.")
    name= input("Enter your name :")
    print(f"{name} your card will deliver you after 7 working days \n Thank You")
elif(age>=15):
    name= input("Enter your name :")
    print(f"{name} you are not eligible for id card.")
else:
    name = input("Enter your name :")
    print(f"{name} get lost ")


    
     
