# # i = 1

# while i  <= 10  : 
#     print(f"{3*i}, OK")
#     i += 1

# # no = 100
# while no >= 1 :
#     print(no)
#     no -= 1

# # t3 = 3
# while t3 <= 30 :
#     print(t3)
#     t3 += 3 

# l1 = [1,4,9,16,25,36,49,64,81,100]

# idx = 0

# while idx < len(l1):
#     print(l1[idx])
#     idx += 1

l2 = (1,4,9,16,25,36,49,64,81,100)
x = int(input("Enter the no :"))
print(x)
idx = 0

while idx < len(l2):
    if l2[idx] == x :
        print("found","index no =" ,idx)
        break
    else:
        print("no")

    
    idx += 1


