import requests
import sqlite3
from sqlite3 import Error
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.dropdown import DropDown
from kivy.uix.spinner import Spinner
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.core.window import Window

Window.clearcolor = (1, 1, 1, 1)
base_currency = 'USD'
target_currency = 'RUB'
url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
response = requests.get(url)
data = response.json()
exchange_rate = data["rates"]
login_data = {'user1' : '1234', 'user2' : '4543', 'user3' : '12345', 'user4' : '123456', 'user5' : '1234567'}

class LoginScreen(Screen):
    pass
class RegisterScreen(Screen):
    pass
class MainScreen(Screen):
    pass


class ConverterApp(App): # CoverterApp class runs the main application and calculates the value of the exchanged currencies

       
    def build(self): # Build window of application 
        self.load_kv('config.kv')
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='Login'))
        sm.add_widget(RegisterScreen(name='Register'))
        sm.add_widget(MainScreen(name='Main'))
        return sm
    
    def calculations(self, instance):  # Calculate the currency conversion
        if self.root.get_screen('Main').ids.currency_in.text == 'USD':
            result = float(self.root.get_screen('Main').ids.amount_in.text) * exchange_rate[self.root.get_screen('Main').ids.currency_out.text]
            
        else:
            usd = float(self.root.get_screen('Main').ids.amount_in.text) / exchange_rate[self.root.get_screen('Main').ids.currency_in.text]
            result = usd * exchange_rate[self.root.get_screen('Main').ids.currency_out.text]

        self.root.get_screen('Main').ids.amount_out.text = str(round(result,2))

    def login(self, instance):
        username = self.root.get_screen('Login').ids.username.text
        password = self.root.get_screen('Login').ids.password.text
        if username in login_data:
            if password == login_data[username]:
                self.root.current = 'Main'

        else:
            popup = Popup(title='Wrong Username or Password. Try again!', content=Label(text='Try Again'),
                            size_hint=(None, None), size=(410, 410), background='white_bg.png', 
                            title_color=(0, 0, 0, 1), separator_color=(0, 0, 0, 1))
            
            popup.open()
            self.root.get_screen('Login').ids.username.text = ''
            self.root.get_screen('Login').ids.password.text = ''

    def register(self, instance):
        new_username = self.root.get_screen('Register').ids.new_user.text
        new_password = self.root.get_screen('Register').ids.new_password.text
        if new_username in login_data:
            popup = Popup(title='Username Already Exists', content=Label(text='Try Again'),
                            size_hint=(None, None), size=(410, 410), background='white_bg.png', 
                            title_color=(0, 0, 0, 1), separator_color=(0, 0, 0, 1))
            popup.open()
            self.root.get_screen('Register').ids.new_user.text = ''
            self.root.get_screen('Register').ids.new_password.text = ''
        else:
            login_data[new_username] = new_password
            self.root.current = 'Login'

    
            



if __name__ == '__main__': # Run the application
    ConverterApp().run()


# screen = ScreenManager()
# self.title = 'Currency Converter'
# self.root = Builder.load_file('config.kv')  # Load the configuration file of the application (.kv)
# return self.root
    
    

        
        
        
     
      



