# file_manager: a program that searches objects in a given file by given keywords
import os

user_file = input('File Name: ')
user_keyword = input('Keyword: ')


def search_file():
    with open(os.path.abspath(user_file), encoding='UTF-8', mode='r') as file:
        file_content = list(file.readlines())
        for i in file_content:
            if user_keyword == i:
                print(f'{user_keyword} is in file...')


search_file()
