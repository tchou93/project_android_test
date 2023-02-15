from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.properties import StringProperty

# class CustomBoxLayout(BoxLayout):
#     var_hours_min = StringProperty()
#     var_minutes_min = StringProperty()
#     var_hours_max = StringProperty()
#     var_minutes_max = StringProperty()
#     var_select_patient = StringProperty()
#     var_payment_mode = StringProperty()
#     var_medical_office_priority = StringProperty()
#     var_medical_office_secondary = StringProperty()
#
#     def __init__(self, window, symptoms_pos_scroll, patients_name, hours_min, minutes_min,
#                  date_min, hours_max, minutes_max, date_max, selection_patient_id, payment_id,
#                  medical_office_priority_id, medical_office_secondary_id, **kwargs):
#         super().__init__(**kwargs)
#
#         self.var_hours_min = hours_min
#         self.var_minutes_min = minutes_min
#         self.var_hours_max = hours_max
#         self.var_minutes_max = minutes_max
#         self.var_select_patient = selection_patient_id
#         self.var_payment_mode = payment_id
#         self.var_medical_office_priority = medical_office_priority_id
#         self.var_medical_office_secondary = medical_office_secondary_id

        # self.patients_name = patients_name
        # self.date_min = date_min
        # self.date_max = date_max
        # self.symptoms_pos_scroll = symptoms_pos_scroll
        #
        # self.add_widget(Label(text='Patient Name:'))
        # self.add_widget(TextInput(text=self.var_select_patient, readonly=True))
        # self.add_widget(Button(text='Min Date', on_press=self.date_min))
        # self.add_widget(Button(text='Max Date', on_press=self.date_max))


