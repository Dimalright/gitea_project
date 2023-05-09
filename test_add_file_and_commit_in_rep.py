
import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_create_new_file(browser):
    # Вход в учетную запись
    browser.get('http://localhost:3000/user/login?redirect_to=%2f')
    username_field = browser.find_element(By.NAME, "user_name")
    username_field.send_keys('gamdddd@mail.ru')
    password_field = browser.find_element(By.ID, 'password')
    password_field.send_keys('mypassword')
    password_field.send_keys(Keys.RETURN)
    time.sleep(2)

    # Перейти на страницу созданного ранее репозитория
    browser.get('http://localhost:3000/Dimalright/new_repo_by_Dimalright')
    time.sleep(5)

    # Переходим на создание "Нового файла"
    browser.get(
        'http://localhost:3000/Dimalright/new_repo_by_Dimalright/_new/main/')

    # Ввести имя файла
    name_field = browser.find_element(By.XPATH, '//*[@id="file-name"]')
    name_field.send_keys("file")

    # Вводим описание для файла
    editor_field = browser.find_element(
        By.XPATH, '/html/body/div[1]/div[2]/div[2]/form/div[2]/div[2]/div/div/div[1]/textarea')
    editor_field.send_keys("I like selenium!!!!")

    # Ввести сообщение коммита
    commit_message = "Add new file!"
    commit_field = browser.find_element(By.NAME, 'commit_summary')
    commit_field.send_keys(commit_message)

    # Нажать на кнопку "Сохранить правки"
    browser.find_element(By.ID, 'commit-button').click()
    time.sleep(3)

    browser.get(
        'http://localhost:3000/Dimalright/new_repo_by_Dimalright/src/branch/main')

    # Проверяем, что файл отображается на странице
    files = browser.find_elements(
        By.XPATH, '//*[@id="repo-files-table"]/tbody/tr/td[1]/span/a')
    assert any('file' in file.text for file in files), 'Файл не был создан'

    # Переходим на страницу истории коммитов
    browser.get(
        'http://localhost:3000/Dimalright/new_repo_by_Dimalright/commits/main')
    time.sleep(2)

    # Проверяем, что последний коммит отображается на странице
    commit_elements = browser.find_elements(
        By.XPATH, '//*[@id="commits-table"]/tbody')
    assert any(
        commit_message in commit.text for commit in commit_elements), 'Коммит не был создан'

    # Закрыть браузер
    browser.quit()
