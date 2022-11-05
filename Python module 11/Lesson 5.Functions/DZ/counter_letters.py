def counter_letters(t,k,n):
    counter_let=0
    counter_num=0
    for i in t:
        if i==n:
            counter_let+=1
        if i==k:
            counter_num+=1
    print('Number of numbers: ',counter_num)
    print('Number of letters: ',counter_let)
            


t=input('Insert the text: ')
k=input('What number are we looking for? ')
n=input('What letter are we looking for: ')
counter_letters(t,k,n)
