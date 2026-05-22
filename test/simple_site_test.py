from selenium.webdriver.common.by import By
import time
from pages.homepage import Homepage
from pages.product import ProductPage




def test_page_s6_open (browser) :
    homepage = Homepage(browser)
    homepage.open()
    homepage.click_galaxy_s6()
    product_page = ProductPage(browser)
    product_page.check_title("Samsung galaxy s6")

    browser.get('https://www.demoblaze.com/index.html')
    time.sleep(3)
    galaxy_s6 = browser.find_element(By.XPATH, value= "//a[text()='Samsung galaxy s6']")
    galaxy_s6.click()
    time.sleep(3)
    title = browser.find_element(By.CSS_SELECTOR, 'h2')
    assert title.text == "Samsung galaxy s6"


def test_counter (browser) :
    homepage = Homepage(browser)
    homepage.open()
    # browser.get('https://www.demoblaze.com/index.html')
    homepage.click_monitor()
    # monitor_link = browser.find_element(By.CSS_SELECTOR, value:='''[onclick="byCat('monitor')"]''')
    # monitor_link.click()
    time.sleep(3)
    homepage.check_products_counts(2)
    # monitors = browser.find_elements(By.CSS_SELECTOR, value:='.card')
    # assert len(monitors) == 2



