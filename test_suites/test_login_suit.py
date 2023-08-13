#Импорт необходимых компонентов
import pytest # Импорт pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # Драйвер ожидания загрузки
from selenium.webdriver.support import expected_conditions as EC #ожидаемые условия для отображения элемента
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException # Импорта модуля о ненайденом элементе
import time # импортируем модуль - нужен для работы с временем в системе
# Читаем файл с логином и паролем

class Test_Login():
    def test_login_in_sf(self, browser, login_pass): # Тест проверяет правильность логина и пароля в текстововм файле. В скобках указываем какие фикстуры вызываем как атрибуты функции
        try: 
            link = "https://test.salesforce.com/"
            browser.get(link)
            # Вводим логин и пароль и нажимаем войти
            delay = 5 # задержка ожидания при ожидании элемента
            element1 = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.ID, 'username'))) #presence_of_element_located #для ожидания появления элемента окна ввода user_name на странице.
            input1 = browser.find_element(By.ID, "username")
            input1.send_keys(login_pass["user_name_key"]) # происходит обращение к кешу login_pass который был создан в фикстуре через ключ user_name_key
            element2 = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.ID, 'password')))
            input2 = browser.find_element(By.ID, "password")
            input2.send_keys(login_pass["password_key"]) # происходит обращение к кешу login_pass который был создан в фикстуре через ключ password_key
            element3 = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.ID, 'Login')))
            button = browser.find_element(By.ID, "Login")
            button.click()
            #Проверка входа 
            try: 
                check_error = browser.find_element(By.ID, "error") #Ищем сообщение о том что неправильный логин или пароль для входа
            except NoSuchElementException: # ожидаем что не найдем элемента с сообщением о неправильном логине и пароле
                pass # Если находим что элемента нет - пропускаем этот этап - вся логика в следущем шаге
            else: # Здесь если элемента нет об ошибке (check_error == False) то продолжаем работать. Если элемент есть (check_error == True), тогда не выполянеятся условие assert и тест падает с ошибкой о неправильныз логине и пароле.
                assert check_error == False, "Логин и пароль НЕ правильные" # после равенства указывается текст ошибки в случае не правильности равенства
        finally:
            # ожидание чтобы визуально оценить результаты прохождения скрипта
            time.sleep(5) # необходим для отладки, убрать при прохождении теста


    def test_uptade_pass_in_sf(self, browser, login_pass): # Тест проверяет необходимости смены пароля текущего пользователя
        try: 
            link = "https://test.salesforce.com/"
            browser = webdriver.Chrome()
            browser.get(link)
            # Вводим логин и пароль и нажимаем войти
            delay = 5 # задержка ожидания при ожидании элемента
            element1 = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.ID, 'username'))) #presence_of_element_located #для ожидания появления элемента окна ввода user_name на странице.
            input1 = browser.find_element(By.ID, "username")
            input1.send_keys(login_pass["user_name_key"]) # происходит обращение к кешу login_pass который был создан в фикстуре через ключ user_name_key
            element2 = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.ID, 'password')))
            input2 = browser.find_element(By.ID, "password")
            input2.send_keys(login_pass["password_key"]) # происходит обращение к кешу login_pass который был создан в фикстуре через ключ password_key
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