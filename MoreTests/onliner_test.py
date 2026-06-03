from selenium.webdriver.common.by import By
import allure


@allure.feature ('Temperature test')
@allure.story('Checking if the temperature <>0')
def test_open_browser(driver1):
    with allure.step('Go to https://www.onliner.by/'):
     driver1.get("https://www.onliner.by/")

    with allure.step("Find catalogue button"):
     catalogue = driver1.find_element(
        By.CSS_SELECTOR,
        '[href="https://catalog.onliner.by"] .b-main-navigation__text'
    )
    with allure.step('Click catalogue button'):
     catalogue.click()
    with allure.step('Find weather counter'):
     weather = driver1.find_element(
        By.CSS_SELECTOR,
        '[href="https://pogoda.onliner.by"] ._u'
    )

    temperature = int(
        weather.text
        .replace("+", "")
        .replace("°", "")
    )
    print(f"Температура: {temperature}°")

    with allure.step('Compare temperature with 0'):
     assert temperature >= 0, "Температура ниже 0 — тест провален, температура выше 0 - тест пройден"

#не запускается с -headless