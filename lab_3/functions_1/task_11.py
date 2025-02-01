def palindrome ():
    a = input("Enter a word: ")
    if a == a[::-1]:
        print(True)
    else:
        print(False)

palindrome()