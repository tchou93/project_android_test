# from kivy.app import App
# from kivy.uix.boxlayout import BoxLayout
# from kivy.uix.button import Button
# from models.sos_scrape import scrape_get_patient, scrape_sos
# from kivy.uix.dropdown import DropDown
# from models.global_var import SYMPTOMS_POS_SCROLL_INIT, HOURS_MIN_INIT, PATIENTS_NAME_INIT, \
#     MINUTES_MIN_INIT, DATE_MIN_INIT, HOURS_MAX_INIT, MINUTES_MAX_INIT, DATE_MAX_INIT, \
#     SELECTION_PATIENT_ID_INIT, PAYMENT_ID_INIT, MEDICAL_OFFICE_PRIORITY_ID_INIT, \
#     MEDICAL_OFFICE_SECONDARY_ID_INIT
# from views.view_frame_all_informations import CustomBoxLayout

# class MainWindow(BoxLayout):
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#         self.orientation = "vertical"
#
#         # Configure the root window
#         self.title = "Réservation SOS MEDECINS VAL d'OISE"
#         self.size = (900, 900)
#         self.filemenu_open = Button(text="Ouvrir", size_hint=(1, 0.1), size=(0, 40))
#         self.filemenu_open.bind(on_press=lambda x: scrape_get_patient())
#         self.filemenu_save_as = Button(text="Enregistrer sous", size_hint=(1, 0.1), size=(0, 40))
#         self.filemenu_save_as.bind(on_press=lambda x: scrape_sos(
#             login="tchou93@msn.com",
#             password="Angela93!",
#             time_date_format_min="02/02/2023 6:00",
#             time_date_format_max="02/02/2023 19:00",
#             patient_id=3,
#             symptoms_pos=(1, 2),
#             payment_mode_id=5,
#             medical_office_priority_id=5,
#             medical_office_secondary_id=2))
#         self.add_widget(self.filemenu_open)
#         self.add_widget(self.filemenu_save_as)
#
# class HelloWorldApp(App):
#     def build(self):
#         return MainWindow()
#         #             window=MainWindow(),
#         #             symptoms_pos_scroll=SYMPTOMS_POS_SCROLL_INIT,
#         #             patients_name=PATIENTS_NAME_INIT,
#         #             hours_min=HOURS_MIN_INIT,
#         #             minutes_min=MINUTES_MIN_INIT,
#         #             date_min=DATE_MIN_INIT,
#         #             hours_max=HOURS_MAX_INIT,
#         #             minutes_max=MINUTES_MAX_INIT,
#         #             date_max=DATE_MAX_INIT,
#         #             selection_patient_id=SELECTION_PATIENT_ID_INIT,
#         #             payment_id=PAYMENT_ID_INIT,
#         #             medical_office_priority_id=MEDICAL_OFFICE_PRIORITY_ID_INIT,
#         #             medical_office_secondary_id=MEDICAL_OFFICE_SECONDARY_ID_INIT,
#         # )

# if __name__ == "__main__":
#     HelloWorldApp().run()

from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

screen_helper = """

ScreenManager:
    MenuScreen:
    ProfileScreen:
    UploadScreen:

<MenuScreen>:
    name: 'menu'
    MDRectangleFlatButton:
        text: 'Profile'
        pos_hint: {'center_x':0.5,'center_y':0.6}
        on_press: root.manager.current = 'profile'
    MDRectangleFlatButton:
        text: 'Upload'
        pos_hint: {'center_x':0.5,'center_y':0.5}
        on_press: root.manager.current = 'upload'

<ProfileScreen>:
    name: 'profile'
    MDLabel:
        text: 'Profile'
        halign: 'center'
    MDRectangleFlatButton:
        text: 'Back'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'menu'

<UploadScreen>:
    name: 'upload'
    MDLabel:
        text: 'Upload'
        halign: 'center'
    MDRectangleFlatButton:
        text: 'Back'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'menu'

"""


class MenuScreen(Screen):
    pass


class ProfileScreen(Screen):
    pass


class UploadScreen(Screen):
    pass


# Create the screen manager
sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(ProfileScreen(name='profile'))
sm.add_widget(UploadScreen(name='upload'))


class DemoApp(MDApp):

    def build(self):
        screen = Builder.load_string(screen_helper)
        return screen


DemoApp().run()
