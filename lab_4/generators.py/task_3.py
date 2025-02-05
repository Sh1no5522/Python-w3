def div (n):
    i = 1
    while i < n:
        if(i % 3 == 0 and i % 4 == 0):
            yield i
        i += 1

a = int(input("Enter a number: "))
b = []
for i in div(a):
    b.append(str(i))
print(" ".join(b))