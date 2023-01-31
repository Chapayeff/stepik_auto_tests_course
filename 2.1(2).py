from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/get_attribute.html"



def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)


    x_element = browser.find_element(By.ID, "treasure")
    x_treas = x_element.get_attribute("valuex")
    y = calc(x_treas)

    input5 = browser.find_element(By.ID, "answer")
    input5.send_keys(y)

    input1 = browser.find_element(By.ID, "robotCheckbox")
    input1.click()

    input2 = browser.find_element(By.ID, "robotsRule")
    input2.click()


    button = browser.find_element(By.CSS_SELECTOR, "[type = 'submit']")
    button.click()

finally:
    time.sleep(10)
    browser.quit()