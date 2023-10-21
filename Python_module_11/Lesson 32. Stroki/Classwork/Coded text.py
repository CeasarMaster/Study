text = input('Insert the text: ')
'''for i_num,i_char in enumerate(text):
    print(i_num,i_char)'''
counter_char = 0
new_text = ''
symb = text[0]
for i_num, i_char in enumerate(text):

    if symb == i_char:
        counter_char += 1
    else:
        new_text = new_text + symb + str(counter_char)
        counter_char = 1
        symb = i_char

new_text = new_text + i_char + str(counter_char)
print(new_text)
