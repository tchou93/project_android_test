from threading import Thread

from selenium.common import NoSuchElementException, ElementNotInteractableException, \
    ElementClickInterceptedException
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from models import global_var
from models.global_var import TAB_SYMPTOMS, DIC_MEDICAL_OFFICE
from models.utils import return_key_dic, reservation_time_verif_datetime_multi
import os
from selenium.webdriver.support.wait import WebDriverWait
from kivy.uix.label import Label
from browserstack.local import Local
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction



def scrape_get_patient():

    def test():
        wrong_pass_or_login = False
        patients_name = []
        desired_cap = {
            "browserName": "chrome",
            "device": "Samsung Galaxy S10",
            "realMobile": "true",
            "os_version": "8.0",
            "name": "Bstack-[Python] Sample Test"
        }
        # Create the WebDriver instance
        driver = webdriver.Remote(
            command_executor="http://tan.tran.workpro@gmail.com:Y6E1xGtPbqNMeqXv4i7y@hub-cloud.browserstack.com/wd/hub",
            desired_capabilities=desired_cap)
        driver.get("https://www.sosmedecins.com/patient/login")
        driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/form[1]/div[1]/div/input").send_keys("tchou93@msn.com")
        driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/form[1]/div[2]/div/div/input").send_keys("Angela93!")
        driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/form[1]/div[4]/button[1]").click()
        print("ok")
        try:
            driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/ul/li[2]/a").click()
        except NoSuchElementException:
            wrong_pass_or_login = True
        print("ok2")
        if not wrong_pass_or_login:
            for i in range(3, 5):
                print("ok3")
                try:
                    driver.find_element(By.XPATH, f"/html/body/div[2]/div[{i}]/div")
                    nom = driver.find_element(By.XPATH,
                                              f"/html/body/div[2]/div[{i}]/div/div[2]/h4").text[6:]
                    prenom = driver.find_element(By.XPATH,
                                                 f"/html/body/div[2]/div[{i}]/div/div[3]/h4").text[9:]
                    patients_name.append((nom, prenom))
                except NoSuchElementException:
                    break
        print(patients_name)
        driver.quit()

    t1 = Thread(target=test)
    t1.start()

