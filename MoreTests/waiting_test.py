from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_wait(browser):
    browser.get("https://demoqa.com/dynamic-properties")

    wait = WebDriverWait(browser, 10)
    # Ждем появления кнопки
    button = wait.until(
        EC.visibility_of_element_located(
            (By.ID, "visibleAfter")
        )
    )

    # Получаем текст кнопки
    print(button.text)
    #Проверяем что текст тот
    assert button.text == "Visible After 5 Seconds"


def test_clickability(browser):

        browser.get("https://demoqa.com/dynamic-properties")

        wait = WebDriverWait(browser, 10)

        # Ждем пока кнопка станет активной
        button = wait.until(
            EC.element_to_be_clickable(
                (By.ID, "enableAfter")
            )
        )

        print(button.text)

        # Проверяем что кнопка активна
        assert button.is_enabled()

        # Проверяем текст
        assert button.text == "Will enable 5 seconds"










