# Third Party Libraries
import kivy
kivy.require('1.9.1')

from kivy.app import App  
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.lang import Builder
from kivy.properties import NumericProperty, StringProperty
from kivy.garden.mapview import MapView

__version__ = '1.1'


class LoginPopup(Popup):
    pass


class MenuPopup(Popup):
    pass


class CityHunterRoot(FloatLayout):

    def __init__(self, **kwargs):
        super(CityHunterRoot, self).__init__(**kwargs)
        self.login_popup = LoginPopup()
        self.menu_popup = MenuPopup()
        self.map_widget = MapView(zoom=14, lon=50.6394, lat=3.057)

    def show_login(self):
        self.login_popup.ids.username.text = ''
        self.login_popup.ids.password.text = ''
        self.login_popup.open()

    def show_menu(self, user='Guest'):
        self.menu_popup.title = 'What {0} wants?'.format(user)
        self.menu_popup.open()

    def update(self, *args):
        self.ids.status.text = 'Welcome, {0}'.format(str(args[0]))

    def text(self):
        pass


class CityHunterApp(App):

    user = StringProperty()
    latitude = NumericProperty()
    longitude = NumericProperty()

    def build(self):
        self.user = 'Guest'
        # Return root widget
        return CityHunterRoot()

    def login(self, *args):
        self.root.update(*args)
        self.user = args[0]
        self.password = args[1]
        self.root.login_popup.dismiss()

    def logout(self):
        self.user = 'Guest'
        self.root.menu_popup.dismiss()
        self.root.show_login()

    def on_start(self):
        self.root.show_login()

    def on_pause(self):
        return True


if __name__ == "__main__":  
    CityHunterApp().run()