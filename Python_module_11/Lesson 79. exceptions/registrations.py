import os

with open(os.path.abspath('registrations.txt'), encoding='UTF-8', mode='r') as file, open(
        os.path.abspath('registrations_good.log'), encoding='UTF-8', mode='w') as good_file, open(
    os.path.abspath('registrations_bad.log'), encoding='UTF-8', mode='w') as bad_file:
    bad_log = []
    good_log=[]
    for j, i in enumerate(file):
        try:
            n = i.split()
            if len(n) != 3:
                raise IndexError(f'{j+1}) НЕ присутствуют все три поля')
            if not n[0].isalpha():
                raise NameError(f'{j+1}) Поле имени содержит НЕ только буквы')
            if '@' not in n[1] or '.' not in n[1]:
                raise SyntaxError(f'{j+1}) Поле «Имейл» НЕ содержит @ и .(точку)')
            if int(n[2]) not in range(10, 99 + 1):
                raise ValueError(f'{j+1}) Поле «Возраст» НЕ является числом от 10 до 99')

        except IndexError as bad_index:
            bad_log.append(f'{bad_index}')
        except NameError as bad_name:
            bad_log.append(f'{bad_name}')
        except SyntaxError as bad_syntax:
            bad_log.append(f'{bad_syntax}')
        except ValueError as bad_value:
            bad_log.append(f'{bad_value}')
        else:
            good_log.append(i)

    bad_file.write('\n'.join(bad_log))
    good_file.write('\n'.join(good_log))
