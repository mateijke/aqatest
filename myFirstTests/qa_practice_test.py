import pytest
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()

    yield driver
    driver.quit()


def test5(driver):

    driver.get("https://www.qa-practice.com/")
    button = driver.find_element(By.XPATH, "//span[text()='Forms']")
    button.click()

    title = driver.find_element(By.CSS_SELECTOR,'a[href="/forms/practice-form"]')
    assert title.text == "Practice Form"
