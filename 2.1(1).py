from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "https://suninjuly.github.io/math.html"


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))
try:
    browser = webdriver.Chrome()
    browser.get(link)


    x_element = browser.find_element(By.ID, "input_value")
    input5 = browser.find_element(By.ID, "answer")
    x = x_element.text
    y = calc(x)
    input5.send_keys(y)

    input1 = browser.find_element(By.ID, "robotCheckbox")
    input1.click()

    input2 = browser.find_element(By.ID, "robotsRule")
    input2.click()


    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(5)
    browser.close()
    browser.quit()