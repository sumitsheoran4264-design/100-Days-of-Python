import requests
import smtplib
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
API_KEY = "7O8KJUAA6HN0XQP3."
NEWS_API_KEY = "ecdb04fa31e642f4bfff1e841b2ca65f"

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": API_KEY
}
with requests.get(STOCK_ENDPOINT , params=stock_parameters) as response:
    response.json()
    data = response.json()["Time Series (Daily)"]
    data_list = [value for (key, value) in data.items()]
    yesterday_data = data_list[0]
    yesterday_closing_price = yesterday_data["4. close"]
    

    
day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]

difference = abs(float(yesterday_closing_price) - float(day_before_yesterday_closing_price))


diff_percent = (difference / float(yesterday_closing_price)) * 100
if diff_percent > 1:
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qinTitle": COMPANY_NAME
}
    with requests.get(NEWS_ENDPOINT, news_params) as news_response:
        articles = news_response.json()["articles"]
        three_articles = articles[:3]
    
                

    with smtplib.SMTP("smtp.gmail.com") as connection:
        my_email = "sumitsheoran4264@gmail.com"
        password = "uzvabppjbzvfkrbj"

        connection.starttls()
        connection.login(user=my_email, password=password)
        
        formated_article = [f"Headline: {article['title']}.\nBrief: {article['description']}" for article in three_articles]
        print(formated_article)
        # for article in formated_article:
        #     connection.sendmail(from_addr=my_email, 
        #                         to_addrs=my_email,
        #                         msg= f"Subject: Stocks Related\n\n{article}")
    
    