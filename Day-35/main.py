import requests
import smtplib

API_KEY = "2856d4e6bdd13bcae2180b8dc5f9fc58"

# parameters = {
#     "q": "Delhi",
#     "appid": API_KEY,
#     "units": "metric"
# }

# response = requests.get(
#     "https://api.openweathermap.org/data/2.5/weather",
#     params=parameters
# )

# data = response.json()


parameters = {
    "lat": 28.418700,
    "lon": 75.808960,
    "appid": API_KEY,
    "cnt": 4,
}

my_email = "sumitsheoran4264@gmail.com"
password = "uzvabppjbzvfkrbj"

with requests.get("https://api.openweathermap.org/data/2.5/forecast", params=parameters) as response:
    response.raise_for_status()
    weather_data = response.json()
    
    # print("\n")
    # print(weather_data["list"][0])
    # print("\n")
    # print(weather_data["list"][0]["weather"])

    # print(weather_data["list"][0]["weather"][0])
    # print(weather_data["list"][0]["weather"][0]["id"])
    
    will_rain = False
    for hour_data in weather_data["list"]:
        condition_code = hour_data["weather"][0]["id"]

        if int(condition_code) < 700:
            will_rain = True
    if will_rain:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=my_email,
                                msg="Don't forget your umbrella today, it looks like rain.")
            