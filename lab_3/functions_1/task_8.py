def spy_game(*nums):
    u = False
    for i in range(len(nums)- 2):
        if (nums[i] == 0 and nums[i + 1] == 0 and nums[i + 2] == 7):
            u = True
            break
        else:
            pass
    if u != True:
        return False
    else:
        return True

user_input = list(map(int, input("Enter a all numbers: ").split()))
print(spy_game(*user_input))