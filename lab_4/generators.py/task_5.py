def zero (n):
    i = 0
    while i < n:
        yield n
        n -= 1

a = int(input("Enter a number: "))
b = []
for i in zero(a):
    b.append(str(i))
print(" ".join(b))