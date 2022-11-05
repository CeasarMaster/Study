n = list(input('Insert the text: '))
for i in range(len(n)):
    if n[i - 1] == ' ':
        n[i] = n[i].upper()

print(''.join(n))
