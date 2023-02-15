import datetime
global stop_thread
FONT_TEXT_BOLD = ("Courrier", 15, "bold")
FONT_TEXT = ("Courrier", 15)
TAB_SYMPTOMS = [
    ("Céphalée-Brutale", 32),
    ("Conjonctivite", 44),
    ("Fièvre>40°C", 142),
    ("Otite", 220),
    ("Tête", 288),
    ("Toux", 289),
    ("Angine", 8),
]

DIC_PAYMENTS = {
    "Carte_bleue": "1",
    "Espece": "5",
}

INDEX_PATIENTS = {
    "patient1": "2",
    "patient2": "3",
}

DIC_MEDICAL_OFFICE = {
    "Cabinet_saint-ouen_l'aumône": "2",
    "Cabinet_taverny": "3",
    "Cabinet_Groslay": "4",
    "Cabinet_Argenteuil": "5",
}

SYMPTOMS_POS_SCROLL_INIT = []
PATIENTS_NAME_INIT = [("LASTNAME1", "FIRSTNAME1"), ("LASTNAME2", "FIRSTNAME2")]
SELECTION_PATIENT_ID_INIT = INDEX_PATIENTS["patient1"]
PAYMENT_ID_INIT = DIC_PAYMENTS["Carte_bleue"]
LOGIN_INIT = ""
PASSWORD_INIT = ""
MEDICAL_OFFICE_PRIORITY_ID_INIT = DIC_MEDICAL_OFFICE["Cabinet_saint-ouen_l'aumône"]
MEDICAL_OFFICE_SECONDARY_ID_INIT = DIC_MEDICAL_OFFICE["Cabinet_taverny"]

HOURS_MIN_INIT = "7"
MINUTES_MIN_INIT = "0"
HOURS_MAX_INIT = "8"
MINUTES_MAX_INIT = "0"
DATE_MIN_INIT = datetime.datetime.today().strftime('%d/%m/%Y')
DATE_MAX_INIT = datetime.datetime.today().strftime('%d/%m/%Y')
