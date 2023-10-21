def multiple(num, count):
    if count == num:
        return 'YES'
    elif count > num:
        return 'NO'
    else:
        count *= 2
        return multiple(num, count)


n = int(input('Insert the number: '))
x = 1

print(multiple(n, x))
'''while x != n:
    x *= 2
if x < n:
    print('NO')

else:
    print('YES')'''
