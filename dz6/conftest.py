import os
import pytest
from selenium import webdriver
from selenium.webdriver.opera.options import Options as OperaOptions

DRIVERS = os.path.expanduser("~/projects/browsers")

def pytest_addoption(parser):
    parser.addoption("--maximized", action="store_true", help="full screen")
    parser.addoption("--headless", action="store_true", help="run headless")
    parser.addoption("--browser", action="store", choices=["chrome", "firefox", "opera"], default="firefox")
    parser.addoption("--url", action="store", default="http://localhost/")
    parser.addoption("--timeout", type=int, default=5)

@pytest.fixture
def browser(request):
    browser_opt = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    maximized = request.config.getoption("--maximized")
    url = request.config.getoption("--url")
    timeout = request.config.getoption("--timeout")

    driver = None

    if browser_opt == "chrome":
        opts = webdriver.ChromeOptions()
        if headless:
            opts.headless = True
        driver = webdriver.Chrome(executable_path=f"{DRIVERS}/chromedriver", options=opts)
    elif browser_opt == "firefox":
        opts = webdriver.FirefoxOptions()
        if headless:
            opts.headless = True
        driver = webdriver.Firefox(executable_path=f"{DRIVERS}/geckodriver", options=opts)
    elif browser_opt == "opera":
        opts = OperaOptions()
        if headless:
            opts.headless = True
        driver = webdriver.Opera(executable_path=f"{DRIVERS}/operadriver")

    driver.t = timeout
    
    if maximized:
        driver.maximize_window()

    def close_browser():
        driver.quit()

    request.addfinalizer(close_browser)

    driver.get(url)
    driver.url = url

    return driver
