# n = [1, 2, 3, 4, 5]
# z = iter(n)
# print(next(z))
# print(next(z))
# print(next(z))
# print(next(z))
# print(next(z))
#


class Fibonacii:
    '''iterator class in fibonacci sequence'''

    def __init__(self, number: int):
        self.number = number
        self.counter = 0
        self.current_num = 0
        self.next_num = 1

    def __iter__(self):  # Intial values
        self.counter = 0
        self.current_num = 0
        self.next_num = 1
        return self

    def __next__(self):  # Logic of how the cycle works
        self.counter += 1
        if self.counter > self.number:  # Stop the cycle
            raise StopIteration
        self.current_num, self.next_num = self.next_num, self.current_num + self.next_num
        return self.current_num


x = Fibonacii(6)
for i in x:
    print(i)
for i in x:
    print(i)
