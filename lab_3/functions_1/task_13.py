import random
d = input("Hello! What is your name?: ")
a = random.randint(1, 21)
running = True
c = 0
while running:
    b = int(input("Enter a guess: "))
    if b == a:
        print(f"Good job, {d} You guessed my number in {c} guesses!")
        running = False
    elif b < a:
        print("Too low!")
        c += 1
        continue
    elif b > a:
        print("Too high!")
        c += 1
        continue