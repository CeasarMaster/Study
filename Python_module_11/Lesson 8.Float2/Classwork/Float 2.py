def argument(a,b):
    if a>b:
        return a
    else:
        return b
    
    
n1=int(input('Insert a number: '))
n2=int(input('Insert a number: '))
n3=int(input('Insert a number: '))
x=argument(n1,n2)
print(argument(x,n3))
