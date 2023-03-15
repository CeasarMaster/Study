import time
import os
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


def logic(i):
    with open(os.path.abspath(f'../Other/Chapters/{i}.txt'), encoding='UTF-8', mode='r') as file:
        data = chapter_dialogue(file.readlines())
        dia = []
        for line in data:
            now = time.localtime()
            current_time = time.strftime("%H:%M:%S", now)
            dia.append((f'\n{current_time} {line[1]}\n{line[2]}', line[-2]))
    return dia


def chapter_dialogue(chapter):
    data = []
    for i in chapter:
        data.append(i.split('__'))
    return data


def walking_text(window, label, data, font='Arial', size=14):
    label['text'] = f''
    label['font'] = (font, size)
    for i in data:
        time.sleep(0.01)
        label['text'] += f' {i}'
        window.update()


def walking_dialogue(text_history, window, data, font='Arial', size=14):
    text_history['font'] = (font, size)
    for i in data:
        time.sleep(0.01)
        text_history['text'] += f' {i}'
        window.update()
