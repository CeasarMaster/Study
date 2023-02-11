import tkinter
import time
from PIL import ImageTk, Image


def print_data(event):
    flag = False
    label['text'] = f''
    button_start.configure(state='disabled')
    for i in data:
        time.sleep(0.06)
        label['text'] += f' {i}'
        window.update()
    button_start.configure(state='active')


def start_game():
    window.title('Game started')


flag = True
data = 'You play as a resident of a small town surrounded by dense forests,\n\n who suddenly finds themselves in the middle of a raging wildfire.\n\n Your goal is to escape the blaze and reach safety.'
window = tkinter.Tk()
window.title('Escape The Blaze')
window.geometry('1920x1080')
window.resizable(True, True)
window.configure(background='black')
label = tkinter.Label(window,
                      text='Click anywhere to begin',
                      background='black', foreground='white', font=('Arial', 14))
label.pack()
label.place(anchor='center', relx=0.5, rely=0.5)

button_start = tkinter.Button(window, text='START GAME', background='black', foreground='white', font=('Arial', 14),
                              command=start_game)
button_start.pack()
button_start.place(anchor='center', width=150, height=80, relx=0.5, rely=0.8)
if flag:
    window.bind('<ButtonPress>', print_data)
window.mainloop()
