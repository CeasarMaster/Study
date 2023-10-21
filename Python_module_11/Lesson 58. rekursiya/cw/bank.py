def count_years(x, p, y, c):
    if x >= y:

        return c

    else:
        x = x * (p / 100 + 1)
        c += 1
        return count_years(x, p, y, c)


counter = 0
money = int(input('Insert the money: '))
percent = int(input('Insert the percentage: '))
total_money = int(input('Insert the total money: '))
print(count_years(money, percent, total_money, counter))


















































