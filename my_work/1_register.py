from selenium import webdriver
from selenium.webdriver.common.by import By

# Открываем браузер Chrome
driver = webdriver.Chrome()

# Переходим на страницу регистрации
driver.get("http://localhost:3000/user/sign_up")

# Находим поле "Имя пользователя" и заполняем его
username_field = driver.find_element(By.CSS_SELECTOR, "input#user_name")
username_field.send_keys("Dimalright")

# Находим поле "Адрес электронной почты" и заполняем его
email_field = driver.find_element(By.NAME, "email")
email_field.send_keys("gamdddd@mail.ru")

# Находим поле "Пароль" и заполняем его
password_field = driver.find_element(By.NAME, "password")
password_field.send_keys("mypassword")

# Находим поле "Введите пароль еще раз" и заполняем его
password_confirm_field = driver.find_element(By.NAME, "retype")
password_confirm_field.send_keys("mypassword")

# Нажимаем кнопку "Регистрация аккаунта"
register_button = driver.find_element(
    By.XPATH, "/html/body/div/div[2]/div/div/div/form/div[5]/button")
register_button.click()

# Закрываем браузер
driver.quit()
