from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class MainWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"

        # Configure the root window
        self.title = "Réservation SOS MEDECINS VAL d'OISE"
        self.size = (900, 900)
        self.add_widget(Label(text="Fichier", size_hint=(1, 0.1)))
        self.filemenu_open = Button(text="Ouvrir", size_hint=(1, 0.1))
        self.filemenu_save_as = Button(text="Enregistrer sous", size_hint=(1, 0.1))
        self.add_widget(self.filemenu_open)
        self.add_widget(self.filemenu_save_as)


class MyApp(App):
    def build(self):
        return MainWindow()

if __name__ == "__main__":
    MyApp().run()