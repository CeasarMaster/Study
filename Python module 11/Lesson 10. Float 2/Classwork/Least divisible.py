def divisible(a):
    for i in range(2,a+1):
        if a%i==0:
            print(i)
            break
    

n = int(input('Insert the number: '))
divisible(n)

print('hello world')