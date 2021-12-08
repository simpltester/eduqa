import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--maximized", action="store_true", help="full screen")
    parser.addoption("--headless", action="store_true", help="run headless")
    parser.addoption("--browser", action="store", choices=["chrome", "firefox", "opera"])
    parser.addoption("--url", action="store", default="http://localhost/")

@pytest.fixture
def browser(request):
    browser = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    maximized = request.config.getoption("--maximized")

    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "opera":
        driver = webdriver.Opera()

    return driver
    