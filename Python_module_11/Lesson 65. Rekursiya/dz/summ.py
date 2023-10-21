def summ(*args, count):
    print(args)
    for i in args:
        #print(i)

        if isinstance(i, list):
            summ(i, count=count)
            count += i

    print(count)


counter = 0
summ(1, 5, [78, [1, 2]], [7, 8], count=counter)
