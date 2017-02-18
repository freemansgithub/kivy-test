# Third Party Libraries
from kivy.app import App  
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.lang import Builder

__version__ = '1.1'


class LoginPopup(Popup):
    pass

class MenuPopup(Popup):
    pass

class CityHunterRoot(FloatLayout):

    def login(self, text_input):
        layout = BoxLayout(orientation='vertical')
        text = Label(text="Hello, {}!".format(text_input))
        button = Button(text='push')
        layout.add_widget(text)
        layout.add_widget(button)
        pop_up = Popup(title="Our Title!", content=layout, size_hint=(.7, .7))
        pop_up.open()

    def menu(self, text_input):
        text = Label(text="Hello, {}!".format(text_input))
        pop_up = Popup(title="Our Title!", content=text, size_hint=(.7, .7))
        pop_up.open()


class CityHunterApp(App):

    def build(self):
        # self.root = Builder.load_file('test.kv')
        self.root = CityHunterRoot()
        # Return root widget 
        # return SimpleRoot()

    def on_start(self):
        root_widget = CityHunterRoot()
        root_widget.login('Please Login')

if __name__ == "__main__":  
    CityHunterApp().run()