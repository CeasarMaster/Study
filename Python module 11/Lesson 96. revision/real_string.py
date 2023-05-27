class RealString:
    def __init__(self, Word: str):
        self.Word = Word

    def __lt__(self, word):
        return len(self.Word) < len(word.Word)


word1 = RealString('Hello')
word2 = RealString('Yes')
print(word1 < word2)
print(word1 > word2)
