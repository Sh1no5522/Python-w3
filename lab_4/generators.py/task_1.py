def square (n):
    i = 1
    while i <= n:
        yield i ** 2
        i += 1

a = int(input("Enter a number: "))
for i in square(a):
    print(i)