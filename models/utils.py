import json
import tkinter
import datetime


def valid_time_slot_datetime(date_time_min, date_time_max):
    f = '%d/%m/%Y %H:%M'
    timemin_tmp = datetime.datetime.strptime(date_time_min, f)
    timemax_tmp = datetime.datetime.strptime(date_time_max, f)

    return timemin_tmp <= timemax_tmp


def reservation_time_verif_datetime(date_time_min, date_time_max, reservation_time):
    f = '%d/%m/%Y %H:%M'
    timemin_tmp = datetime.datetime.strptime(date_time_min, f)
    timemax_tmp = datetime.datetime.strptime(date_time_max, f)

    reservation_time_format = datetime.datetime.strptime(reservation_time, f)
    return timemin_tmp <= reservation_time_format <= timemax_tmp


def save_to_json(login, password, hours_min, minutes_min, hours_max, minutes_max, date_min,
                 date_max, selection_patient_id, symptoms_pos_scroll, payment_id,
                 medical_office_priority_id, medical_office_secondary_id, patients_name):
    serializer = {
        "login": login,
        "password": password,
        "hours_min": hours_min,
        "minutes_min": minutes_min,
        "hours_max": hours_max,
        "minutes_max": minutes_max,
        "date_min": date_min,
        "date_max": date_max,
        "selection_patient_id": selection_patient_id,
        "symptoms_pos_scroll": symptoms_pos_scroll,
        "payment_id": payment_id,
        "medical_office_priority_id": medical_office_priority_id,
        "medical_office_secondary_id": medical_office_secondary_id,
        "patients_name": patients_name,
    }
    json_object = json.dumps(serializer, indent=4)

    file = tkinter.filedialog.asksaveasfile(title="Enregistrer sous … un fichier",
                                            filetypes=[('jsons files', '.json')],
                                            defaultextension="*.*")
    file.write(json_object)
    file.close()


def convert_sosformat_datetime(datetime_sosformat):
    sos_date = datetime_sosformat[:13].replace("Le ", "")
    sos_time = datetime_sosformat[16:]
    new_format = sos_date + " " + sos_time
    return new_format


def load_from_json():
    file = tkinter.filedialog.askopenfilename(title="Ouvrir un fichier",
                                              filetypes=[('jsons files', '.json')])
    try:
        with open(file, 'r') as openfile:
            json_object = json.load(openfile)
        return json_object
    except FileNotFoundError:
        return None


def return_key_dic(dic, value):
    for key in dic.keys():
        if dic[key] == value:
            return key


def reservation_time_verif_datetime_multi(date_time_min, date_time_max, datetime_multi):
    lignes = datetime_multi.split("\n")

    for index in range(len(lignes)):
        ligne = lignes[index]
        reserv_datetime_format = ligne[:13].replace("Le ", "") + " " + ligne[16:]
        if reservation_time_verif_datetime(date_time_min, date_time_max, reserv_datetime_format):
            return index, len(lignes)

    return -1, -1


if __name__ == "__main__":
    # f = '%d/%m/%Y, %H:%M'
    # valid_time_slot_datetime(date_time_min, date_time_max):

    # date_time_min_tmp = '03/10/1985 20:10'
    # date_time_max_tmp = '03/10/1985 20:12'
    # print(valid_time_slot_datetime(date_time_min_tmp, date_time_max_tmp))

    # Le 10/01/2023 à 13:45
    # sos_date_tmp = sos_format_tmp[:13].replace("Le ","")
    # sos_time_tmp = sos_format_tmp[16:]

    # sos_format_tmp = "Le 10/01/2023 à 13:45"
    # print(convert_sosformat_datetime(sos_format_tmp))
    date_time_min_tmp = "12/01/2023 12:15"
    date_time_max_tmp = "12/01/2023 12:30"
    datetime_multi_tmp = \
        "Le 12/01/2023 à 11:30\n" \
        "Le 12/01/2023 à 11:45\n" \
        "Le 12/01/2023 à 12:15\n" \
        "Le 12/01/2023 à 13:00\n"
    print(reservation_time_verif_datetime_multi(date_time_min_tmp, date_time_max_tmp,
                                                datetime_multi_tmp))
