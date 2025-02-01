from itertools import permutations

def print_permutations():
    user_input = input("Enter a string: ")
    all_permutations = permutations(user_input, len(user_input))
    
    print("All permutations:")
    print("***************************************")
    for perm in all_permutations:
        print(''.join(perm))
    print("***************************************")


print_permutations()