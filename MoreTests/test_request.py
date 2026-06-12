import time

from selenium.webdriver.common.by import By



def test_one(driver2):
    driver2.get("https://www.google.com/")
    field = driver2.find_element(By.ID,"APjFqb")
    field.send_keys("lol")
    field.submit()

