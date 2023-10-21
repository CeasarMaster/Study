import os


def cesar(move, line):
    cipher_text = ''
    for i in line.lower():
        index = alphabet.index(i)
        index += move
        cipher_text += alphabet[index % 26]
    return cipher_text.title()


alphabet = [chr(i) for i in range(ord('a'), ord('z') + 1)]

with open(os.path.abspath('text.txt'), encoding='UTF-8', mode='r') as file, open(os.path.abspath('cipher.txt'),encoding='UTF-8',mode='w') as file2:
    text = file.read().split('\n')
    for move, line in enumerate(text):
        file2.write(cesar(move + 1, line)+'\n')

