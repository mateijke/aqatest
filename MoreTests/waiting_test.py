from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


@allure.feature ('WebDriverWaitPractice')
@allure.story('Waiting for element to be visible')
def test_wait(browser):
    with allure.step("Go to https://demoqa.com/dynamic-properties"):
     browser.get("https://demoqa.com/dynamic-properties")

    with allure.step("Wait for element to be visible"):
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
    with allure.step('Check if needed button has appeared'):
     assert button.text == "Visible After 5 Seconds"


@allure.feature ('WebDriverWaitPractice')
@allure.story('Waiting for element to color change')
def test_clickability(browser):
       with allure.step("Go to https://demoqa.com/dynamic-properties"):
        browser.get("https://demoqa.com/dynamic-properties")

        wait = WebDriverWait(browser, 10)

        # Ждем пока кнопка станет активной
        with allure.step("Wait for element to be active"):
         button = wait.until(
            EC.element_to_be_clickable(
                (By.ID, "enableAfter")
            )
        )

        print(button.text)

        # Проверяем что кнопка активна
        with allure.step("Check if needed button is active"):
         assert button.is_enabled()

        # Проверяем текст
         assert button.text == "Will enable 5 seconds"










