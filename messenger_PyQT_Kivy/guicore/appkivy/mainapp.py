from kivy.app import App

from kivy.uix.pagelayout import PageLayout

from kivy.uix.boxlayout import BoxLayout

from kivy.uix.label import Label

from kivy.uix.actionbar import ActionBar

from kivy.uix.button import Button

from kivy.uix.textinput import TextInput

from kivy.base import runTouchApp

import settings

# # ********************************************
# from kivy.config import Config

# Config.set('graphics', 'resizable', '0')

# Config.set('graphics', 'width', settings.WIDTH)

# Config.set('graphics', 'height', settings.HEIGHT)
# ********************************************

class ContainerWidget(BoxLayout):

    def __init__(self, *args, **kwargs):

        super(ContainerWidget, self).__init__(*args, **kwargs)

        self.orientation = 'vertical'

        self.list_response = list()


    def display_set(self,response):

        self.ids.display.text = ''

        self.list_response.append(response + '\n')

        for itm in self.list_response:

            self.ids.display.text = self.ids.display.text + itm

    def clear(self):

        self.ids.input.text = ''



    def press_btn(self):

        self.ids.btn.bind(on_press = self.set_text_display)

    # def set_text_display(self,instance):
    #     self.ids.display.text = 'text'


class MainApp(App):

    def __init__(self, *args, **kwargs):

        super(MainApp, self).__init__(*args, **kwargs)

    def build(self):
        pass


# if __name__ == "__main__":

#     app=MainApp()

#     app.run()