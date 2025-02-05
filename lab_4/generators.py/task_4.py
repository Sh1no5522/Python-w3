def squares (a , n):
    while a < n:
        yield a ** 2
        a += 1

a = int(input("Enter first number: "))
n = int(input("Enter second number: "))
b = []
for i in squares(a , n):
    b.append(str(i))
print(" ".join(b))