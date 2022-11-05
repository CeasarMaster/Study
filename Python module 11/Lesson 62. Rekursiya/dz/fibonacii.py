def fibonaci(num, previous_number, fibon, counter):
    if counter >= num:
        print(previous_number)
        return 0
    else:
        next_number = previous_number + fibon
        previous_number = fibon
        fibon = next_number

        return fibonaci(num,previous_number,fibon,counter+1)


n = int(input('Insert the numbers: '))
prev_number = 1
fib = 1
x = 1
fibonaci(n, prev_number, fib, x)
'''while True:
    x += 1
    next_num = prev_number + fib
    prev_number = fib

    if x >= n:
        print(fib)
        break
    fib = next_num'''
