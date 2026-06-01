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
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver1 = webdriver.Chrome(options=options)
    driver1.implicitly_wait(10)
    driver1.maximize_window()
    yield driver1
    driver1.quit()

