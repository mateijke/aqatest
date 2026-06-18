import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv

load_dotenv()
LOGIN = os.getenv("LOGIN")
PASSWORD = os.getenv("PASSWORD")


def test_login(driver3):
    driver3.get("https://www.saucedemo.com/")
    driver3.find_element(By.ID, 'user-name').send_keys(LOGIN)
    driver3.find_element(By.ID, 'password').send_keys(PASSWORD)
    driver3.find_element(By.ID, 'login-button').click()
    assert "/inventory.html" in driver3.current_url

    driver3.find_element(By.ID, 'item_0_title_link').click()

    button = driver3.find_element(By.ID, 'add-to-cart')
    assert button.text == "Add to cart"
    button.click()
    cart_badge = driver3.find_element(By.CLASS_NAME, 'shopping_cart_badge')
    assert cart_badge.text == "1"
    wait = WebDriverWait(driver3, 10)
    state_changed_button = wait.until(EC.presence_of_element_located((By.ID, 'remove')))
    assert state_changed_button.text == "Remove"

    driver3.find_element(By.CSS_SELECTOR, '.shopping_cart_link').click()
    driver3.find_element(By.ID, 'checkout').click()
    assert "/checkout-step-one" in driver3.current_url

    driver3.find_element(By.ID, 'first-name').send_keys("John")
    driver3.find_element(By.ID, 'last-name').send_keys("Doe")
    driver3.find_element(By.ID, 'postal-code').send_keys("12345")
    driver3.find_element(By.ID, 'continue').click()
    driver3.find_element(By.ID, 'finish').click()
    assert "Thank you for your order!" in driver3.page_source, "Текст подтверждения заказа не найден на странице"










