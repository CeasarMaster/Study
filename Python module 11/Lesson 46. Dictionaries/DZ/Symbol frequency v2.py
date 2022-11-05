message = {}
inverted_dict = {}
n = input('Insert the message: ')
for i in n:
    message[i] = n.count(i)
for i in sorted(message):
    print(i, ':', message[i])

for i in message:
    if message[i] not in inverted_dict:
        inverted_dict[message[i]] = [i]
    else:
        inverted_dict[message[i]].append(i)
for i in inverted_dict:
    print(i, ':', inverted_dict[i])
