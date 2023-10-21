'''def summa(num):
    if num == 1:
        return 1
    return num + summa(num - 1)




summa = 0
while n > 0:
    summa += n
    n -= 1
print(summa)
print(summa(n))'''


'''def root(num):
    if num == 1:
        return 1
    print(num ** 3)
    root(num - 1)


n = int(input('Insert the number: '))
root(n)'''













def root(stop,num):
    print(stop ** 3)
    if num==stop:
        return 0

    return root(stop+1,num)




n=int(input('Insert the number: '))
x=1
root(x,n)























'''def factorial(num):
    if num == 1:
        return 1
    return num * factorial(num - 1)


n = int(input('Insert the number: '))
print(factorial(n))'''
