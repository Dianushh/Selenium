from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrom()
browser.get("https://parsinger.ru/html/watch/1/1_5.html")
product = browser.find_element(By.CLASS_NAME, "description")

data = product.text

print(data)
browser.quit()


