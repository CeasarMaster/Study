# file_manager: a program that searches objects in a given file by given keywords
import os

user_file = input('File Name: ')
user_keyword = input('Keyword: ')


def search_file():
    with open(os.path.abspath(user_file), encoding='UTF-8', mode='r') as file:
        file_content = file.readlines()
        for line_number, line in enumerate(file_content, 1):
            if user_keyword in line:
                highlighted_content = line.replace(user_keyword, f"\033[1;31m{user_keyword}\033[0m")

                print(f"Line {line_number}: {highlighted_content}")
        else:
            print('Keyword not found. Try again')


search_file()
