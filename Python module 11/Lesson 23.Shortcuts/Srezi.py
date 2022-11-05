'''nums = [48, -10, 9, 38, 17, 50, -5, 43, 46, 12]
print(nums[:5])
print(nums[:8])
print(nums[::2])
print(nums[1::2])
print(nums[::-1])
print(nums[::-2]'''

'''import random as r

nums = [r.randint(1, 10) for _ in range(10)]
a = int(input('Insert the number:'))
b = int(input('Insert the number:'))
if a > b:
    a, b = b, a
print(nums)
print(nums[:a-1], nums[b:])'''

'''n = 'abcdefg'
print(n)
print(n[::-1])
print(n[::2])
print(n[1::2])
print(n[:1])
print(n[6:5:-1])
print(n[3:4])
print(n[4:])
print(n[3:5])
print(n[4:2:-1])'''

n = ['1', '2', '3', '4', '5']
y = n
y.append('3')
print(n)
print(y)
x=True
y=x
y+=False
print(x)
print(y)
