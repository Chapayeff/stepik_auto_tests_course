from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/alert_accept.html"

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))
try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.CSS_SELECTOR, "[type = 'submit']")
    button.click()

    alert = browser.switch_to.alert
    alert.accept()

    x_element = browser.find_element(By.ID, "input_value")
    x_treas = browser.find_element(By.ID, "input_value")
    y = calc(int(x_treas.text))
    input5 = browser.find_element(By.ID, "answer")
    input5.send_keys(y)

    button = browser.find_element(By.CSS_SELECTOR, "[type = 'submit']")
    button.click()



finally:
    time.sleep(5)
    browser.quit()