cards_list = []
new_cards = []
max_model = []
n = int(input('Insert the number of cards: '))
for i in range(n):
    cards = int(input('Insert the card model: '))
    cards_list.append(cards)
max_model = max(cards_list)
for i in cards_list:
    if i != max_model:
        new_cards.append(i)
print('Old list:', cards_list)
print('New list:', new_cards)
