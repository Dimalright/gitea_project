import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def browser():
    # Инициализация браузера перед запуском теста
    driver = webdriver.Chrome()
    yield driver
    # Закрытие браузера после выполнения теста
    driver.quit()


def test_register_new_user(browser):
    # Открываем страницу регистрации
    browser.get("http://localhost:3000/user/sign_up")

    # Заполняем поля для регистрации нового пользователя
    username_field = browser.find_element(By.CSS_SELECTOR, "input#user_name")
    username_field.send_keys("Dimalright")
    email_field = browser.find_element(By.NAME, "email")
    email_field.send_keys("gamdddd@mail.ru")
    password_field = browser.find_element(By.NAME, "password")
    password_field.send_keys("mypassword")
    password_confirm_field = browser.find_element(By.NAME, "retype")
    password_confirm_field.send_keys("mypassword")

    # Нажимаем кнопку "Регистрация аккаунта"
    register_button = browser.find_element(
        By.XPATH, "/html/body/div/div[2]/div/div/div/form/div[5]/button")
    register_button.click()

    # Проверяем, что пользователь успешно зарегистрирован и перенаправлен на главную страницу
    assert browser.current_url == "http://localhost:3000/"
