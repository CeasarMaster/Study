import os


class DataAnalyst:
    def __init__(self, text: str):
        self.text = text
        self.rus_alpha = [chr(i) for i in range(ord('А'), ord('Я') + 1)]

    def is_kirillik(self, word):
        for i in word.upper():
            if i.isalpha():
                if i not in self.rus_alpha:
                    return False
        return True

    def edit_text(self):
        with open(os.path.abspath('text.txt'), encoding='UTF-8', mode='r') as file:
            file = file.read()
            words = []
            word = ''
            for i_sym in file:
                if i_sym.isalpha():
                    word += i_sym
                else:
                    if word != '':
                        words.append(word)
                        word = ''
            return words

    def lexic(self):
        lex = text.edit_text()
        count = len(lex)  # All words in list
        unique = 0
        for i in lex:
            if lex.count(i) == 1:
                unique += 1
        diff = unique / count
        return diff


text = DataAnalyst('мама мыла раму, мама мыла Рому и ковер')
print(text.is_kirillik('Прив'))
print(text.edit_text())
print(text.lexic())
