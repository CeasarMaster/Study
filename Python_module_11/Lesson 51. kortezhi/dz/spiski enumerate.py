n = ['й', 'р', 'с', 'г', 'а', 'а', 'т', 'ж', 'е', 'к']
x = ['д', 'а', 'а', 'в', 'т', 'ж', 'р', 'б', 'й', 'р']
letters_num = {}
letters_num2 = {}
for i, y in enumerate(n):
    letters_num[i] = y
for i, y in enumerate(x):
    letters_num2[i] = y

print('First dictionary: ',letters_num)
print('Second dictionary: ',letters_num2)
