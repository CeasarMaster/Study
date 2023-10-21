phone_dict = {'Petya': 854634, 'Masha': 326846, 'Vanya': 467364}
'''for i in phone_dict:
    print(i, phone_dict[i])'''
phone_dict['Sasha'] = 127432
phone_dict['Vanya'] = 7777777
phone_dict.pop('Masha')
x = phone_dict.pop('Vanya')
phone_dict['Ivan Vasilyevich'] = x
print(phone_dict)
