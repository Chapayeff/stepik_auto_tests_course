from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/execute_script.html"



def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, "input_value")
    x_treas = browser.find_element(By.ID, "input_value")
    y = calc(int(x_treas.text))

    input5 = browser.find_element(By.ID, "answer")
    input5.send_keys(y)

    input1 = browser.find_element(By.ID, "robotCheckbox")
    input1.click()

    browser.execute_script("window.scrollBy(0, 100);")

    input2 = browser.find_element(By.ID, "robotsRule")
    input2.click()

    button = browser.find_element(By.CSS_SELECTOR, "[type = 'submit']")
    button.click()


finally:
    time.sleep(5)
    browser.quit()