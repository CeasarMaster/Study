import tkinter

window = tkinter.Tk()
window.title('Wildfires Text Quest')
window.geometry('1920x1080')
window.resizable(True, True)

button_start = tkinter.Button(window, text='START GAME')
button_start.place(x=0, y=0, width=100, height=40)
button_controls = tkinter.Button(window, text='CONTROLS')
button_controls.place(x=100, y=0, width=100, height=40)
button_manual=tkinter.Button(window,text='MANUAL')
button_manual.place(x=200,y=0,width=100,height=40)

window.mainloop()
