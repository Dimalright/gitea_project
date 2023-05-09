import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# Используем fixture для инициализации браузера перед каждым тестом
@pytest.fixture
def browser():
    # Инициализация браузера перед запуском теста
    driver = webdriver.Chrome()
    yield driver
    # Закрытие браузера после выполнения теста
    driver.quit()

# Тест для создания нового репозитория
def test_create_new_repository(browser):
    # Входим в учетную запись
    browser.get('http://localhost:3000/user/login?redirect_to=%2f')
    username_field = browser.find_element(By.NAME, "user_name")
    username_field.send_keys('gamdddd@mail.ru')
    password_field = browser.find_element(By.ID, 'password')
    password_field.send_keys('mypassword')
    password_field.send_keys(Keys.RETURN)

    # Создаем новый репозиторий
    browser.get('http://localhost:3000/repo/create')
    repo_name_field = browser.find_element(By.ID, 'repo_name')
    repo_name_field.send_keys('new_repo_by_Dimalright')
    repo_description_field = browser.find_element(By.ID, 'description')
    repo_description_field.send_keys('selenium the best!')
    repo_submit_button = browser.find_element(
        By.XPATH, "/html/body/div/div[2]/div/div/form/div/div[8]/button")
    repo_submit_button.click()

    # Проверяем, что репозиторий успешно создан
    assert browser.current_url == 'http://localhost:3000/Dimalright/new_repo_by_Dimalright'
