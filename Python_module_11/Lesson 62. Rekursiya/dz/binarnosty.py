def binary(num, count):
    if count > num or num == 1:

        return False

    elif count == num:
        return True
    else:
        count *= 2
        return binary(num, count)


n = int(input('Insert the number: '))
x = 1
print(binary(n, x))
'''while x != n:
    x *= 2
if x > n:
    print('False')
else:
    print('True')'''
