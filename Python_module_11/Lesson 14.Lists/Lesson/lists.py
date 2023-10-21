'''number = []
for i in range(101):
    number.append(i)
print(number)

number=list(range(101))
print(number)'''

number_ID = []
n = int(input('Insert the amount of workers in the office: '))
for _ in range(n):
    x = int(input('Insert the workers ID: '))
    number_ID.append(x)
y=int(input('Insert the ID you are looking for: '))
if y not in number_ID:
    print('The worker is not in the office: ')
else:
    print('The worker is in the office')