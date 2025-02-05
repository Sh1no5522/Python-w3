from datetime import datetime
a = input("Enter a first date using spaces: ").split()
b = input("Enter a second date using spaces: ").split()

r = datetime(int(a[0]), int(a[1]), int(a[2]), int(a[3]), int(a[4]), int(a[5]))
z = datetime(int(b[0]), int(b[1]), int(b[2]), int(b[3]), int(b[4]), int(b[5]))

d = r - z

print(f"The difference is {d.seconds} seconds.")