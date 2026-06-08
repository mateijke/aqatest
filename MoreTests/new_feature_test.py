from selenium.webdriver.common.by import By
from selenium import webdriver
import pytest
from selenium.webdriver.common.action_chains import ActionChains



def test_marketing(driver1):
    driver1.get("https://www.mageplaza.com/kb/magento-2-demo.html?utm_source=chatgpt.com")
    blog = driver1.find_element(By.ID, "homeMegaMenuBlog")
    marketing = driver1.find_element(By.CSS_SELECTOR, '[href="https://www.mageplaza.com/blog/marketing/"]')
    #ActionChains(driver1).move_to_element(blog).click(marketing).perform()
    actions = ActionChains(driver1)
    actions.move_to_element(blog)
    actions.click(marketing)
    actions.perform()



def test_dnd(driver1):
    driver1.get("https://www.qa-practice.com/elements/dragndrop/boxes")
    drag = driver1.find_element(By.ID, "rect-draggable")
    drop = driver1.find_element(By.ID, "text-droppable")
    ActionChains(driver1).drag_and_drop(drag,drop).perform()








