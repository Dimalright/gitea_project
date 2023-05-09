import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Создание экземпляра веб-драйвера Chrome
driver = webdriver.Chrome()
driver.get('http://localhost:3000/user/login?redirect_to=%2f')

# Входим в учетную запись
username_field = driver.find_element(By.NAME, "user_name")
username_field.send_keys('gamdddd@mail.ru')
password_field = driver.find_element(By.ID, 'password')
password_field.send_keys('mypassword')
password_field.send_keys(Keys.RETURN)

time.sleep(2)
# Перейти на страницу созданного ранее репозитория
driver.get('http://localhost:3000/Dimalright/new_repo_by_Dimalright')

time.sleep(5)
# Переходим на создание "Нового фаила"
driver.get('http://localhost:3000/Dimalright/new_repo_by_Dimalright/_new/main/')

# Ввести имя файла
name_field = driver.find_element(By.XPATH, '//*[@id="file-name"]')
name_field.send_keys("file")

# Вводим описание для файла
editor_field = driver.find_element(
    By.XPATH, '/html/body/div[1]/div[2]/div[2]/form/div[2]/div[2]/div/div/div[1]/textarea')
editor_field.send_keys("I like selenium!!!!")

# Ввести сообщение коммита
commit_message = "Add new file!"
commit_field = driver.find_element(By.NAME, 'commit_summary')
commit_field.send_keys(commit_message)

# Нажать на кнопку "Сохранить правки"
driver.find_element(By.ID, 'commit-button').click()

# Закрыть браузер
driver.quit()
