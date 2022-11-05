import tkinter as tk
import tkinter.filedialog as tfd
import tkinter.messagebox as tkm


def new_file():
    global file_name

    if file_name == 'untitled' and len(text_input.get(1.0, 'end')) != 0:
        if tkm.askokcancel('New file creation:', f'Do you want to save your previous changes to "{file_name}"'):
            save_as_file()
    file_name = 'untitled'
    text_input.delete(1.0, 'end')


def open_file():
    global file_name
    text_input.delete(1.0, 'end')
    file_name = tfd.askopenfilename()
    with open(file_name) as file:
        text_input.insert(1.0, file.read())


def save_as_file():
    global file_name
    file_name = tfd.asksaveasfilename()
    content = text_input.get(1.0, 'end')
    with open(file_name, 'w') as file:
        file.write(content)


def save_file():
    global file_name
    if file_name == 'untitled':
        save_as_file()
    else:
        content = text_input.get(1.0, 'end')
        with open(file_name, 'w') as file:
            file.write(content)


file_name = 'untitled'
window = tk.Tk()
window.geometry('400x400')
window.title('Notepad')
text_input = tk.Text(window, wrap='word')
text_input.place(x=0, y=0, relwidth=1, relheight=1)
main_menu = tk.Menu(window)
window.configure(menu=main_menu)
file_menu = tk.Menu(main_menu)
icon_open = tk.PhotoImage(file='Open-Folder-icon.png')
icon_new = tk.PhotoImage(file='Files-New-File-icon.png')
icon_save = tk.PhotoImage(file='Save-icon.png')
icon_save_as = tk.PhotoImage(file='save-icon (1).png')
main_menu.add_cascade(label='File', menu=file_menu)
file_menu.add_command(label='New', image=icon_new, command=new_file, compound='left')
file_menu.add_command(label='Open', image=icon_open, command=open_file, compound='left')
file_menu.add_command(label='Save', image=icon_save, command=save_file, compound='left')
file_menu.add_command(label='Save As', image=icon_save_as, command=save_as_file, compound='left')

window.mainloop()
