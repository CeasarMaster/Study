from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.properties import DictProperty
from kivy.uix.popup import Popup
# Window.clearcolor = (0, 0, 0, 0.93)
 


class MainScreen(Screen):
    pass
class CategoriesScreen(Screen):
    pass
class TransactionsScreen(Screen):
    pass
class AccountScreen(Screen):
    pass



class ExpenseFlow(App):
    def build(self):
        self.load_kv('expenseflow_config.kv')
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='Main'))
        sm.add_widget(CategoriesScreen(name='Categories'))
        sm.add_widget(TransactionsScreen(name='Transactions')) 
        sm.add_widget(AccountScreen(name='Account'))
        sm.current = 'Main'
        return sm

    

if __name__ == '__main__':
    ExpenseFlow().run()