import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def driver() :
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(3)
        yield driver
        driver.quit()






def test_brokenimage (driver) :
   driver.get("https://the-internet.herokuapp.com/")
   broken = driver.find_element(By.XPATH, value="//a[text()='Broken Images']")
   broken.click()
   title = driver.find_element(By.CSS_SELECTOR, 'h3')
   assert title.text == "Broken Images"














