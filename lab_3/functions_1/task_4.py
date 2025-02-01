import math
def filter_prime(*args):
    b = list()
    for i in range(len(args)):
        r = args[i]
        r = float(r)
        for j in range(2, int(math.sqrt(r))+ 1):
            if not r % j == 0:
                t = int(r)
                b.append(t)
    return b

user_input = list(map(int, input("Enter a all numbers: ").split()))
print(filter_prime(*user_input))