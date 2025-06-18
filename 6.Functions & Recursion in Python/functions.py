def Cal_sum(a,b):
    sum = a+b
    print(sum)
    return sum 
    

# Cal_sum(int(input("Enter a num :")) , int(input("Enter a no :"))) 


def per(a , b):
    divide = a/b
    multi = divide * 100
    print(f"You got {multi} percentage") 
    return(multi)


per(int(input("Enter your marks :")),int(input("Enter the total marks :")))
