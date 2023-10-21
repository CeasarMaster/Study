from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label

class LoginScreen(GridLayout):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text = 'Username'))
        
        #To create a singleline TextInput, set the TextInput.multiline property to False 
        self.username = TextInput(multiline = False)
        self.add_widget(self.username)
        self.add_widget(Label(text = 'Password'))
        self.password = TextInput(password = True, multiline = False)
        self.add_widget(self.password)

class BasicApp(App):
    def build(self):
        return LoginScreen()
    
app = BasicApp()
app.run() 