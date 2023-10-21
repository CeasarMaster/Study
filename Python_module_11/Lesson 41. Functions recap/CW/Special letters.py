n = input()


def letter(a):
    counter = 0
    counter2 = 0
    for i in a:
        if i == 's':
            counter += 1
        else:
            if counter > counter2:
                counter2 = counter
            counter = 0
    return counter2


print(letter(n))
