import tkinter

window = tkinter.Tk()
window.title('Python Calculator')
window.geometry('288x372')
window.configure(bg='light gray')
window.resizable(False, False)
num1 = 0
action = ''


def one():
    text_line.insert('end', '1')


def two():
    text_line.insert('end', '2')


def zero():
    text_line.insert('end', '0')


def three():
    text_line.insert('end', '3')


def four():
    text_line.insert('end', '4')


def five():
    text_line.insert('end', '5')


def six():
    text_line.insert('end', '6')


def seven():
    text_line.insert('end', '7')


def eight():
    text_line.insert('end', '8')


def nine():
    text_line.insert('end', '9')


def clear_entry():
    text_line.delete(0, 'end')


def delete():
    text_num = text_line.get()
    text_line.delete(len(text_num) - 1, 'end')


def plus():
    global num1, action
    num1 = text_line.get()
    action = '+'
    clear_entry()


def minus():
    global num1, action
    num1 = text_line.get()
    action = '-'
    clear_entry()


def multiply():
    global num1, action
    num1 = text_line.get()
    action = 'X'
    clear_entry()


def divide():
    global num1, action
    num1 = text_line.get()
    action = '÷'
    clear_entry()


def squared():
    global num1, action
    num1 = text_line.get()
    action = 'x²'
    clear_entry()


def one_x():
    global num1, action
    num1 = text_line.get()
    action = '1/x'
    clear_entry()


def percent():
    global num1, action
    num1 = text_line.get()
    action = '%'
    clear_entry()


def sqrt_squared():
    global num1, action
    num1 = text_line.get()
    action = '²√x'
    clear_entry()


def clear():
    global num1, action
    num1 = 0
    action = ''
    clear_entry()


def plus_minus():
    num1 = text_line.get()
    if '-' in num1:
        text_line.delete(0, 1)
    else:
        text_line.insert(0, '-')


def comma():
    num1 = text_line.get()
    if num1.count('.') == 0 and num1 != '':
        text_line.insert('end', '.')


def equals():
    global num1, action
    num1 = float(num1)
    num2 = text_line.get()
    num2 = float(num2)
    if action == '+':
        res = num1 + num2
    if action == '-':
        res = num1 - num2
    if action == 'X':
        res = num1 * num2
    if action == '÷':
        res = num1 / num2
    if action == 'x²':
        res = num1 ** num2
    if action == '1/x':
        res = num1 // num2
    if action == '%':
        res = num2 / (num1 / 100)
    if action == '²√x':
        res = num1 ** (1 / num2)

    clear_entry()
    text_line.insert('end', res)


button_percent = tkinter.Button(window, text='%', command=percent)
button_percent.place(x=0, y=120, width=70, height=40)
button_clear_entry = tkinter.Button(window, text='CE', command=clear_entry)
button_clear_entry.place(x=72, y=120, width=70, height=40)
button_clear = tkinter.Button(window, text='C', command=clear)
button_clear.place(x=144, y=120, width=70, height=40)
button_delete = tkinter.Button(window, text='⌫', command=delete)
button_delete.place(x=216, y=120, width=70, height=40)
button_one_x = tkinter.Button(window, text='1/x', command=one_x)
button_one_x.place(x=0, y=162, width=70, height=40)
button_x_squared = tkinter.Button(window, text='x²', command=squared)
button_x_squared.place(x=72, y=162, width=70, height=40)
button_sqrt_squared = tkinter.Button(window, text='²√x', command=sqrt_squared)
button_sqrt_squared.place(x=144, y=162, width=70, height=40)
button_divide = tkinter.Button(window, text='÷', command=divide)
button_divide.place(x=216, y=162, width=70, height=40)
button_7 = tkinter.Button(window, text='7', command=seven)
button_7.place(x=0, y=204, width=70, height=40)
button_8 = tkinter.Button(window, text='8', command=eight)
button_8.place(x=72, y=204, width=70, height=40)
button_9 = tkinter.Button(window, text='9', command=nine)
button_9.place(x=144, y=204, width=70, height=40)
button_times = tkinter.Button(window, text='X', command=multiply)
button_times.place(x=216, y=204, width=70, height=40)
button_4 = tkinter.Button(window, text='4', command=four)
button_4.place(x=0, y=246, width=70, height=40)
button_5 = tkinter.Button(window, text='5', command=five)
button_5.place(x=72, y=246, width=70, height=40)
button_6 = tkinter.Button(window, text='6', command=six)
button_6.place(x=144, y=246, width=70, height=40)
button_minus = tkinter.Button(window, text='-', command=minus)
button_minus.place(x=216, y=246, width=70, height=40)
button_1 = tkinter.Button(window, text='1', command=one)
button_1.place(x=0, y=288, width=70, height=40)
button_2 = tkinter.Button(window, text='2', command=two)
button_2.place(x=72, y=288, width=70, height=40)
button_3 = tkinter.Button(window, text='3', command=three)
button_3.place(x=144, y=288, width=70, height=40)
button_plus = tkinter.Button(window, text='+', command=plus)
button_plus.place(x=216, y=288, width=70, height=40)
button_plus_minus = tkinter.Button(window, text='+/-', command=plus_minus)
button_plus_minus.place(x=0, y=330, width=70, height=40)
button_0 = tkinter.Button(window, text='0', command=zero)
button_0.place(x=72, y=330, width=70, height=40)
button_comma = tkinter.Button(window, text=',', command=comma)
button_comma.place(x=144, y=330, width=70, height=40)
button_equals = tkinter.Button(window, text='=', command=equals)
button_equals.place(x=216, y=330, width=70, height=40)
text_line = tkinter.Entry(window, width=47)
text_line.place(x=0, y=20)
window.mainloop()
