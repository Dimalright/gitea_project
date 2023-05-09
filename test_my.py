import requests


def test_gitea_page():
    url = "http://localhost:3000/"
    expected_selectors = ["ui container", "center", "left-links"]
    expected_text = "Gitea: Git with a cup of tea"

    response = requests.get(url)

    assert response.status_code == 200, "Failed to load Gitea page"
    assert all(
        selector in response.text for selector in expected_selectors), "Failed to find expected CSS selectors"
    assert expected_text in response.text, "Failed to find expected text"
