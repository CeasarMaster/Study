def max_num(n1):
    m=n1%10
    while n1>0:
        if m<n1%10:
            m=n1%10
        n1//=10
    print('The max number is: ',m)
def min_num(n1):
    m=n1%10
    while n1>0:
        if m>n1%10:
            m=n1%10
        n1//=10
    print('The min number is: ',m)
def sum_num(n1):
    suma=0
    while n1>0:
        suma+=n1%10
        n1//=10
    print('The sum of your numbers is: ',suma)

    
   

n=int(input('Insert the number: '))
action=input('What do you want to do? Find Maximum or Minimum or the sum of your numbers? ')
if action=='max':
    max_num(n)
if action=='min':
    min_num(n)
if action=='sum':
    sum_num(n)




