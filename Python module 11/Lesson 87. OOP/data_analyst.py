import os

rus_alpha = [chr(i) for i in range(ord('А'), ord('Я') + 1)]
words = []


class DataAnalyst:
    def __init__(self, text: str):
        self.text = text

    def is_kirillik(self, word):
        for i in rus_alpha:
            print(i)

            if i in word:
                return True
            else:
                return False

    def edit_text(self):
        with open(os.path.abspath('text.txt'), encoding='UTF-8', mode='r') as file:
            for i in file:
                for x in i:
                    if x.isalpha():
                        words.append(x)

    def lexic(self):
        pass


text = DataAnalyst('')
print(text.is_kirillik('Прив'))
text.edit_text()
print(words)