def scrape_sos(login, password, time_date_format_min, time_date_format_max,
               patient_id, symptoms_pos, payment_mode_id,
               medical_office_priority_id, medical_office_secondary_id):
    def test():
        desired_cap = {
            "browserName": "chrome",
            "device": "Samsung Galaxy S10",
            "realMobile": "true",
            "os_version": "8.0",
            "name": "Bstack-[Python] Sample Test"
        }
        # Create the WebDriver instance
        driver = webdriver.Remote(
            command_executor="http://tan.tran.workpro@gmail.com:Y6E1xGtPbqNMeqXv4i7y@hub-cloud.browserstack.com/wd/hub",
            desired_capabilities=desired_cap)

        global_var.stop_thread = False
        # driver = webdriver.Chrome(service=Service(ChromeDriverManager(path=r"drivers").install()))
        print("ici1")
        try:
            driver.get("https://www.sosmedecins.com/patient/login")
            print("ici2")
            driver.find_element(By.XPATH,
                                "/html/body/div[2]/div[1]/form[1]/div[1]/div/input").send_keys(
                login)
            driver.find_element(By.XPATH,
                                "/html/body/div[2]/div[1]/form[1]/div[2]/div/div/input").send_keys(
                password)
            driver.find_element(By.XPATH,
                                "/html/body/div[2]/div[1]/form[1]/div[4]/button[1]").click()
            print("ici3")
            if not global_var.stop_thread:
                print("Etape 1/12: Entrer du login et passe")
                driver.find_element(By.XPATH, "/html/body/div[4]/select/option[9]").click()
            if not global_var.stop_thread:
                print("Etape 2/12: Selection val d'oise")
                driver.find_element(By.XPATH, "/html/body/div[6]/button[2]").click()
            if not global_var.stop_thread:
                print("Etape 3/12: Entrer dans le menu demander un RDV en consultation")
                driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/div[2]/button").click()
            if not global_var.stop_thread:
                print("Etape 4/12: Valider les conditions")
        except (Exception,):
            pass

        url_cabinet = driver.current_url
        cpt = 0

        while not global_var.stop_thread:
            cpt += 1
            if cpt % 7 == 0:
                choose_cabinet = medical_office_secondary_id
            else:
                choose_cabinet = medical_office_priority_id

            driver.get(url_cabinet)
            try:
                # detection du creneau
                if not global_var.stop_thread:
                    print("Etape 5/12: Vérifier la tranche horaire du ")
                else:
                    break

                datetime_multi = driver.find_element(
                    By.XPATH, f"/html/body/div[3]/div[{choose_cabinet}]/div/div[6]"
                )
                status_reserv = \
                    reservation_time_verif_datetime_multi(time_date_format_min,
                                                          time_date_format_max,
                                                          datetime_multi.text)

                if status_reserv != (-1, -1):
                    if not global_var.stop_thread:
                        # selection du cabinet
                        driver.find_element(
                            By.XPATH,
                            f"/html/body/div[3]/div[{choose_cabinet}]/div/div[8]/button"
                        ).click()
                        print("Etape 6/12: Selectionner le {medical_office_name}")
                    else:
                        break

                    # selection du nombre de patient
                    if not global_var.stop_thread:
                        driver.find_element(By.XPATH,
                                            "/html/body/div[3]/div[1]/div/div/div[1]/button").click()
                        print("Etape 7/12: Selection du nombre de patient")
                    else:
                        break
                    # premier créneau
                    if not global_var.stop_thread:
                        if status_reserv[1] == 1:
                            driver.find_element(By.XPATH,
                                                "/html/body/div[4]/div[1]/div/div/div/button").click()
                        else:
                            driver.find_element(
                                By.XPATH,
                                f"/html/body/div[4]/div[1]/div/div[{status_reserv[0] + 1}]/div/button"
                            ).click()
                        print("Etape 8/12: Choisir le créneau numéro {status_reserv[0]}")
                    else:
                        break

                    # selection du bon patient
                    if not global_var.stop_thread:
                        driver.find_element(
                            By.XPATH,
                            f"/html/body/div[3]/div[{patient_id}]/div/div[9]/div/button"
                        ).click()
                        print("Etape 9/12: Choisir le bon patient")
                    else:
                        break

                    if not global_var.stop_thread:
                        tab_symptoms_sorted = sorted(TAB_SYMPTOMS, key=lambda s: s[0])
                        for symptom in symptoms_pos:
                            symptom_id = (tab_symptoms_sorted[symptom])[1]
                            driver.find_element(
                                By.XPATH,
                                f"/html/body/div[4]/table/tbody/tr[{symptom_id}]"
                            ).click()
                        driver.find_element(
                            By.XPATH,
                            "/html/body/div[3]/div[2]/div[6]/form/div[2]/button"
                        ).click()

                        print("Etape 10/12: Choisir le(s) bon(s) symptome(s)")
                    else:
                        break

                    # Choix carte bleue
                    if not global_var.stop_thread:
                        driver.find_element(
                            By.XPATH,
                            f"/html/body/div[2]/form/div[1]/div/select/option[{payment_mode_id}]"
                        ).click()
                        driver.find_element(
                            By.XPATH,
                            "/html/body/div[2]/form/div[2]/div[2]/button"
                        ).click()
                        print("Etape 11/12: Choisir le bon moyen de paiement")

                    else:
                        break

                    # Confirmation de la demande
                    print("Etape 12/12: Confirmation de la demande")
                    print("Finish !")
                    path = os.getcwd()
                    driver.save_screenshot(f"{path}/datas/ss.png")
                    # TBD !!!dernière étape!!!
                    # Confirmation de la demande <TBD>
                    break
            except NoSuchElementException:
                pass
            except ElementNotInteractableException:
                pass
            except ElementClickInterceptedException:
                pass
            except (Exception,):
                pass

        driver.close()
        driver.quit()
    t2 = Thread(target=test)
    t2.start()