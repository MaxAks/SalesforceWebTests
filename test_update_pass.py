#Импорт необходимых компонентов
import pytest # Импорт pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # Драйвер ожидания загрузки
from selenium.webdriver.support import expected_conditions as EC #ожидаемые условия для отображения элемента
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException # Импорта модуля о ненайденом элементе
import time # импортируем модуль - нужен для работы с временем в системе
# Читаем файл с логином и паролем
def test_uptade_pass_in_sf():
    try: 
        with open("login-pass.txt", "r") as f: # Открываем файил лежадий в одной директории с файлом и открываем его в переменную r
            lines = f.readlines() # читаем файил построчно в переменную
            user_name = lines[0].rstrip('\n') # Удаляем из первой строчки знак переноса строки
            password = lines[1]
            link = "https://test.salesforce.com/"
            browser = webdriver.Chrome()
            browser.get(link)
            # Вводим логин и пароль и нажимаем войти
            delay = 1 # задержка ожидания при ожидании элемента
            element1 = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.ID, 'username'))) #presence_of_element_located #для ожидания появления элемента окна ввода user_name на странице.
            input1 = browser.find_element(By.ID, "username")
            input1.send_keys(user_name)
            element2 = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.ID, 'password')))
            input2 = browser.find_element(By.ID, "password")
            input2.send_keys(password)
            element3 = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.ID, 'Login')))
            button = browser.find_element(By.ID, "Login")
            button.click()
            #Проверка входа
            time.sleep(5)
            try: 
                check_error = browser.find_element(By.ID, "password-button") #Ищем сообщение о том что неправильный логин или пароль для входа
            except NoSuchElementException: # ожидаем что не найдем элемента с сообщением о неправильном логине и пароле
                pass # Если находим что элемента нет - пропускаем этот этап - вся логика в следущем шаге
            else: # Здесь если элемента нет об ошибке (check_error == False) то продолжаем работать. Если элемент есть (check_error == True), тогда не выполянеятся условие assert и тест падает с ошибкой о неправильныз логине и пароле.
                assert check_error == False, "Требуется смена пароля на аккаунте, зайдите в аккаунт в ручном режиме, обновите пароль и внесите новые данные в фаил login-pass.txt" # после равенства указывается текст ошибки в случае не правильности равенства
    finally:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(5) # необходим для отладки, убрать при прохождении теста
        # закрываем браузер после всех манипуляций
        browser.quit()

