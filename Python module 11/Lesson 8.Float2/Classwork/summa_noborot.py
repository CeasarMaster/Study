def reverse_num(n1):
    x=''
    while n1>0:
        x+=str(n1%10)
        n1//=10
    return int(x)
x=int(input('Insert a number: '))
x2=int(input('Insert a number: '))
x3=reverse_num(x)
x4=reverse_num(x2)
suma=x3+x4
print('The sum is: ',suma)
print('The sum reversed: ',reverse_num(suma))

