import time

import docker
import pytest
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture(scope="session")
def gitea_container():
    client = docker.from_env()
    container = client.containers.run(
        "pytest",
        detach=True,
        ports={"3000/tcp": ("localhost", 3000)},
        remove=True,
    )
    yield container
    container.stop()


@pytest.fixture(scope="session")
def gitea_url(gitea_container):
    return "http://localhost:3000/"


@pytest.fixture(scope="session")
def gitea_page(gitea_url):
    response = requests.get(gitea_url)
    return response


@pytest.fixture(scope="session")
def expected_selectors():
    return ["ui container", "center", "left-links"]


@pytest.fixture(scope="session")
def expected_text():
    return "Gitea: Git with a cup of tea"


def test_gitea_setup(gitea_container, gitea_url):
    assert gitea_container
    assert gitea_url == "http://localhost:3000/"
    time.sleep(5)


def test_gitea_installation(gitea_url):
    driver = webdriver.Chrome()
    driver.get(gitea_url)
    install_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "/html/body/div/div/div/div/div/form/div[17]/button"))
    )
    install_button.click()
    time.sleep(12)


def test_gitea_page(gitea_url, expected_selectors, expected_text):
    response = requests.get(gitea_url)
    assert response.status_code == 200, "Failed to load Gitea page"
    assert all(
        selector in response.text for selector in expected_selectors), "Failed to find expected CSS selectors"
    assert expected_text in response.text, "Failed to find expected text"
