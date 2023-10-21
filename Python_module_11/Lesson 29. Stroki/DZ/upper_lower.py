message = input('Insert the message: ')
counter1 = 0
counter2 = 0
for i in message:
    if i.islower():
        counter1 += 1
    else:
        counter2 += 1
if counter1 > counter2:
    print(message.lower())
else:
    print(message.upper())

