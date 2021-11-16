from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import pyautogui
import os
import time

driver = webdriver.Chrome(os.getcwd() + "\chromedriver.exe")
driver.maximize_window()
driver.get("http:localhost:80/admin0009e8qap")
driver.find_element(By.ID, "email").send_keys("admin@jasniej.pl")
driver.find_element(By.ID, "passwd").send_keys("adminadmin")
driver.find_element(By.NAME, "submitLogin").submit()
try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "subtab-AdminAdvancedParameters"))
    )
finally:
    driver.find_element(By.ID, "subtab-AdminAdvancedParameters").click()
    #driver.find_element(By.ID, "subtab-AdminParentOrders").click()
    try:
        main = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "subtab-AdminImport"))
        )
    finally:
        time.sleep(1)
        driver.find_element(By.ID, "subtab-AdminImport").click()
        try:
            main = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "entity"))
            )
        finally:
            Select(driver.find_element(By.ID, "entity")).select_by_visible_text("Produkty")
            driver.find_element(By.ID, "file").send_keys(os.getcwd() + '\lamps2.csv')
            driver.find_element(By.ID, "truncate_1").click()
            #upload_element = driver.find_element(By.ID, "file-add-button")
            #upload_element.click()
            time.sleep(1)
            #pyautogui.write(os.getcwd() + '\lamps2.csv', interval=0.01)
            #pyautogui.press('return')
            #time.sleep(3)
            driver.find_element(By.NAME, "submitImportFile").click()
            time.sleep(0.3)
            alert_obj = driver.switch_to.alert
            alert_obj.accept()
            time.sleep(0.3)
            try:
                main = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID, "valueImportMatchs"))
                )
            finally:
                Select(driver.find_element(By.ID, "valueImportMatchs")).select_by_visible_text("import_git")
                driver.find_element(By.ID, "loadImportMatchs").click()
                driver.find_element(By.ID, "import").click()