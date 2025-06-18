def show(n):
    if  n == 100:
        return
    print(n)
    show(n + 1)


show(2)
