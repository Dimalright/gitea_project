import docker
import pytest
import requests


@pytest.fixture(scope="session")
def gitea_container():
    client = docker.from_env()
    container = client.containers.run(
        "gitea/gitea:1.15.5",
        detach=True,
        ports={"3000/tcp": ("127.0.0.1", 3000)},
        remove=True,
    )
    yield container
    container.stop()


@pytest.fixture(scope="session")
def gitea_url(gitea_container):
    ip_address = gitea_container.attrs["NetworkSettings"]["IPAddress"]
    return f"http://{ip_address}:3000/"


@pytest.fixture(scope="session")
def gitea_page(gitea_url):
    response = requests.get(gitea_url)
    return response


@pytest.fixture(scope="session")
def expected_selectors():
    return ["ui container", "center", "left-links"]


@pytest.fixture(scope="session")
def expected_text():
    return "expected text"
