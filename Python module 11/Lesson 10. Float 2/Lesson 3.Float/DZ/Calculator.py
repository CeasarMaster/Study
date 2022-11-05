n1=int(input('Insert the 1st number: '))

action=input('What do you want to do? Find Maximum or Minimum or the sum of your numbers? ')
if action=='max':
    m=n1%10
    while n1>0:
        if m<n1%10:
            m=n1%10
        n1//=10
    print('The max number is: ',m)
  
if action=='min':
    m=n1%10
    while n1>0:
        if m>n1%10:
            m=n1%10
        n1//=10
    print('The min number is: ',m)
    
 

if action=='sum':
    suma=0
    while n1>0:
        suma+=n1%10
        n1//=10
    print('The sum of your numbers is: ',suma)
    
    
  
