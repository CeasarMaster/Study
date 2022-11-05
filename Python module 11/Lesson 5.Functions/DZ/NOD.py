'''def nod(n1,n2):
    while n1 !=0 and n2 !=0:
        if n1>=n2:
            n1%=n2
        else:
            n2%=n1
    return n1 or n2

n=int(input('Insert the 1st number: '))
n2=int(input('Insert the 2nd number: '))
a=nod(n,n2)
print(a)'''

def nod(n1,n2):
    if n1>n2:
        n1,n2=n2,n1
    n=0
    for i in range(1,n1+1):
        if n1%i==0 and n2%i==0:
            n=i
    return n
n=int(input('Insert the 1st number: '))
n2=int(input('Insert the 2nd number: '))
a=nod(n,n2)
print(a)
            
