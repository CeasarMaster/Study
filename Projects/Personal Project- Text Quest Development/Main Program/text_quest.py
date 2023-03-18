import os
import tkinter
import time
from PIL import ImageTk, Image
from sys import platform
from tkinter.messagebox import showwarning
from main_game import *

chapters = ['the_ignition', 'the_plan', 'the_journey', 'the_rescue', 'the_aftermath']
macos = {'bg': 'black', 'fr': 'black'}
windows = {'bg': 'black', 'fr': 'white'}
if platform == 'darwin':
    soft_bg = macos['bg']
    soft_fr = macos['fr']
elif platform == 'win32':
    soft_bg = windows['bg']
    soft_fr = windows['fr']

answers = ['']
number = 0
chapter_for_show = ['Chapter 2\n\nThe Plan\n', 'Chapter 3\n\nThe Journey\n', 'Chapter 4\n\nThe Rescue\n',
                    'Chapter 5\n\nThe Aftermath\n']


def main_game():
    global number

    def hulk():
        text_entry.destroy()
        send.destroy()
        label_health.destroy()
        display_health.destroy()
        label_hunger.destroy()
        display_hunger.destroy()

    def button():

        global number
        ans = text_entry.get()
        if ans == answers[0]:
            number += 1
            text_entry.delete(0, 'end')
            storyline()
        else:
            showwarning('You died', "YOU DIED")
            window.destroy()

    text_entry = tkinter.Entry(window)
    text_entry.place(relx=0.15, rely=0.8, relheight=0.07, relwidth=0.8)
    text_history.place(x=0, y=0, relheight=0.75, relwidth=1)
    send = tkinter.Button(window, text='SEND', background=soft_bg, foreground=soft_fr, font=('Arial', 14),
                          command=button)
    send.place(relx=0.955, rely=0.8, relwidth=0.043, relheight=0.07)
    label_health = tkinter.Label(window, text='Health:', bg=soft_bg, fg=soft_fr, font=('Arial', 14))
    display_health = tkinter.Label(window, text='<==========>', bg=soft_bg, fg=soft_fr, font=('Arial', 14))
    label_hunger = tkinter.Label(window, text='Hunger:', bg=soft_bg, fg=soft_fr, font=('Arial', 14))
    display_hunger = tkinter.Label(window, text='<==========>', bg=soft_bg, fg=soft_fr, font=('Arial', 14))
    label_health.place(relx=0, rely=0.8)
    display_health.place(relx=0.05, rely=0.8)
    label_hunger.place(relx=0, rely=0.84)
    display_hunger.place(relx=0.05, rely=0.84)
    dia = logic(chapters.pop(0))

    def storyline():
        if number == 0:
            answers[0] = dia[0][-1]
            walking_dialogue(text_history, window, dia[0][0])
        elif number == len(dia):
            hulk()
            show_chapters()
        elif number == 1:
            walking_dialogue(text_history, window, dia[1][0])
            answers[0] = dia[1][-1]
        elif number == 2:
            walking_dialogue(text_history, window, dia[2][0])
            answers[0] = dia[2][-1]
        elif number == 3:
            walking_dialogue(text_history, window, dia[3][0])

            if len(chapters) == 0:
                time.sleep(1)
                window.destroy()
                showwarning('Win', 'You ended game')
            answers[0] = dia[3][-1]
        elif number == 4:
            walking_dialogue(text_history, window, dia[4][0])
            answers[0] = dia[4][-1]
        elif number == 5:
            walking_dialogue(text_history, window, dia[5][0], clean=True)
            answers[0] = dia[5][-1]
        elif number == 6:
            walking_dialogue(text_history, window, dia[6][0])
            answers[0] = dia[6][-1]
        elif number == 7:
            walking_dialogue(text_history, window, dia[7][0])
            answers[0] = dia[7][-1]
        elif number == 8:
            walking_dialogue(text_history, window, dia[8][0])
            answers[0] = dia[8][-1]
        elif number == 9:
            walking_dialogue(text_history, window, dia[9][0])
            answers[0] = dia[9][-1]
        elif number == 10:
            walking_dialogue(text_history, window, dia[10][0])
            answers[0] = dia[10][-1]

        window.mainloop()

    storyline()


def show_chapters():
    if len(chapter_for_show) > 0:
        chapter = chapter_for_show.pop(0)
        start_game(chapter)
    else:
        showwarning('Win', 'You ended game')


def start_game(chapter=None):
    global number
    number = 0
    if chapter is not None:
        data = chapter
    else:
        data = 'Chapter 1\n\nThe Ignition\n'
    button_start.destroy()
    walking_text(window, text_history, data, size=20)
    time.sleep(1)
    window.title('Game started')
    main_game()


def print_data(event):
    data = 'You play as a resident of a small town surrounded by dense forests,\n\n who suddenly finds themselves in the middle of a raging wildfire.\n\n Your goal is to escape the blaze and reach safety.'
    button_start.configure(state='disabled')
    walking_text(window, text_history, data)
    button_start.configure(state='active')


window = tkinter.Tk()
window_height = window.winfo_height()
window_width = window.winfo_width()
window.title('Escape The Blaze')
window.attributes('-fullscreen', True)
window.resizable(True, True)
window.configure(background=soft_bg)

text_history = tkinter.Label(window,
                             text='Press Enter To Begin',
                             background=soft_bg, foreground=soft_fr, font=('Arial', 14))
text_history.pack()
text_history.place(anchor='center', relx=0.5, rely=0.5)

button_start = tkinter.Button(window, text='START GAME', background=soft_bg, foreground=soft_fr, font=('Arial', 14),
                              command=start_game)

button_start.pack()
button_start.place(anchor='center', width=150, height=80, relx=0.5, rely=0.8)
window.bind('<Return>', print_data)
window.mainloop()
