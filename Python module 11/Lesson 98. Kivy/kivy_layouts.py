from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy.core.window import Window

'''children is a ListProperty in kivy which defaults to an empty list.
add_widget() : add a widget as a child
remove_widget() : remove a widget from the children list
clear_widget() : remove all children from the list'''

'''BoxLayout: Arranges widgets in an adjacent manner (either vertically or horizontally) manner, to fill all the space.
The size_hint property of children can be used to change proportions allowed to each child, or set fixed size for some of them:

BoxLayout:
    BoxLayout:
        orientation: 'vertical' or 'horizontal'
        # this layout is populated with Button widgets in app code
        id: entries_box'''

class TestBox(App):
    def command(self, instance):
        temp_button = Button(text='New button')
        self.root.ids.entries_box.add_widget(temp_button)  # Get the configuration for the BoxLayout by id from test.kv
    def build(self):
        self.root = Builder.load_file('test.kv')
        return self.root


'''GridLayout: Arranges widgets in a grid.
 You must specify at least one dimension of the grid so kivy can compute the size of the elements and how to arrange them.'''
class TestGrid(App):

    def build(self):
        layout = GridLayout(cols=2)
        layout.add_widget(Button(text='Hello 1', size_hint_x=None, width=100))
        layout.add_widget(Button(text='World 1'))
        layout.add_widget(Button(text='Hello 2', size_hint_x=None, width=100))
        layout.add_widget(Button(text='World 2'))

        return layout


'''StackLayout: Arranges widgets adjacent to one another, but with a set size in one of the dimensions,
without trying to make them fit within the entire space. 
This is useful to display children of the same predefined size.'''
class TestStack(App):

    def build(self):
        root = StackLayout()
        for i in range(25):
            btn = Button(text=str(i), width=40 + i * 5, size_hint=(None, 0.15))
            root.add_widget(btn)
        return root

''' AnchorLayout: The AnchorLayout aligns its children to a border (top, bottom, left, right) or center.'''
class TestAnchor(App):
    def build(self):
        #Draw a button in the lower right corner:
        layout = AnchorLayout(anchor_x='right', anchor_y='bottom')
        btn = Button(text='Hello World')
        layout.add_widget(btn)
        

'''FloatLayout: Allows placing children with arbitrary locations and size, either absolute or relative to the layout size.
Default size_hint (1, 1) will make every child the same size as the whole layout,
so you probably want to change this value if you have more than one child.
You can set size_hint to (None, None) to use absolute size with size.
This widget honors pos_hint also, which as a dict setting position relative to layout position.'''
class TestFloat(App):
    def build(self):
        layout = FloatLayout(size=(300,300))
        button = Button(text='Hello float')
        layout.add_widget(button)
        return layout
app = TestFloat()
app.run()
