import secrets
import string
import os 


def create_pass(pass_length = 8):
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation

    alphabet = letters + digits + special_chars
    password = ''
    pass_strong = False

    while not pass_strong:
        password = ''
        for i in range(pass_length):
            password += ''.join(secrets.choice(alphabet))
        if (any(char in special_chars for char in password)) and sum(char in digits for char in password) >= 2:
            pass_strong = True

    return password

print(create_pass())

#make this generate into a file.