from bs4 import BeautifulSoup
import requests
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

my_email = os.getenv("MY_EMAIL")
password = os.getenv("PASSWORD")
APP_URL = "https://appbrewery.github.io/instant_pot/"

response = requests.get(APP_URL)
contant =  response.text

soup = BeautifulSoup(contant, "html.parser")

price = soup.find(name="span", class_="a-offscreen").get_text()
price_without_currency = float(price.replace("$", ""))


if price_without_currency < float(100.00):
    

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email,password= password)
        message = f"Don't wait grab yours while supplies last at this special price ${price_without_currency}."
        connection.sendmail(from_addr=my_email, 
                            to_addrs=my_email,
                            msg= f"Subject:Buy Product\n\n{message}")