'''def function():
    return 1, 2, 3, 4


print(function())'''

'''x = tuple(range(1, 11+1))
print(x)'''

import random


def change(nums):
    index = random.randint(0, 4)

    value = random.randint(100, 1000)

    value = nums[index]

    return nums, value


my_nums = 1, 2, 3, 4, 5

new_nums, rand_val = change(my_nums)

print(new_nums, rand_val)

new_nums = change(new_nums)[0]

rand_val += change(new_nums)[1]

print(new_nums, rand_val)
