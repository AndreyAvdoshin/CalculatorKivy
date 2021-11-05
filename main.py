from kivymd.app import MDApp
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window

Window.size = (300, 450)

class Container(GridLayout):

    def clear(self):
        self.ids.text_label.text = ''


    def press_button(self, button):
        if self.ids.text_label.text == '0':
            self.ids.text_label.text = ''

        self.ids.text_label.text += str(button)


class CalcApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        return Container()


if __name__ == '__main__':
    CalcApp().run()