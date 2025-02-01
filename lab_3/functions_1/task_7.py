def has_33(*nums):
    u = False
    for i in range(1, len(nums) - 1):
        if nums[i] == 3 and (nums[i + 1] == 3 or nums[i - 1] == 3):
            u =  True
            break
        else:
            pass
    if u != True:
        return False
    else:
        return True

user_input = list(map(int, input("Enter a all numbers: ").split()))
print(has_33(*user_input))