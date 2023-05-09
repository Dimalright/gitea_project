from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Указываем путь к драйверу Chrome и запускаем браузер
driver = webdriver.Chrome()
driver.get('http://localhost:3000/user/login?redirect_to=%2f')

# Входим в учетную запись
username_field = driver.find_element(By.NAME, "user_name")
username_field.send_keys('gamdddd@mail.ru')
password_field = driver.find_element(By.ID, 'password')
password_field.send_keys('mypassword')
password_field.send_keys(Keys.RETURN)

# Создаем новый репозиторий
driver.get('http://localhost:3000/repo/create')
repo_name_field = driver.find_element(By.ID, 'repo_name')
repo_name_field.send_keys('new_repo_by_Dimalright')

# Добавляем описание репозитория
repo_description_field = driver.find_element(By.ID, 'description')
repo_description_field.send_keys('selenium the best!')

# Создаем репозиторий
repo_submit_button = driver.find_element(
    By.XPATH, "/html/body/div/div[2]/div/div/form/div/div[8]/button")
repo_submit_button.click()

# Закрываем браузер
driver.quit()
