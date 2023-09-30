# # import requests

# # def get_exchange_rate(base_currency, target_currency):
# #     url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
# #     response = requests.get(url)
# #     data = response.json()
# #     exchange_rate = data["rates"][target_currency]
# #     return exchange_rate

# # base_currency = "USD"
# # target_currency = "EUR"
# # exchange_rate = get_exchange_rate(base_currency, target_currency)
# # print(f"Курс обмена {base_currency} к {target_currency} составляет {exchange_rate}")


# from kivy.app import App
# from kivy.uix.button import Button
# from kivy.uix.label import Label
# from kivy.uix.boxlayout import BoxLayout
# from kivy.uix.scrollview import ScrollView
# from kivy.uix.gridlayout import GridLayout

# class MyApp(App):

#     main_layout = BoxLayout(orientation='vertical')
#     top_layout = BoxLayout(orientation='horizontal')

#     scrollView = ScrollView()
#     gridLayout = GridLayout(size_hint_y=None)

#     gridLayout.cols = 1
#     gridLayout.padding = [0, 0, 0, 0]
#     gridLayout.bind(minimum_height=gridLayout.setter('height'))
#     scrollView.add_widget(gridLayout)

#     main_layout.add_widget(top_layout)
#     main_layout.add_widget(scrollView)

#     def btn_create(self, instance):
#         self.gridLayout.add_widget(Label(text='test', size_hint_y=None))

#     def btn_edit(self, instance):
#         pass

#     def btn_delete(self, instance):
#         pass

#     def build(self):
#         self.top_layout.size_hint=(1, .1)

#         # Button 'Erstellen'
#         btnCreate = Button()
#         btnCreate.text = 'Erstellen'
#         btnCreate.bind(on_press=self.btn_create)

#         # Button 'Bearbeiten'
#         btnEdit = Button()
#         btnEdit.text = 'Bearbeiten'
#         btnEdit.bind(on_press=self.btn_edit)

#         # Button 'Löschen'
#         btnDelete = Button()
#         btnDelete.text = 'Löschen'
#         btnDelete.bind(on_press=self.btn_delete)

#         self.top_layout.add_widget(btnCreate)
#         self.top_layout.add_widget(btnEdit)
#         self.top_layout.add_widget(btnDelete)

#         return self.main_layout

# if __name__ == '__main__':
#     MyApp().run()


# a = int(input('Insert the first number: '))
# b = int(input('Insert the second number: '))
# print(f'The sum of the two numbers: {a+b}')

for i in range(1, 1000000+1):
    print(i)
