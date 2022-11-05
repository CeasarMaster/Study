n = int(input('Insert the amount of people in the game:'))
count = int(input('Insert the number you want to count to:'))
people = list(range(1, n + 1))
counter = 0

while len(people) > 1:
    print('Current people in the game:', people)
    counter = (counter + count - 1) % len(people)
    print('Starting from:', counter)
    if people[counter] == people[-1]:
        print('Person that is taken out is:', people.pop(counter))
        counter = 0
    else:
        print('Person that is taken out is:', people.pop(counter))

print('Person that is left is:', people[0])
