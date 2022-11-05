'''n=[]

with open('games.txt') as file:
    for i in file:
        print(i)
        n.append(i)
with open('games.txt','r') as file:
    print(file.read())

print(n)'''
with open('games.txt') as file:
    x = file.read()

with open('empty.txt', 'w') as file:
    file.write(x)
n = input()
with open('empty.txt', 'a') as file:
    file.write(f'\n{n}')
