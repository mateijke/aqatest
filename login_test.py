from selenium.webdriver.common.by import By
import pytest


@pytest.mark.parametrize(
    ('login', 'password'),
    [
        ('username', '123'),
        ('mathew', '1234'),
    ]
)
def test_login_invalid_data(driver1, login, password):

    driver1.get("https://the-internet.herokuapp.com/login")

    driver1.find_element(By.ID, "username").send_keys(login)
    driver1.find_element(By.ID, "password").send_keys(password)

    driver1.find_element(By.CSS_SELECTOR, '[type="submit"]').click()

    validation = driver1.find_element(By.ID, "flash").text

    assert 'Your username is invalid!' in validation

@pytest.mark.parametrize(
    ('login', 'password'),
    [
        ('tomsmith', 'SuperSecretPassword!'),
    ]
)
def test_login_valid_data(driver1, login, password):
    driver1.get("https://the-internet.herokuapp.com/login")

    driver1.find_element(By.ID, "username").send_keys(login)
    driver1.find_element(By.ID, "password").send_keys(password)

    driver1.find_element(By.CSS_SELECTOR, '[type="submit"]').click()

    alert = driver1.find_element(By.ID, "flash").text
    assert 'You logged into a secure area!' in alert

