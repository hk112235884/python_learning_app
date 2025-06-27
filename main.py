from kivy.app import App
from kivy.uix.label import Label

class PythonLearnApp(App):
    def build(self):
        return Label(text="Welcome to Python Learning App!")

PythonLearnApp().run()
