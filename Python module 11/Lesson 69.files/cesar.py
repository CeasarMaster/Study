import os


def cipher(string, step):
    return ''.join([alphabet[(alphabet.index(i) + step) % 26] if i in alphabet else i for i in string.lower()]).title()


alphabet = list('abcdefghijklmnopqrstuvwxyz')

move = 1
text=[]
with open(os.path.abspath('text.txt'), encoding='UTF-8', mode='r') as file:
        for i in file:
            text.append(cipher(i, move))
            move += 1

with open(os.path.abspath('cipher_text.txt'), encoding='UTF-8', mode='w') as file2:
    file2.write('\n'.join(text))
