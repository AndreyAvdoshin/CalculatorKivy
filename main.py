from kivymd.app import MDApp
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window

Window.size = (300, 450)

class Container(GridLayout):
    pass


class CalcApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        return Container()


if __name__ == '__main__':
    CalcApp().run()