import tkinter
import time

from PIL import ImageTk, Image


def walking_text(data, font='Arial', size=14):
    label['text'] = f''
    label['font'] = (font, size)
    for i in data:
        time.sleep(0.04)
        label['text'] += f' {i}'
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
    text_history = tkinter.Text(window, state='disabled', bg='black', fg='white', font=('Arial', 14))
    text_entry = tkinter.Entry(window, width=230)
    text_entry.pack()
    text_entry.place(x=300, y=850, relheight=0.07)
    text_history.pack()
    text_history.place(x=0, y=0, relheight=0.75, relwidth=1)
    send = tkinter.Button(window, text='SEND', background='black', foreground='white', font=('Arial', 14))
    send.pack()
    send.place(x=1730, y=900)
    label_health = tkinter.Label(window, text='Health:', bg='black', fg='white', font=('Arial', 14))
    display_health = tkinter.Label(window, text='<==========>', bg='black', fg='white', font=('Arial', 14))
    label_hunger = tkinter.Label(window, text='Hunger:', bg='black', fg='white', font=('Arial', 14))
    display_hunger = tkinter.Label(window, text='<==========>', bg='black', fg='white', font=('Arial', 14))
    label_health.pack()
    label_hunger.pack()
    display_health.pack()
    display_hunger.pack()
    label_health.place(x=0, y=830)
    display_health.place(x=75, y=830)
    label_hunger.place(x=0, y=930)
    display_hunger.place(x=75, y=930)


window = tkinter.Tk()
window_height = window.winfo_height()
window_width = window.winfo_width()
print(window_width)
print(window_height)
window.title('Escape The Blaze')
window.attributes('-fullscreen', True)
#window.geometry('1920x1080')
window.resizable(True, True)
window.configure(background='black')
label = tkinter.Label(window,
                      text='Press Enter To Begin',
                      background='black', foreground='white', font=('Arial', 14))
label.pack()
label.place(anchor='center', relx=0.5, rely=0.5)

button_start = tkinter.Button(window, text='START GAME', background='black', foreground='white', font=('Arial', 14),
                              command=start_game)
button_start.pack()
button_start.place(anchor='center', width=150, height=80, relx=0.5, rely=0.8)
window.bind('<Return>', print_data)
window.mainloop()
