message = {}
n = input('Insert the text: ')
for i in n:
    message[i] = n.count(i)

for i in sorted(message):
    print(i, ':', message[i])
print('Maximum frequency:', max(message.values()))
