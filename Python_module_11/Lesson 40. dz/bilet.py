n = input()
nums = []
for i in n:
    nums.append(int(i))
if nums[0] + nums[1] + nums[2] == nums[3] + nums[4] + nums[5]:
    print('YES')
else:
    print('NO')
