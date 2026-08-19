from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


driver = webdriver.Chrome(options=chrome_options)
driver.get("https://appbrewery.github.io/fake-newsletter-signup/")

name_input = driver.find_element(By.NAME, value="fName")
name_input.send_keys("Sumit", Keys.ENTER)

last_name = driver.find_element(By.NAME, value="lName")
last_name.send_keys("Sheoran")

email_adress = driver.find_element(By.NAME, value="email")
email_adress.send_keys("sumit333333@gmail.com")

button = driver.find_element(By.CLASS_NAME, value="btn-primary")
button.click()