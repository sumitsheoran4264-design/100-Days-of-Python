from selenium import webdriver
from selenium.webdriver.common.by import By

# keep chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org")

events_dates = driver.find_elements(By.CSS_SELECTOR, value=".event-widget  time")

events_names = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")



events = {}

for n in range(0, len(events_dates)):
    events[n] = {
        "time": events_dates[n].text,
        "name": events_names[n].text
    }

print(events)
driver.quit() 