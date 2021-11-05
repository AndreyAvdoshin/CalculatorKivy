from kivymd.app import MDApp
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window

Window.size = (300, 450)
formula = ''
result = False

class Container(GridLayout):

    def action(self, button):
        global formula
        global result
        if button not in formula[-1]:
            formula += button
            self.ids.text_label.text = ''
            result = False
        print(formula)


    def press_button(self, button):
        global formula
        global result
        if result:
            self.ids.text_label.text = ''
            formula = ''
            result = False
        if button == 'AC':
            self.ids.text_label.text = formula = ''

        elif self.ids.text_label.text == '0':
            if button == '.':
                self.ids.text_label.text += button
                formula += self.ids.text_label.text
            else:
                self.ids.text_label.text = ''
                self.ids.text_label.text = str(button)
                formula = self.ids.text_label.text

        elif button == '.' and button in self.ids.text_label.text:
            self.ids.text_label.text += ''
        
        else:
            self.ids.text_label.text += str(button)
            formula += str(button)
        print(formula)


    def equal(self):
        global formula
        global result
        try:
            self.ids.text_label.text = str(eval(formula))
            formula = self.ids.text_label.text
            result = True
        except Exception:
            self.ids.text_label.text = 'Ошибка'
            result = True


class CalcApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        return Container()


if __name__ == '__main__':
    CalcApp().run()