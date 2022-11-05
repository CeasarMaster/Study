def collect(num,debt):
    if num >= debt:
        print('thank you.')
        return 0
    else:
        print('Not enough.')
        n = int(input('How much money will you give: '))
        collect(n,x)


x = int(input('Insert the debt: '))
n = int(input('How much money will you give: '))
collect(n,x)
