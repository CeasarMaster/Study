from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.checkbox import CheckBox
from kivy.uix.image import Image
from kivy.uix.slider import Slider
from kivy.uix.progressbar import ProgressBar
from kivy.uix.textinput import TextInput
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.switch import Switch
from kivy.uix.textinput import TextInput
from kivy.lang import Builder


'''The Label widget is for rendering text'''

class TestLabel(App):
    def build(self):
        # hello world text
        l = Label(text='Hello world')

        # unicode text; can only display glyphs that are available in the font
        unicode_text= Label(text='Hello world ' + chr(2764))

        # multiline text
        multiline = Label(text='Multi\nLine')

        # size
        font = Label(text='Hello world', font_size='20sp')


'''The Button is a Label with associated actions that are triggered when the button is pressed
(or released after a click/touch). To configure the button, the same properties (padding, font_size, etc)
and sizing system are used as for the Label class:

Kv Example: 
Button:
    text: 'press me'
    on_press: print("ouch! More gently please")
    on_release: print("ahhh")
    on_state:
        print("my current state is {}".format(self.state))'''

class TestButton(App):
    def build(self):
        button = Button(text='Hello world', font_size=14)


'''CheckBox is a specific two-state button that can be either checked or unchecked.
If the CheckBox is in a Group, it becomes a Radio button.
As with the ToggleButton, only one Radio button at a time can be selected when the CheckBox.group is set.'''

# def TestCheckBox(App):
#     def on_checkbox_active(checkbox, value):
#         if value:
#             print('The checkbox', checkbox, 'is active')
#         else:
#             print('The checkbox', checkbox, 'is inactive')

# checkbox = CheckBox()
# checkbox.bind(active=on_checkbox_active)


'''The Image widget is used to display an image.

Kv example: 
Image:
    source: 'mylogo.png'
    size: self.texture_size
'''

class MyApp(App):
  
    # defining build()
      
    def build(self):
          
        # return image
        return Image(source ='python.png')
  
# run the App
#MyApp().run()


'''The Slider widget looks like a scrollbar. It supports horizontal and vertical orientations, min/max values and a default value.

Kv example:

BoxLayout:
    Slider:
        id: slider
        min: 0
        max: 100
        step: 1
        orientation: 'vertical'

    Label:
        text: str(slider.value)'''


class TestSlider(App):
    
    def build(self):
        #To create a slider from -100 to 100 starting from 25:
        return Slider(min=-100, max=100, value=25)

        # #To create a vertical slider:
        # s = Slider(orientation='vertical')

        # # To create a slider with a red line tracking the value:
        # s = Slider(value_track=True, value_track_color=[1, 0, 0, 1])
#TestSlider().run()

'''The ProgressBar widget is used to visualize the progress of some task.'''

Builder.load_file('progress.kv')

class MyLayout(Widget):
	def press_it(self):
		# Grab the current progress bar value
		current = self.ids.my_progress_bar.value
		# If statement to start over after 100
		if current == 1:
			current = 0

		# Increment value by .25
		current += .25
		# Update the progress bar
		self.ids.my_progress_bar.value = current
		# Update the label
		self.ids.my_label.text = f'{int(current*100)}% Progress'

class AwesomeApp(App):
	def build(self):
		return MyLayout()


# if __name__ == '__main__':
# 	AwesomeApp().run()

    
'''The TextInput widget provides a box for editable plain text.'''

class TestTextInput(App):
      def build(self):
            #To create a singleline TextInput, set the TextInput.multiline property to False
            return TextInput(text='hello world', multiline=Falsemoon)
            
TestTextInput().run()