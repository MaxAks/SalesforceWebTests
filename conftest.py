import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture(scope="function") # Фиксутар вызова и закрытия браузера с инциацией для каждой функции в тесте. При добавлении параметра autouse=True означает, что фикстура автоматически запускается для каждого теста без необхолимости вызова ее в тесте) 
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()

@pytest.fixture(scope="function") # Фиксутар вызова и закрытия браузера с инциацией для каждой функции в тесте. При добавлении параметра autouse=True означает, что фикстура автоматически запускается для каждого теста без необхолимости вызова ее в тесте) 
def login_pass():
    with open("login-pass.txt", "r") as f: # Открываем файил лежадий в одной директории с файлом и открываем его в переменную r
        lines = f.readlines() # читаем файил построчно в переменную
    if len(lines) == 2: # ПРоверяем что в файле 2 строки
        user_name = lines[0].rstrip('\n') # Удаляем из первой строчки знак переноса строки
        password = lines[1]
        if len(user_name) == 0 and len(password) > 1: #Если первая строка пустая а вторая нет
            assert len(user_name) != 0, "ВЫ НЕ УКАЗАЛИ Логин в файле login-pass.txt" # после равенства указывается текст ошибки в случае не правильности равенства
        elif len(user_name) > 0 and len(password) <= 1: # Если первая строка не пустая а вторая да
            assert len(password) > 1, "ВЫ НЕ УКАЗАЛИ ПАРОЛЬ НА ВТОРОЙ СТРОКЕ в файле login-pass.txt" # после равенства указывается текст ошибки в случае не правильности равенства
        else: # Когда и первая и вторая стоки не пустые выполняем основные действия.
            return {"user_name_key": user_name, "password_key": password} #создание хеша, который передается дальше в функции следующих тестов.
            pass
    elif len(lines) < 2: # если указали только логин и не указали пароль
        assert len(lines) >= 2, "Вы НЕ УКАЗАЛИ НИКАКОЙ ПАРОЛЬ в файле login-pass.txt"
    elif len(lines) >= 2: # если указали больше двух строк в файле
        assert len(lines) <= 2, "Вы ВВЕЛИ БОЛЬШЕ 2 СТРОК в файле login-pass.txt"
    else:
        assert len(lines) != 2, "ПРОВЕРЬТЕ ДАННЫЕ в файле login-pass.txt" # после равенства указывается текст ошибки в случае не правильности равенства