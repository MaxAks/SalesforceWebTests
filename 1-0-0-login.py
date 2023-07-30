#Импорт необходимых компонентов
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # Драйвер ожидания загрузки
from selenium.webdriver.support import expected_conditions as EC #ожидаемые условия для отображения элемента
from selenium import webdriver
# Читаем файл с логином и паролем
with open("login-pass.txt", "r") as f: # Открываем файил лещадий в одной директории с файлом и открываем его в переменную r
    lines = f.readlines() # читаем файил построчно в переменную
    user_name = lines[0].rstrip('\n') #читаем первую строчку файла, убираем символы переноса строки и записываем в переменную
    password = lines[1] #читаем втору строчку файла, не убираем символы переноса строки, потому их здесь нет и записываем в переменную

try: 
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
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10) # необходим для отладки, убрать при прохождении теста
    # закрываем браузер после всех манипуляций
    browser.quit()

