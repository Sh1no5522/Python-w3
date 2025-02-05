import math
a = float(input("Enter the number of sides: "))
b = float(input("Enter the length of a side: "))
d = b / (2 * math.tan(math.radians(180 / a)))
c = (a * b * d) / 2
print(f"Area of the regular polygon is {c:.2f}")