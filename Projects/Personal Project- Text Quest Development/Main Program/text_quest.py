import os
import tkinter
import time
from PIL import ImageTk, Image
from sys import platform

chapters = ['the_ignition', 'the_journey', 'the_plan']
macos = {'bg': 'black', 'fr': 'black'}
windows = {'bg': 'black', 'fr': 'white'}
if platform == 'darwin':
    soft_bg = macos['bg']
    soft_fr = macos['fr']
elif platform == 'win32':
    soft_bg = windows['bg']
    soft_fr = windows['fr']


def chapter_dialogue(chapter):
    data = []
    for i in chapter:
        data.append(i.split('__'))
    return data


def walking_text(data, font='Arial', size=14):
    label['text'] = f''
    label['font'] = (font, size)
    for i in data:
        time.sleep(0.01)
        label['text'] += f' {i}'
        window.update()


def walking_dialogue(data, font='Arial', size=14):
    text_history['font'] = (font, size)
    for i in data:
        time.sleep(0.01)
        text_history['text'] += f' {i}'
        window.update()


def print_data(event):
    data = 'You play as a resident of a small town surrounded by dense forests,\n\n who suddenly finds themselves in the middle of a raging wildfire.\n\n Your goal is to escape the blaze and reach safety.'
    button_start.configure(state='disabled')
    walking_text(data)
    button_start.configure(state='active')


def start_game():
    data = 'Chapter 1\n\nThe Ignition'
    button_start.destroy()
    walking_text(data, size=20)
    time.sleep(1)
    window.title('Game started')
    main_game()


def main_game():
    label.destroy()

    text_entry = tkinter.Entry(window)
    text_entry.place(relx=0.15, rely=0.8, relheight=0.07, relwidth=0.8)
    text_history.place(x=0, y=0, relheight=0.75, relwidth=1)
    send = tkinter.Button(window, text='SEND', background=soft_bg, foreground=soft_fr, font=('Arial', 14))
    send.place(relx=0.955, rely=0.8, relwidth=0.043, relheight=0.07)
    label_health = tkinter.Label(window, text='Health:', bg=soft_bg, fg=soft_fr, font=('Arial', 14))
    display_health = tkinter.Label(window, text='<==========>', bg=soft_bg, fg=soft_fr, font=('Arial', 14))
    label_hunger = tkinter.Label(window, text='Hunger:', bg=soft_bg, fg=soft_fr, font=('Arial', 14))
    display_hunger = tkinter.Label(window, text='<==========>', bg=soft_bg, fg=soft_fr, font=('Arial', 14))
    label_health.place(relx=0, rely=0.8)
    display_health.place(relx=0.05, rely=0.8)
    label_hunger.place(relx=0, rely=0.84)
    display_hunger.place(relx=0.05, rely=0.84)

    for j, i in enumerate(chapters):
        with open(os.path.abspath(f'../Other/Chapters/{i}.txt'), encoding='UTF-8', mode='r') as file:
            data = chapter_dialogue(file.readlines())
            for line in data:
                now = time.localtime()
                current_time = time.strftime("%H:%M:%S", now)
                ind = float(f'{line[0]}.0')
                walking_dialogue(f'\n{current_time} {line[1]}\n{line[1]}')

window = tkinter.Tk()
window_height = window.winfo_height()
window_width = window.winfo_width()
window.title('Escape The Blaze')
window.attributes('-fullscreen', True)
window.resizable(True, True)
window.configure(background=soft_bg)

'''img = ImageTk.PhotoImage(Image.open('/Users/nikitadereza/PycharmProjects/Study/Projects/Personal Project- Text Quest Development/Other/pictures/tree.png'))
picture = tkinter.Label(window, image=img, width=113, height=233)
picture.place(relx=0.3, rely=0.3)'''

label = tkinter.Label(window,
                      text='Press Enter To Begin',
                      background=soft_bg, foreground=soft_fr, font=('Arial', 14))
label.pack()
label.place(anchor='center', relx=0.5, rely=0.5)

button_start = tkinter.Button(window, text='START GAME', background=soft_bg, foreground=soft_fr, font=('Arial', 14),
                              command=start_game)
text_history = tkinter.Label(window, bg='white', fg='black', font=('Arial', 14))
button_start.pack()
button_start.place(anchor='center', width=150, height=80, relx=0.5, rely=0.8)
window.bind('<Return>', print_data)
window.mainloop()
