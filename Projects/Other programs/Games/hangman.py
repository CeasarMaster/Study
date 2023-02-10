import random

tries = 10
words = ['cars', 'mouse', 'mug', 'monitor', 'alphabet']
chosen_word = random.choice(words)
length = len(chosen_word)
display = '_' * length
guessed = []

while tries > 0:
    guess = input(f'This is the word: {display} Enter your letter: ')
    if guess in chosen_word:
        guessed.extend(guess)
        index = chosen_word.find(guess)
        chosen_word = chosen_word[:index] + "_" + chosen_word[index + 1:]
        display = display[:index] + guess + display[index + 1:]
        print(display + "\n")

    elif guess in guessed:
        print('Try another letter.\n')

    else:
        tries -= 1
        print(f'Tries left: {tries}')

    if len(''.join(guessed)) == length:
        print('You have guessed the word!')
        break
