#Импорт необходимых компонентов
import pytest # Импорт pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # Драйвер ожидания загрузки
from selenium.webdriver.support import expected_conditions as EC #ожидаемые условия для отображения элемента
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException # Импорта модуля о ненайденом элементе
import time # импортируем модуль - нужен для работы с временем в системе
# Читаем файл с логином и паролем
def test_account_check():
    try: 
        with open("login-pass.txt", "r") as f: # Открываем файил лежадий в одной директории с файлом и открываем его в переменную f
            lines = f.readlines() # читаем файил построчно в переменную
            user_name = lines[0].rstrip('\n')# Удаляем из первой строчки знак переноса строки
            password = lines[1]
            link = "https://test.salesforce.com/"
            browser = webdriver.Chrome()
            browser.get(link)
            # Вводим логин и пароль и нажимаем войти
            delay = 1 # задержка ожидания при ожидании элемента
            element1 = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.ID, 'username'))) #presence_of_element_located #для ожидания появления элемента окна ввода user_name в дереве на странице.
            input1 = browser.find_element(By.ID, "username")
            input1.send_keys(user_name)
            element2 = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.ID, 'password')))
            input2 = browser.find_element(By.ID, "password")
            input2.send_keys(password)
            element3 = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.ID, 'Login')))
            button = browser.find_element(By.ID, "Login")
            button.click()
            #Ожидание кнопки View Profile и ее нажатие
            element4 = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.slds-icon-waffle'))) # element_to_be_clickable проверяет что искомая иконка доступна для нажатия
            #time.sleep(5)
            button2 = browser.find_element(By.CSS_SELECTOR, '.slds-icon-waffle')
            button2.click()
            #Ожидание кнопки Settings и ее нажатие
            #time.sleep(5)
    finally:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(1) # необходим для отладки, убрать при прохождении теста
        # закрываем браузер после всех манипуляций
        browser.quit()
