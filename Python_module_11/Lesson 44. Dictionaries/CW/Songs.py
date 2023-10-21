violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}
counter = 0
n = int(input('How many songs?: '))
for i in range(n):
    x = input('Insert the songs name: ')
    for j in violator_songs:
        if j == x:
            counter += violator_songs[j]
print('Total playtime of songs:',counter)
