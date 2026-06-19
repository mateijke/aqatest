import pytest
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.homepage import Homepage
from pages.mainpage import HomePage

@pytest.fixture
def driver():
    options = Options()
    options.add_argument('--headless')
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()

    yield driver
    driver.quit()


def test5(driver):

    mainpage = HomePage(driver)

    mainpage.open_main_page()
    mainpage.click_forms()
    mainpage.check_text("Practice Form")
