import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_view_file(browser):
    # Входим в учетную запись
    browser.get('http://localhost:3000/user/login?redirect_to=%2f')
    username_field = browser.find_element(By.NAME, "user_name")
    username_field.send_keys('gamdddd@mail.ru')
    password_field = browser.find_element(By.ID, 'password')
    password_field.send_keys('mypassword')
    password_field.send_keys(Keys.RETURN)

    # открытие страницы файла
    browser.get(
        "http://localhost:3000/Dimalright/new_repo_by_Dimalright/src/branch/main/file")

    # получение текста файла
    wait = WebDriverWait(browser, 10)
    element = wait.until(EC.presence_of_element_located(
        (By.XPATH, "/html/body/div/div[2]/div[2]/div[3]/div/div/table/tbody/tr/td[2]/code")))
    file_text = element.text

    # проверка соответствия текста файла оригинальному тексту
    assert file_text == "I like selenium!!!!"
