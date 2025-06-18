cities = ["karachi" ,"isb","hyd","sukkur","lahore"]

def len_city(list):
    print(len(list))
    for items in list:
        print(items , end="-")

len_city(cities)
print()


def fac_no(n):
    f = 1
    for i in range(1,n+1):
        f *= i
    print(f)

fac_no(7)
