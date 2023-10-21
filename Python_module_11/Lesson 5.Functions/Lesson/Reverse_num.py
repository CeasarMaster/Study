def reverse_num(n1):
        x=''
        for i in n1:
            x=i+x
        print('Reversed number: ',x)
        

while True:
    n=(input('Insert a number: '))
    if n=='0':
        print('The program has ended :(')
        break
    
    reverse_num(n)
