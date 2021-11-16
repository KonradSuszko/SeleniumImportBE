from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import pyautogui
import os
import time
import uuid

driver = webdriver.Chrome(os.getcwd() + "\chromedriver.exe")

qty = ['1',    '1',    '2',     '1',    '2',    '3',    '1',    '2',     '4',    '6']

driver.get("https://localhost:443")
driver.find_element(By.CLASS_NAME, "dropdown-item").click()
driver.find_element(By.LINK_TEXT , "Lampy zewnętrzne").click()
for i in range(7):
    items = driver.find_elements(By.XPATH, "//article[@class='product-miniature js-product-miniature']")
    items[i].click()
    try:
        main = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "qty"))
        )
    finally:
        quantity = driver.find_element(By.NAME , "qty")
        quantity.send_keys(Keys.CONTROL + "a")
        quantity.send_keys(qty[i])
        driver.find_element(By.XPATH, "//button[@data-button-action='add-to-cart']").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "//button[@class='btn btn-secondary']").click()
        driver.find_element(By.LINK_TEXT, "Lampy zewnętrzne").click()

driver.find_element(By.LINK_TEXT, "Oświetlenie").click()
driver.find_element(By.LINK_TEXT, "Gniazda i wyłączniki").click()
for i in range(3):
    items = driver.find_elements(By.XPATH, "//article[@class='product-miniature js-product-miniature']")
    items[i].click()
    try:
        main = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "qty"))
        )
    finally:
        quantity = driver.find_element(By.NAME , "qty")
        quantity.send_keys(Keys.CONTROL + "a")
        quantity.send_keys(qty[i])
        driver.find_element(By.XPATH, "//button[@data-button-action='add-to-cart']").click()
        time.sleep(5)
        driver.find_element(By.XPATH, "//button[@class='btn btn-secondary']").click()
        driver.find_element(By.LINK_TEXT, "Gniazda i wyłączniki").click()
driver.find_element(By.XPATH, "//div[@id='_desktop_cart']//a[@rel='nofollow']").click()
cart_elements = driver.find_elements(By.CLASS_NAME, 'cart-item')
cart_elements[3].find_element(By.CLASS_NAME, 'remove-from-cart').click()
driver.find_element(By.XPATH, "//a[@class='btn btn-primary']").click()
driver.find_element(By.NAME, "id_gender").click()
driver.find_element(By.NAME, "firstname").send_keys("Test")
driver.find_element(By.NAME, "lastname").send_keys("Testowy")
driver.find_element(By.NAME, "email").send_keys("test" + str(uuid.uuid4()) + "@jasniej.pl")
driver.find_element(By.NAME, "password").send_keys("haslo123")
driver.find_element(By.NAME, "birthday").send_keys("2000-01-01")
driver.find_element(By.NAME, "psgdpr").click()
driver.find_element(By.NAME, "continue").click()
try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "address1"))
    )
finally:
    driver.find_element(By.NAME, "address1").send_keys("Testowa 5")
    driver.find_element(By.NAME, "postcode").send_keys("99-900")
    driver.find_element(By.NAME, "city").send_keys("Testowo")
    driver.find_element(By.NAME, "confirm-addresses").click()
    driver.find_element(By.XPATH, "//button[@type='submit']")
    try:
        main = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "delivery_option_4"))
        )
    finally:
        driver.find_element(By.ID, "delivery_option_4").click()
        time.sleep(0.5)
        driver.find_element(By.NAME, "confirmDeliveryOption").click()
        try:
            main = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "payment-option-2"))
            )
        finally:
            driver.find_element(By.ID, "payment-option-2").click()
            driver.find_element(By.ID, "conditions_to_approve[terms-and-conditions]").click()
            time.sleep(1)
            driver.find_element(By.XPATH, "//button[@class='btn btn-primary center-block']").click()
            try:
                main = WebDriverWait(driver, 60).until(
                    EC.presence_of_element_located((By.XPATH, "//a[@title='Wyświetl moje konto klienta']"))
                )
            finally:
                time.sleep(5)
                driver.find_element(By.XPATH, "//a[@title='Wyświetl moje konto klienta']").click()
                driver.find_element(By.ID, "history-link").click()
                time.sleep(3)
                driver.find_element(By.XPATH, "//a[@data-link-action='view-order-details']").click()