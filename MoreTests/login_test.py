from selenium.webdriver.common.by import By
import pytest
import allure


@pytest.mark.parametrize(
    ('login', 'password'),
    [
        ('username', '123'),
        ('mathew', '1234'),
    ]
)
@allure.feature ('Login check')
@allure.story('Input invalid data')
def test_login_invalid_data(driver1, login, password):
    with allure.step(" Go to https://the-internet.herokuapp.com/login"):
     driver1.get("https://the-internet.herokuapp.com/login")

    with allure.step('Enter invalid data'):
     driver1.find_element(By.ID, "username").send_keys(login)
     driver1.find_element(By.ID, "password").send_keys(password)

    with allure.step("Click on Submit button"):
     driver1.find_element(By.CSS_SELECTOR, '[type="submit"]').click()

    validation = driver1.find_element(By.ID, "flash").text
    with allure.step("Check the validation message"):
     assert 'Your username is invalid!' in validation

@pytest.mark.parametrize(
    ('login', 'password'),
    [
        ('tomsmith', 'SuperSecretPassword!'),
    ]
)
@allure.feature ('Login check')
@allure.story('Input valid data')
def test_login_valid_data(driver1, login, password):
    with allure.step("Go to https://the-internet.herokuapp.com/login"):
     driver1.get("https://the-internet.herokuapp.com/login")

    with allure.step("Enter valid data"):
     driver1.find_element(By.ID, "username").send_keys(login)
     driver1.find_element(By.ID, "password").send_keys(password)

    with allure.step("Click on Submit button"):
     driver1.find_element(By.CSS_SELECTOR, '[type="submit"]').click()

    alert = driver1.find_element(By.ID, "flash").text
    with allure.step("Check the validation message"):
     assert 'You logged into a secure area!' in alert

