from selenium.webdriver.common.by import By



def test_open_browser(driver1):
    driver1.get("https://www.onliner.by/")


    catalogue = driver1.find_element(
        By.CSS_SELECTOR,
        '[href="https://catalog.onliner.by"] .b-main-navigation__text'
    )
    catalogue.click()

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
    assert temperature >= 0, "Температура ниже 0 — тест провален, температура выше 0 - тест пройден"

#не запускается с -headless