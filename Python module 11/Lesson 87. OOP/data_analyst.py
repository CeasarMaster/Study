import os

rus_alpha = [chr(i) for i in range(ord('А'), ord('Я') + 1)]


class DataAnalyst:
    def __init__(self, text: str):
        self.text = text

    def is_kirillik(self, word):
        for i in word:
            if i in rus_alpha:
                return True
            else:
                return False

    def edit_text(self):
        pass

    def lexic(self):
        pass


text = DataAnalyst('')
