from selenium import webdriver
from selenium.webdriver.common.by import By


# keep chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.amazon.in/Duodeno-Saucepan-Boiling-Kitchen-Saucepen/dp/B0FH76K5JZ/ref=sr_1_1?crid=1PMZJ3V1NCQFR&dib=eyJ2IjoiMSJ9.DCvA9ltJcGo1t7MaWz3fsdH27dGtywcCKvjFg1aJSHEeUpIV-y1TKQ05uOReUfQYb2MstK1rX_snI6dK1439KRCC8sK0dQghPvjwBADmynsHbznHO6YnNm_9Opd2-wccIN_uykXMWWz1MuZPWe0YqU4w4osgjCwuK7umSxfS7_HXc2IWS166I8dFb5mAl7VPFoQVGPKcaqdSAKeyxwghU3yoluOXKDGf0PYAnmEiSkQ.3YD1CvNU0wRB9e0akl4Dhr9w0GHUoWMawv9xSTX4ubE&dib_tag=se&keywords=instant%2Bpot%2Bduo&qid=1786956393&sprefix=instant%2Bpot%2Bdu%2Caps%2C269&sr=8-1&th=1")

price = driver.find_element(By.CLASS_NAME, value="a-price-whole")
price_currency = driver.find_element(By.CLASS_NAME, value="a-price-symbol")
print(price_currency.text)
driver.quit()
