from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.uix.bubble import Bubble
from kivy.uix.dropdown import DropDown 
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.uix.recycleview import RecycleView
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.vkeyboard import VKeyboard
from kivy.uix.screenmanager import ScreenManager, Screen
# Another way used for running kivy app
from kivy.base import runTouchApp





'''The Bubble widget is a form of menu or a small popup with an arrow arranged on one side of it’s content.

The Bubble contains an arrow attached to the content (e.g., BubbleContent) pointing in the direction you choose.
It can be placed either at a predefined location or flexibly by specifying a relative position on the border of the widget.'''



'''
Bubble
======

Test of the widget Bubble.
'''



# Builder.load_string('''
# <cut_copy_paste>
#     size_hint: (None, None)
#     size: (160, 120)
#     pos_hint: {'center_x': .5, 'y': .6}
#     BubbleContent:
#         BubbleButton:
#             text: 'Cut'
#             size_hint_y: 1
#         BubbleButton:
#             text: 'Copy'
#             size_hint_y: 1
#         BubbleButton:
#             text: 'Paste'
#             size_hint_y: 1
# ''')


class cut_copy_paste(Bubble):
    pass


class BubbleShowcase(FloatLayout):

    def __init__(self, **kwargs):
        super(BubbleShowcase, self).__init__(**kwargs)
        self.but_bubble = Button(text='Press to show bubble')
        self.but_bubble.bind(on_release=self.show_bubble)
        self.add_widget(self.but_bubble)

    def show_bubble(self, *l):
        if not hasattr(self, 'bubb'):
            self.bubb = bubb = cut_copy_paste()
            self.add_widget(bubb)
        else:
            values = ('left_top', 'left_mid', 'left_bottom', 'top_left',
                'top_mid', 'top_right', 'right_top', 'right_mid',
                'right_bottom', 'bottom_left', 'bottom_mid', 'bottom_right')
            index = values.index(self.bubb.arrow_pos)
            self.bubb.arrow_pos = values[(index + 1) % len(values)]


class TestBubbleApp(App):

    def build(self):
        return BubbleShowcase()


# if __name__ == '__main__':
#     TestBubbleApp().run()



'''Drop-Down List:

A versatile drop-down list that can be used with custom widgets.
It allows you to display a list of widgets under a displayed widget.
Unlike other toolkits, the list of widgets can contain any type of widget:simple buttons, images etc.

The positioning of the drop-down list is fully automatic:
we will always try to place the dropdown list in a way that the user can select an item in the list.'''



# create a dropdown with 10 buttons
dropdown = DropDown()
for index in range(10):
    # When adding widgets, we need to specify the height manually
    # (disabling the size_hint_y) so the dropdown can calculate
    # the area it needs.

    btn = Button(text='Value %d' % index, size_hint_y=None, height=44)

    # for each button, attach a callback that will call the select() method
    # on the dropdown. We'll pass the text of the button as the data of the
    # selection.
    btn.bind(on_release=lambda btn: dropdown.select(btn.text))

    # then add the button inside the dropdown
    dropdown.add_widget(btn)

# create a big main button
mainbutton = Button(text='Hello', size_hint=(None, None))

# show the dropdown menu when the main button is released
# note: all the bind() calls pass the instance of the caller (here, the
# mainbutton instance) as the first argument of the callback (here,
# dropdown.open.).
mainbutton.bind(on_release=dropdown.open)

# one last thing, listen for the selection in the dropdown list and
# assign the data to the button text.
dropdown.bind(on_select=lambda instance, x: setattr(mainbutton, 'text', x))

# runtouchApp:
# If you pass only a widget in runtouchApp(), a Window will
# be created and your widget will be added to the window
# as the root widget.

# runTouchApp(mainbutton)



'''The Popup widget is used to create modal popups.
By default, the popup will cover the whole “parent” window.
When you are creating a popup, you must at least set a Popup.title and Popup.content.'''

class TestPopup(App):
    def build(self):
        popup = Popup(title='Test popup',
            content=Label(text='Hello world'),
            size_hint=(None, None), size=(400, 400))
        
        return popup
    

# TestPopup().run()


'''Spinner is a widget that provides a quick way to select one value from a set.
In the default state, a spinner shows its currently selected value. 
Touching the spinner displays a dropdown menu with all the other available values from which the user can select a new one.

Simpler and less customizable than Dropdown menu

Kv Example:

FloatLayout:
    Spinner:
        size_hint: None, None
        size: 100, 44
        pos_hint: {'center': (.5, .5)}
        text: 'Home'
        values: 'Home', 'Work', 'Other', 'Custom'
        on_text:
            print("The spinner {} has text {}".format(self, self.text))'''

