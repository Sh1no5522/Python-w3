from math import pi
def volume_of_sphere():
    a = float(input("Enter a radius: "))
    b = float(float((4/3)) * pi *(a ** 3))
    print(f"Volume is: {b:.2f}")

volume_of_sphere()