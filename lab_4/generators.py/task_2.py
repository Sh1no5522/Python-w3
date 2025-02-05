def even (n):
    i = 1
    while i < n:
        if(i % 2 == 0):
            yield i
        i += 1

a = int(input("Enter a number: "))
b = []
for i in even(a):
    b.append(str(i))
print(",".join(b))