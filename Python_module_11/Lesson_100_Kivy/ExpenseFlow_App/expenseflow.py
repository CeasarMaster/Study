from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.properties import DictProperty
from kivy.uix.popup import Popup
from datetime import datetime
import sqlite3
# Window.clearcolor = (0, 0, 0, 0.93)
 
Builder.load_file('transactions_popup.kv')

class MainScreen(Screen):
    pass
class CategoriesScreen(Screen):
    pass
class TransactionsScreen(Screen):
    pass
class AccountScreen(Screen):
    pass
class TransactionPopup(Popup):
    def add_transaction(self):
        current_time = datetime.now()
        date = f'{current_time.day}/{current_time.month}/{current_time.year}'
        time = f'{current_time.hour}:{current_time.minute}'
        amount = self.ids.transaction_amount.text
        category = self.ids.selected_category.text
        try:
            sqliteConnection = sqlite3.connect('/Users/nikitadereza/PycharmProjects/Study/Python_module_11/Lesson_100_Kivy/test.db')
            cursor = sqliteConnection.cursor()
            print('Succesfully connected to database')
            params = (date, time, category, amount)
            sqlite_insert_query = """INSERT INTO new_transaction(date,time,category,amount) VALUES(?,?,?,?)"""
            count = cursor.execute(sqlite_insert_query, params)
            sqliteConnection.commit()
            print('Record succesfully inserted into table', cursor.rowcount)
            cursor.close()

        except sqlite3.Error as error:
            print('Failed to insert data into table', error)

        finally:
            if sqliteConnection:
                sqliteConnection.close()
                print('Connection closed')
       

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
    
    # def show_transaction_popup(self, instance):
    #     popup = TransactionPopup()
    #     popup.open()



def main():
    pass
if __name__ == '__main__':
   ExpenseFlow().run