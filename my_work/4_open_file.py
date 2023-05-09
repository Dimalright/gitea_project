from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Указываем путь к драйверу Chrome и запускаем браузер
driver = webdriver.Chrome()
driver.get('http://localhost:3000/user/login?redirect_to=%2f')

# Входим в учетную запись
username_field = driver.find_element(By.NAME, "user_name")
username_field.send_keys('gamdddd@mail.ru')
password_field = driver.find_element(By.ID, 'password')
password_field.send_keys('mypassword')
password_field.send_keys(Keys.RETURN)

# открытие страницы файла
driver.get(
    "http://localhost:3000/Dimalright/new_repo_by_Dimalright/src/branch/main/file")

# получение текста файла

wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located(
    (By.XPATH, "/html/body/div/div[2]/div[2]/div[3]/div/div/table/tbody/tr/td[2]/code")))
file_text = element.text
# проверка соответствия текста файла оригинальному тексту
assert file_text == "I like selenium!!!!"

# закрытие браузера
driver.quit()
