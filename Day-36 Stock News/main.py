import requests
from twilio.rest import Client
import os

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = os.environ.get("STOCK_API_KEY")
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")
TWILIO_SID = os.environ.get("TWILIO_SID")
AUTH_TOKEN = os.environ.get("AUTH_TOKEN")
MOB_NO = os.environ.get("MOB_NO")


STOCK_PARAMS = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY
}

response = requests.get(STOCK_ENDPOINT, params=STOCK_PARAMS)
response.raise_for_status()
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]

difference = float(day_before_yesterday_closing_price) - float(yesterday_closing_price)
up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"


diff_percent = round(difference / float(yesterday_closing_price)) * 100

if diff_percent >= 5:
    NEWS_PARAMS = {
        "apikey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME
    }
    news_response = requests.get(NEWS_ENDPOINT, params=NEWS_PARAMS)
    news_response.raise_for_status()
    articles = news_response.json()["articles"]

    three_articles = articles[:3]

    formatted_article = [(f"{STOCK_NAME}: {up_down}{diff_percent}%\nHeadline: {article['title']}. "
                          f"\nBrief: {article['description']}")
                         for article in three_articles]

    client = Client(TWILIO_SID, AUTH_TOKEN)
    for article in formatted_article:
        message = client.messages.create(
            body=article,
            from_='+12568184743',
            to=MOB_NO
        )
