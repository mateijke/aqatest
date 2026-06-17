import pytest
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC





@pytest.mark.parametrize(
    ('login', 'password'),
    [
        ('test1508@test.com', '123456'),
    ]
)

def test_login(driver3, login, password):
    driver3.get("https://automationexercise.com/")
    driver3.find_element(By.CSS_SELECTOR, 'a[href="/login"]').click()

    driver3.find_element(By.CSS_SELECTOR, 'input[data-qa="login-email"]').send_keys(login)
    driver3.find_element(By.CSS_SELECTOR, 'input[data-qa="login-password"]').send_keys(password)

    driver3.find_element(By.CSS_SELECTOR, '[data-qa="login-button"]').click()

    driver3.get("https://automationexercise.com/product_details/2") #для обхода рекламы, много чего пробовал помогло только это

    quantity = driver3.find_element(By.ID, "quantity")
    quantity.clear()
    quantity.send_keys("2")


    driver3.find_element(By.CSS_SELECTOR, ".btn.btn-default.cart").click()

    driver3.find_element(By.CSS_SELECTOR, '[href="/view_cart"]').click()

    driver3.find_element(By.CSS_SELECTOR, ".btn.btn-default.check_out").click()
    driver3.get('https://automationexercise.com/payment') #ОБХОД РЕКЛАМЫ

    driver3.find_element(By.CSS_SELECTOR, ".form-control").send_keys("Matic")
    driver3.find_element(By.CSS_SELECTOR, '[data-qa="card-number"]').send_keys("353553677632")
    driver3.find_element(By.CSS_SELECTOR, ".card-expiry-month").send_keys("11")
    driver3.find_element(By.CSS_SELECTOR, ".card-expiry-year").send_keys("27")

    driver3.find_element(By.CSS_SELECTOR, ".submit-button").click()
    assert "Your order has been placed successfully!" in driver3.page_source
































