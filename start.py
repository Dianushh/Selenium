import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def test_google_title():
    # Находим chromedriver.exe в папке проекта
    current_dir = os.path.dirname(os.path.abspath(__file__))
    driver_path = os.path.join(current_dir, 'chromedriver.exe')

    service = Service(executable_path=driver_path)
    driver = webdriver.Chrome(service=service)

    try:
        driver.get("https://www.google.com")
        print(f"\nТест пройден! Заголовок: {driver.title}")
        assert "Google" in driver.title
    finally:
        driver.quit()