# from tkinter import StringVar, Scrollbar, Listbox
# from tkinter.constants import END
# from tkcalendar import DateEntry
# from tktimepicker import constants, SpinTimePickerOld
# import customtkinter
#
# from models.global_var import DIC_PAYMENTS, DIC_MEDICAL_OFFICE, FONT_TEXT, TAB_SYMPTOMS, \
#     SYMPTOMS_POS_SCROLL_INIT, PATIENTS_NAME_INIT, \
#     SELECTION_PATIENT_ID_INIT, PAYMENT_ID_INIT, MEDICAL_OFFICE_PRIORITY_ID_INIT, \
#     MEDICAL_OFFICE_SECONDARY_ID_INIT, HOURS_MIN_INIT, MINUTES_MIN_INIT, \
#     MINUTES_MAX_INIT, HOURS_MAX_INIT, DATE_MIN_INIT, DATE_MAX_INIT
#
#
# class FrameAllInformations(customtkinter.CTkFrame):
#     def __init__(self, window, symptoms_pos_scroll, patients_name, hours_min, minutes_min,
#                  date_min, hours_max, minutes_max, date_max, selection_patient_id, payment_id,
#                  medical_office_priority_id, medical_office_secondary_id):
#         super().__init__(window)
#         self._corner_radius = 10
#         self.var_hours_min = StringVar()
#         self.var_minutes_min = StringVar()
#         self.var_hours_max = StringVar()
#         self.var_minutes_max = StringVar()
#         self.var_select_patient = StringVar()
#         self.var_payment_mode = StringVar()
#         self.var_medical_office_priority = StringVar()
#         self.var_medical_office_secondary = StringVar()
#         self.patients_name = patients_name
#         self.date_min = date_min
#         self.date_max = date_max
#
#         self.var_hours_min.set(hours_min)
#         self.var_minutes_min.set(minutes_min)
#         self.var_hours_max.set(hours_max)
#         self.var_minutes_max.set(minutes_max)
#         self.var_select_patient.set(selection_patient_id)
#         self.var_payment_mode.set(payment_id)
#         self.var_medical_office_priority.set(medical_office_priority_id)
#         self.var_medical_office_secondary.set(medical_office_secondary_id)
#         self.symptoms_pos_scroll = symptoms_pos_scroll
#
#         self.button_start = None
#         self.liste = None
#         self.button_date_max = None
#         self.button_date_min = None
#
#     def add_command_button_start(self, command):
#         self.button_start.configure(
#             command=lambda: command()
#         )
#
#     def create_widgets(self, font):
#         label_time_min = customtkinter.CTkLabel(
#             self,
#             text="Indiquez l'heure et le jour [MIN]:",
#             font=font
#         )
#
#         button_time_min = SpinTimePickerOld(self)
#         button_time_min._24HrsTime.configure(width=4)
#         button_time_min._24HrsTime.configure(textvariable=self.var_hours_min)
#         button_time_min._minutes.configure(width=4)
#         button_time_min._minutes.configure(textvariable=self.var_minutes_min)
#         button_time_min.addAll(constants.HOURS24)
#         self.button_date_min = DateEntry(
#             self,
#             width=10,
#             background="grey",
#             foreground="white",
#             locale="fr_FR",
#             bd=2
#         )
#         self.button_date_min.set_date(self.date_min)
#
#         label_time_max = customtkinter.CTkLabel(
#             self,
#             text="Indiquez l'heure et le jour [MAX]:",
#             font=font
#         )
#
#         button_time_max = SpinTimePickerOld(self)
#         button_time_max._24HrsTime.configure(width=4)
#         button_time_max._24HrsTime.configure(textvariable=self.var_hours_max)
#         button_time_max._minutes.configure(width=4)
#         button_time_max._minutes.configure(textvariable=self.var_minutes_max)
#         button_time_max.addAll(constants.HOURS24)
#         self.button_date_max = DateEntry(
#             self,
#             width=10,
#             background="grey",
#             foreground="white",
#             locale="fr_FR",
#             bd=2
#         )
#         self.button_date_max.set_date(self.date_max)
#         label_select_patient = customtkinter.CTkLabel(
#             self,
#             text="Sélectionnez un patient:",
#             font=font)
#         button1_select_patient = customtkinter.CTkRadioButton(
#             self,
#             text=f"{(self.patients_name[0])[0]} {(self.patients_name[0])[1]}",
#             # text="patient1",
#             variable=self.var_select_patient,
#             value="2",
#             border_width_unchecked=3,
#             border_width_checked=4
#         )
#         button2_select_patient = customtkinter.CTkRadioButton(
#             self,
#             text=f"{(self.patients_name[1])[0]} {(self.patients_name[1])[1]}",
#             # text="patient2",
#             variable=self.var_select_patient,
#             value="3",
#             border_width_unchecked=3,
#             border_width_checked=4
#         )
#         label_symptoms = customtkinter.CTkLabel(
#             self,
#             text="Sélectionnez vos symptômes:",
#             font=font
#         )
#         scrollbar = Scrollbar(
#             self,
#             orient="vertical"
#         )
#         self.liste = Listbox(
#             self,
#             selectmode="multiple",
#             heigh=4,
#             yscrollcommand=scrollbar.set
#         )
#
#         for (a, b) in sorted(TAB_SYMPTOMS, key=lambda s: s[0]):
#             self.liste.insert(END, a)
#         for index in self.symptoms_pos_scroll:
#             self.liste.selection_set(index)
#
#         label_payment_mode = customtkinter.CTkLabel(
#             self,
#             text="Sélectionnez un mode de paiement:",
#             font=font
#         )
#         button1_payment_mode = customtkinter.CTkRadioButton(
#             self,
#             text="Carte bleue",
#             variable=self.var_payment_mode,
#             value=DIC_PAYMENTS["Carte_bleue"],
#             border_width_unchecked=3,
#             border_width_checked=4
#         )
#         button2_payment_mode = customtkinter.CTkRadioButton(
#             self,
#             text="Espèce",
#             variable=self.var_payment_mode,
#             value=DIC_PAYMENTS["Espece"],
#             border_width_unchecked=3,
#             border_width_checked=4
#         )
#         label_medical_office_priority = customtkinter.CTkLabel(
#             self,
#             text="Sélectionnez le cabinet médical prioritaire:",
#             font=font
#         )
#         button1_medical_office_priority = customtkinter.CTkRadioButton(
#             self,
#             text="Cabinet saint-ouen l'aumône",
#             variable=self.var_medical_office_priority,
#             value=DIC_MEDICAL_OFFICE["Cabinet_saint-ouen_l'aumône"],
#             border_width_unchecked=3,
#             border_width_checked=4
#         )
#         button2_medical_office_priority = customtkinter.CTkRadioButton(
#             self,
#             text="Cabinet taverny",
#             variable=self.var_medical_office_priority,
#             value=DIC_MEDICAL_OFFICE["Cabinet_taverny"],
#             border_width_unchecked=3,
#             border_width_checked=4
#         )
#         button3_medical_office_priority = customtkinter.CTkRadioButton(
#             self,
#             text="Cabinet Groslay",
#             variable=self.var_medical_office_priority,
#             value=DIC_MEDICAL_OFFICE["Cabinet_Groslay"],
#             border_width_unchecked=3,
#             border_width_checked=4
#         )
#         button4_medical_office_priority = customtkinter.CTkRadioButton(
#             self,
#             text="Cabinet Argenteuil",
#             variable=self.var_medical_office_priority,
#             value=DIC_MEDICAL_OFFICE["Cabinet_Argenteuil"],
#             border_width_unchecked=3,
#             border_width_checked=4
#         )
#         label_medical_office_secondary = customtkinter.CTkLabel(
#             self,
#             text="Sélectionnez le cabinet médical secondaire:",
#             font=font
#         )
#         button1_medical_office_secondary = customtkinter.CTkRadioButton(
#             self,
#             text="Cabinet saint-ouen l'aumône",
#             variable=self.var_medical_office_secondary,
#             value=DIC_MEDICAL_OFFICE["Cabinet_saint-ouen_l'aumône"],
#             border_width_unchecked=3,
#             border_width_checked=4
#         )
#         button2_medical_office_secondary = customtkinter.CTkRadioButton(
#             self,
#             text="Cabinet taverny",
#             variable=self.var_medical_office_secondary,
#             value=DIC_MEDICAL_OFFICE["Cabinet_taverny"],
#             border_width_unchecked=3,
#             border_width_checked=4
#         )
#         button3_medical_office_secondary = customtkinter.CTkRadioButton(
#             self,
#             text="Cabinet Groslay",
#             variable=self.var_medical_office_secondary,
#             value=DIC_MEDICAL_OFFICE["Cabinet_Groslay"],
#             border_width_unchecked=3,
#             border_width_checked=4
#         )
#         button4_medical_office_secondary = customtkinter.CTkRadioButton(
#             self,
#             text="Cabinet Argenteuil",
#             variable=self.var_medical_office_secondary,
#             value=DIC_MEDICAL_OFFICE["Cabinet_Argenteuil"],
#             border_width_unchecked=3,
#             border_width_checked=4
#         )
#
#         self.button_start = customtkinter.CTkButton(
#             self,
#             text="Valider",
#             font=font,
#         )
#
#         label_time_min.grid(row=1, column=0, sticky="w", padx=5, pady=5)
#         button_time_min.grid(row=1, column=1, padx=5, pady=5)
#         self.button_date_min.grid(row=1, column=2, sticky="w", padx=5, pady=5)
#         label_time_max.grid(row=2, column=0, sticky="w", padx=5, pady=5)
#         button_time_max.grid(row=2, column=1, padx=5, pady=5)
#         self.button_date_max.grid(row=2, column=2, sticky="w", padx=5, pady=5)
#         label_select_patient.grid(row=3, column=0, sticky="w", padx=5, pady=5)
#         button1_select_patient.grid(row=3, column=1, sticky="w", padx=5, pady=5)
#         button2_select_patient.grid(row=3, column=2, sticky="w", padx=5, pady=5)
#         label_symptoms.grid(row=4, column=0, sticky="w", padx=5, pady=5)
#         self.liste.grid(row=4, column=1, sticky="e", pady=5)
#         scrollbar.config(command=self.liste.yview)
#         scrollbar.grid(row=4, column=2, sticky='nsw', pady=5)
#         label_payment_mode.grid(row=5, column=0, sticky="w", padx=5, pady=5)
#         button1_payment_mode.grid(row=5, column=1, sticky="w", padx=5, pady=5)
#         button2_payment_mode.grid(row=5, column=2, sticky="w", padx=5, pady=5)
#         label_medical_office_priority.grid(row=6, column=0, sticky="w", padx=5, pady=5)
#         button1_medical_office_priority.grid(row=6, column=1, sticky="w", padx=5, pady=5)
#         button2_medical_office_priority.grid(row=6, column=2, sticky="w", padx=5, pady=5)
#         button3_medical_office_priority.grid(row=6, column=3, sticky="w", padx=5, pady=5)
#         button4_medical_office_priority.grid(row=6, column=4, sticky="w", padx=5, pady=5)
#         label_medical_office_secondary.grid(row=7, column=0, sticky="w", padx=5, pady=5)
#         button1_medical_office_secondary.grid(row=7, column=1, sticky="w", padx=5, pady=5)
#         button2_medical_office_secondary.grid(row=7, column=2, sticky="w", padx=5, pady=5)
#         button3_medical_office_secondary.grid(row=7, column=3, sticky="w", padx=5, pady=5)
#         button4_medical_office_secondary.grid(row=7, column=4, sticky="w", padx=5, pady=5)
#         self.button_start.grid(row=8, column=0, sticky="w", padx=5, pady=5)
#
#         self.pack(fill="x", padx=10, pady=10)
#
#
# if __name__ == "__main__":
#     def func_testok():
#         date_min = frame.button_date_min.get_date()
#         date_min = date_min.strftime("%d/%m/%Y")
#         date_max = frame.button_date_max.get_date()
#         date_max = date_max.strftime("%d/%m/%Y")
#         print("date_min: " + date_min)
#         print("date_max: " + date_max)
#
#     app = customtkinter.CTk()
#     app.geometry("1000x1000")
#     app.minsize(800, 800)
#     app.maxsize(1000, 1000)
#
#     customtkinter.set_appearance_mode("Dark")
#     customtkinter.set_default_color_theme("dark-blue")
#     frame = FrameAllInformations(
#         window=app,
#         symptoms_pos_scroll=SYMPTOMS_POS_SCROLL_INIT,
#         patients_name=PATIENTS_NAME_INIT,
#         hours_min=HOURS_MIN_INIT,
#         minutes_min=MINUTES_MIN_INIT,
#         date_min=DATE_MIN_INIT,
#         hours_max=HOURS_MAX_INIT,
#         minutes_max=MINUTES_MAX_INIT,
#         date_max=DATE_MAX_INIT,
#         selection_patient_id=SELECTION_PATIENT_ID_INIT,
#         payment_id=PAYMENT_ID_INIT,
#         medical_office_priority_id=MEDICAL_OFFICE_PRIORITY_ID_INIT,
#         medical_office_secondary_id=MEDICAL_OFFICE_SECONDARY_ID_INIT,
#     )
#     frame.create_widgets(FONT_TEXT)
#     frame.add_command_button_start(func_testok)
#     app.mainloop()
