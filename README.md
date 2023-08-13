# SalesforceWebTests
Automation tests for tests with Selenium Python different function of Saleforce

ENGLISH

To work with your credentials, you need to check all the selectors in the tests, they may differ when customizing your accounts.

FILE

====================== conftest.py ======================

A file that describes the data configuration in the test and the test environment.
The default configuration is to launch the browser for each function in the test and close the browser after the function completes.
The default browser is Chrome



====================== pytest.ini ======================

A file that contains existing markings for combining tests into a group.
To group tests, use the construct

====
@pytest.mark.regression
     def test_test

this construct will mark the test to run in the regression testing group
to call testing, it is the group of regression tests that must be specified when starting the test suite via the -m command

pytest -s -v -m "regression" test_test.py



====================== test_login_suit ======================

A test suite file containing tests for checking the correctness of the password, the need to enter a variation code or change the password



====================== login-pass.txt ======================

A text file containing the login and password for logging in to the Salesforce account.
The current file should be placed in the same directory as all files that refer to it in their code.
The file structure should look like this:
The first line is login
The second line is password
If the file structure is broken or the values are missing, then the test_login-1-0-0.py file will generate an error.



====================== test_login_in_sf.py =================== ===

This file takes login and password values line by line from the text file login-pass.txt (located in the same directory as the current file) and uses them to enter the sandbox (DEV, UAT, SIT environment) to verify the correct login and password. The file checks for login and password in a text file. If any of this is missing, an error is displayed indicating what exactly is missing. If the text file is filled incorrectly, an error is also displayed. After checking the text file, the current file enters the login and password values in the appropriate windows and logs in. If the login and password are not valid, then a message pops up about their incorrectness. If login and password match, the test succeeds.



====================== test_update_pass.py =================== ===

If the file test_login-1-0-0.py was successful and the login and password are correct, in this case the current file will check if the password needs to be changed on the user in use. If it is necessary to change the password, the test fails with an error and a recommendation to change the password. If the password does not need to be changed, the test succeeds.

>>> REQUIRED TO RECORD THAT THE FILE test_login-1-0-0.py WAS SUCCESSFUL



====================== test_verify_your_identity.py =================== ===

If the file test_login-1-0-0.py was successful and the login and password are correct, in this case the current file will check if you need to enter a verification code to enter the account. If you need to enter such a code, the test fails with an error and a recommendation to contact the Account Administrator. If you do not need to enter a variation code, the test is successful.

>>> REQUIRED TO RECORD THAT THE FILE test_login-1-0-0.py WAS SUCCESSFUL



====================== test_language_check.py =================== ===

If the test_login-1-0-0.py file was successful and the login and password are correct, in this case the current file will check which language is installed in the system and if not the English test is installed, it crashes.

>>> REQUIRED TO RECORD THAT THE FILE test_login-1-0-0.py WAS SUCCESSFUL



РУССКИЙ
Для работы с вашими учетными данными необходима проверка всех селекторов в тестах, они могут отличаться при кастомизации ваших учетных записей.

ФАЙЛЫ и ФУНКЦИИ

====================== conftest.py ======================

Файл, который описывает конфигурацию данных в тесте и тестовю среду.
По умолчанию установлена конфигурация запуска браузера для каждой функуии в тесте и закрытия браузера после завершения функции.
По умолчанию установлен браузер Chrome



====================== pytest.ini ======================

Файл, котороый содержит в себе существующие маркировки для объединения тестов в группу.
Для группировки тестов используйте констукцию 

====
@pytest.mark.regression
    def test_test

это конструкция пометит тест для запуска в группе регрессионного тестирования
для вызова тестирования именно группы регрессионых тестов необходим при запуске тестовго суита указать через команду -m

pytest -s -v -m "regression" test_test.py



====================== login-pass.txt ======================

Текстовый фаил содержаший в себе login и password для входа в учетную запись Salesforce.
Текуший фаил следует помещать в одну директорию со всеми файлами, которые ссылаются на него в своем коде.
Структура файла должна иметь следущий вид:
Первая строка - login
Вторая строка - password
ЕСли структура файла нарушена или значения отсутствуют то фаил test_login-1-0-0.py будет выдавать ошибку.


====================== test_login_suit ======================

Фаил тест-сьют, содержащий в себе тесты на проверку правильности пароля, необходимость ввода варификационного кода или смены пароля



====================== test_login_in_sf.py ======================

Данный файл берет из текстового файла login-pass.txt (лежит в одной директории, что и текущий файл) построчно значения login и password и использует их для входа в песочницу (среда DEV, UAT, SIT) для проверки правильности логина и пароля. Фаил проверяет наличие login и password в текстовом файле. Если чего-то из этого нет - выводится ошибка, что именно отсутствует. Если текстовый файил заполнен не корректно - ошибка выводится также. После проверки текстового файла, текущий фаил вводит значения login и password в соответствующие окна и осуществялет вход. ЕСли логин и пароль не валидны, то выскакиает сообщение об их некорректности. Если login и password подходят, тест заканчивается успехом.



====================== test_update_pass.py ======================

Если фаил test_login-1-0-0.py выполнился успешно и логин и пароль верны, в этом случае текущий фаил проверят необходимость смены пароля на используемом пользователе. В случае необходимости смены пароля, тест падает с ошибкой и рекомендацией сменить пароль. Если пароль менять не нужно тест выполняется успешно.

>>> НЕОБХОДИМО ЗАПИСАТЬ ПРОВЕРКУ, ЧТО ФАИЛ test_login-1-0-0.py БЫЛ ВЫПОЛНЕН УСПЕШНО



====================== test_verify_your_identity.py ======================

Если фаил test_login-1-0-0.py выполнился успешно и логин и пароль верны, в этом случае текущий фаил проверят необходимость ввода варификационного кода для входа в учетную запись. В случае необходимости ввода такого кода, тест падает с ошибкой и рекомендацией связаться с Администратором учетной записи. Если варификационный код вводить не нужно тест выполняется успешно.

>>> НЕОБХОДИМО ЗАПИСАТЬ ПРОВЕРКУ, ЧТО ФАИЛ test_login-1-0-0.py БЫЛ ВЫПОЛНЕН УСПЕШНО



====================== test_language_check.py ======================

Если фаил test_login-1-0-0.py выполнился успешно и логин и пароль верны, в этом случае текущий фаил проверят какой язык установлен в системе и если установлен не Аншлийский тест падает с ошибкой.

>>> НЕОБХОДИМО ЗАПИСАТЬ ПРОВЕРКУ, ЧТО ФАИЛ test_login-1-0-0.py БЫЛ ВЫПОЛНЕН УСПЕШНО