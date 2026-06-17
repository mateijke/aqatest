import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def browser():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(5)

    yield browser
    browser.quit()


@pytest.fixture
def driver1():
    options = Options()

    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver1 = webdriver.Chrome(options=options)
    driver1.implicitly_wait(10)
    driver1.maximize_window()
    yield driver1
    driver1.quit()



import pytest
from _pytest.fixtures import SubRequest
from selenium import webdriver

def pytest_addoption (parser):
    parser.addoption("--browser")

@pytest.fixture
def driver2(request: SubRequest):
    if request.config.getoption("--browser") == "FF":
        driver2=webdriver.Firefox()
    elif request.config.getoption("--browser") == "Chrome":
        driver2=webdriver.Chrome()
    yield driver2
    driver2.quit()



@pytest.fixture
def driver3():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_experimental_option("prefs", {
        "profile.default_content_setting_values.notifications": 2,
        "profile.default_content_setting_values.popups": 2,
    })
    driver3 = webdriver.Chrome(options=chrome_options)
    yield driver3
    driver3.quit()

