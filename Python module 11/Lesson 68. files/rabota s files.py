import os

'''file=open('name.txt',encoding='UTF-8')
for i in file:
    print(i)
print([file.read()])

print(os.path.abspath('name.txt'))

file = open(os.path.abspath('hello.txt'),encoding='UTF-8',mode='a')
file.write('Hello,World 1')
file.close()
print(file.closed)'''
with open(os.path.abspath('hello.txt'),encoding='UTF-8',mode='w') as file:
    x=file
    print(x)
print(file.closed)