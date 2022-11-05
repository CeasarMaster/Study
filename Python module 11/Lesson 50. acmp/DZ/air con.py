t_room, t_con = map(int, input().split())
word_input = input()
if word_input == 'freeze':
    if t_room <= t_con:
        print(t_room)
    else:
        print(t_con)

if word_input == 'heat':
    if t_con <= t_room:
        print(t_room)
    else:
        print(t_con)
if word_input == 'auto':
    print(t_con)
if word_input == 'fan':
    print(t_room)
