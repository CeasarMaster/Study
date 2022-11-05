guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']


while True:
    print('На вечеринке сейчас', len(guests), 'человек')
    print(guests)
    n = input('Гость пришел или ушел?:')
    if n == 'пришел':
        x = input('Введите имя гостя:')

        if len(guests) > 5:
            print('Извини', x, ',но мест больше нет.')
            continue
        guests.append(x)

    if n == 'ушел':
        x = input('Введите имя гостя:')
        guests.remove(x)
    if n == 'пора спать':
        print('Вечеринка закончилась,все легли спать.')
        break



