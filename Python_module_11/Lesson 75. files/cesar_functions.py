def decoder(move: int, line: str, language: str) -> str:
    cipher_text = ''
    alpha = alphabet if language == 'eng' else alphabet_rus

    for i in line.lower():
        if i.isalpha():
            index = alpha.index(i)
            index -= move
            cipher_text += alpha[index % len(alpha)]
        else:
            cipher_text += i

    return cipher_text.title()


def coder(move: int, line: str, language: str) -> str:
    cipher_text = ''
    alpha = alphabet if language == 'eng' else alphabet_rus
    for i in line.lower():
        if i.isalpha():
            index = alpha.index(i)
            index += move
            cipher_text += alpha[index % len(alpha)]
        else:
            cipher_text += i

    return cipher_text.title()


alphabet = [chr(i) for i in range(ord('a'), ord('z') + 1)]
alphabet_rus = [chr(i) for i in range(ord('а'), ord('я') + 1)]
