def first_number(n,x):
    counter1=0
    temp=n
    while temp>0:
        counter1+=1
        temp//=10
    if counter1<x:
        print('The first number contains less than ',x,' numbers')
    else:
        last_digit=n%10
        first_digit=n//10**(counter1-1)
        between_digits=n%10**(counter1-1)//10
        n=last_digit*10**(counter1-1)+between_digits*10+first_digit
        return n
        
    
    
    
 









first_n=int(input('Insert the first number: '))
second_n=int(input('Insert the second number: '))
first_n=first_number(first_n,3)
second_n=first_number(second_n,4)
print('First changed number: ',first_n)
print('Second changed number: ',second_n)
print('Sum of both numbers: ',first_n+second_n)

