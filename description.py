from selenium import webdriver
from selenium.webdriver.common.by import By
import time



browser = webdriver.Chrome()
browser.get("https://parsinger.ru/selenium/3/3.2.4/index.html")
button = browser.find_element(By.ID, "secret-key-button").click()
elem = browser.find_element(By.ID, "secret-key-button").get_attribute("data")


time.sleep(10)

print(elem)
time.sleep(10)

browser.quit()
