def count(num, c):
    c += 1
    if len(str(num)) == c:
        print(c)
    else:

        int(num) // 10
        count(num, c)


counter = 0
n = int(input('Insert the number:'))
count(n, counter)
'''while n > 0:
    counter += 1
    n = n // 10
print(counter)'''
