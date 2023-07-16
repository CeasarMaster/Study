import kivy
from kivy.app import App
from kivy.uix.pagelayout import PageLayout
from kivy.uix.recycleview import RecycleView
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.checkbox import CheckBox
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window


class TestApp(App):
    def command(self, instance):
        temp_button = Button(text='Новая кнопка')
        self.root.ids.entries_box.add_widget(temp_button) 

    def build(self):
        self.root = Builder.load_file('test.kv')
        return self.root


if __name__ == '__main__':
    TestApp().run()