import tkinter as tk


def start_game():
    # code to start the game
    print("Starting the game...")


def load_game():
    # code to load the game
    print("Loading the game...")


def settings():
    # code to open settings menu
    print("Opening settings...")


def quit_game():
    # code to quit the game
    print("Quitting the game...")
    root.destroy()


root = tk.Tk()
root.attributes("-fullscreen", True)  # this will make the menu fullscreen
root.title("Game Menu")

start_button = tk.Button(root, text="Start Game", command=start_game)
start_button.pack()

load_button = tk.Button(root, text="Load Game", command=load_game)
load_button.pack()

settings_button = tk.Button(root, text="Settings", command=settings)
settings_button.pack()

quit_button = tk.Button(root, text="Quit Game", command=quit_game)
quit_button.pack()

root.mainloop()
