from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def open_main_page(self):
        self.driver.get('https://www.qa-practice.com/')

    def click_forms(self):
        forms = self.driver.find_element(By.XPATH, "//span[text()='Forms']")
        forms.click()

    def check_text(self, text):
        button_text = self.driver.find_element(By.CSS_SELECTOR,'a[href="/forms/practice-form"]')
        assert button_text.text == text, f"Ожидалось '{text}', получено '{button_text.text}'"