spinner = Spinner(
    # default value shown
    text='Home',
    # available values
    values=('Home', 'Work', 'Other', 'Custom'),
    # just for positioning in our example
    size_hint=(None, None),
    size=(100, 44),
    pos_hint={'center_x': .5, 'center_y': .5})

def show_selected_value(spinner, text):
    print('The spinner', spinner, 'has text', text)

spinner.bind(text=show_selected_value)

# runTouchApp(spinner)



'''RecycleView:
Recycleview helps to deal with a large number of data items.
Recycleview provides the user with the flexibility to scroll down or scroll-up the data displayed in the kivy application. 
You can also select multiple data items at once. Recycleview is memory efficient as compared to Listview.'''

 
# builder for recycleview
# Builder = Builder.load_string(
#     """
# <RV>:
#     viewclass: 'Button'
#     spacing: 10
#     padding: 10, 10
#     space_x: self.width
#     RecycleBoxLayout:
#         default_size: (dp(100), dp(100))
#         default_size_hint: (None, None)
#         size_hint_y: None
#         height: self.minimum_height
#         orientation: 'vertical'
#         RecycleBoxLayout:
#             orientation: 'vertical'
#             color: 0,0.4,0,0.8
#             default_size: (dp(100), dp(100))
#             default_size_hint: (0.4, None)
#             size_hint_y: None
#             height: self.minimum_height
#         """)
        
#class for recycleview
class RV(RecycleView):
    def __init__(self, **kwargs):
        #superclass for recycleview
        super(RV, self).__init__(**kwargs)
        self.data = [{'text': str(i)} for i in range(20)]
        
#class for app
class MyApp(App):
    def build(self):
        return RV()
        
# run app
# if __name__ == '__main__':
#     MyApp().run()




'''The TabbedPanel widget manages different widgets in tabs, with a header area for the actual tab buttons and a content area 
for showing the current tab content.

The TabbedPanel provides one default tab.'''

Builder.load_string("""

<Test>:
    size_hint: .5, .5
    pos_hint: {'center_x': .5, 'center_y': .5}
    do_default_tab: False

    TabbedPanelItem:
        text: 'first tab'
        Label:
            text: 'First tab content area'
    TabbedPanelItem:
        text: 'tab2'
        BoxLayout:
            Label:
                text: 'Second tab content area'
            Button:
                text: 'Button that does nothing'
    TabbedPanelItem:
        text: 'tab3'
        RstDocument:
            text:
                '\\n'.join(("Hello world", "-----------",
                "You are in the third tab."))
""")


class Test(TabbedPanel):
    pass


class TabbedPanelApp(App):
    def build(self):
        return Test()


if __name__ == '__main__':
    TabbedPanelApp().run()




'''VKeyboard is a Kivy onscreen keyboard. Its works are intended to be transparent to the user. 
Its layout is completely adjustable, and a button in the widget's bottom right allows you to swap between different layouts. 
Using the widget directly is NOT recommended.'''



# to create the vkeyboard
class Test(VKeyboard):
    user = VKeyboard()
 
# Create the App class
class VkeyboardKivyApp(App):
    def build(self):
        return Test()
 
# run the App
# if __name__ == '__main__':
#     VkeyboardKivyApp().run()

'''The screen manager is a widget dedicated to managing multiple screens for your application. 
The default ScreenManager displays only one Screen at a time and uses a TransitionBase to switch from one Screen to another.

Multiple transitions are supported based on changing the screen coordinates / scale or even performing fancy animation using custom shaders.'''




# Create both screens. Please note the root.manager.current: this is how
# you can control the ScreenManager from kv. Each screen has by default a
# property manager that gives you the instance of the ScreenManager used.


# Builder.load_string("""
# <MenuScreen>:
#     BoxLayout:
#         Button:
#             text: 'Goto settings'
#             on_press: root.manager.current = 'settings'
#         Button:
#             text: 'Quit'

# <SettingsScreen>:
#     BoxLayout:
#         Button:
#             text: 'My settings button'
#         Button:
#             text: 'Back to menu'
#             on_press: root.manager.current = 'menu'
# """)

# Declare both screens
class MenuScreen(Screen):
    pass

class SettingsScreen(Screen):
    pass

class TestApp(App):

    def build(self):
        # Create the screen manager
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(SettingsScreen(name='settings'))

        return sm

# if __name__ == '__main__':
#     TestApp().run()