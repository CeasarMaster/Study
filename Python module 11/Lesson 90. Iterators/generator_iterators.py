class Primes:

    def __init__(self, number: int):
        self.number = number
        self.count_regular = 0
        self.regular_num = 1

    def __iter__(self):
        self.count_regular = 0
        self.regular_num = 1
        return self

    def __next__(self):
        while True:
            self.count_regular = 0
            self.regular_num += 1
            if self.regular_num > self.number:
                raise StopIteration
            for i in range(1, self.regular_num + 1):
                if self.regular_num % i == 0:
                    self.count_regular += 1
            if self.count_regular == 2:
                return self.regular_num


prime_nums = Primes(50)

for i in prime_nums:
    print(i, end=' ')


def prime(num):
    counter = 0
    for i in range(1, num + 1):
        if num % i == 0:
            counter += 1

    if counter == 2:
        return True
    else:
        return False
