def hist ():
    b = []
    lists = list(map(int, input("Enter a all numbers: ").split()))
    for i in range(len(lists)):
        b.append(["*"] * lists[i])
    for i in b:
        print(i)

hist()