n=int(input('Insert the number: '))
z=n
counter=0
counter2=0
while n>0:
    counter+=1
    n//=10
while z>0:
    counter2=z%10
    z//=10
    
    
print('Number of numbers: ',counter)
print('Sum of numbers: ',counter2)
print('Difference between Number of numbers and sum: ',counter2-counter)





