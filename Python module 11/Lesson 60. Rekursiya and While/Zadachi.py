'''def printer(num):
    if num == 0:
        return
    else:

        print('Im programmer')
        return printer(num-1)


n = int(input('Insert the number: '))
counter = 0
printer(n)

while True:
    counter+=1
    print('Im programmer')
    if counter==n:
        break'''

'''def scales(num,weight):

    if num==0:
        print(weight)
        return
    else:
        x = int(input('Insert the weight: '))
        weight+=x
        return scales(num-1,weight)









n=int(input('Insert the amount of times the bags were taken: '))
w=0
scales(n,w)
counter=0

while True:
    x=int(input('Insert the weight of the bag: '))
    counter+=1
    weight+=x
    if counter==n:
        print(weight)
        break'''

def total(num,sum_num):
    if num==0:
        return sum_num
    else:
        sum_num+=num%10
        num//=10
        return total(num,sum_num)


n = int(input('Insert the number: '))
summa = 0
print(total(n,summa))
'''while n > 0:
    total += n % 10
    n //= 10
print(total)'''


