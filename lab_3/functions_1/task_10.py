def unique():
    lists = list(map(int, input("Enter a all numbers: ").split()))
    b = []
    c = []
    for i in range(len(lists)):
        if lists[i] in b:
            c.append(lists[i])
            b.append(lists[i])
        else:
            b.append(lists[i])
    for i in range(len(lists)):
        for j in range(len(c)):
            if(c[j] == lists[i]):
                b.remove(lists[i])
    for i in b:
        print(i, end = " ")
                        

unique()