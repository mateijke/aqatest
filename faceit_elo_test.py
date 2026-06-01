from selenium.webdriver.common.by import By
import time

def test_open_browser(browser):
    browser.get("https://www.faceit.com/en/home")
    time.sleep(50)
    profile = browser.find_element( By.CSS_SELECTOR,
    '.Avatar__AvatarHolder-sc-a5251ba3-1.iFpHgb img[src="https://distribution.faceit-cdn.net/images/be102466-b780-45c2-a2f5-e0e71cf76b76.jpg"]'
)
    profile.click()

    move_profile = browser.find_element( By.CSS_SELECTOR, value='.Button__StyledBase-sc-e7bb7161-0.ebUjxd')
    time.sleep(2)
    move_profile.click()

    elo = browser.find_element(By.CSS_SELECTOR, value='.styles__Flex-sc-574cca67-0.styles__Col-sc-574cca67-2.kBtOmH.kHRzTp .Text__StyledText-sc-7932e744-0.dnTRJv')
    elo_value = int(elo.text)
    expected_elo = 2000
    assert expected_elo == elo_value










