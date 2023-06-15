import os
from dotenv import load_dotenv
import requests
from datetime import datetime, timedelta
from twilio.rest import Client

load_dotenv()
STOCK = "TSLA"
COMPANY_NAME = "Tesla"

STOCK_API_KEY = os.getenv("STOCK_KEY")
STOCK_ENDPOINT = "https://www.alphavantage.co/query"

NEWS_API_KEY = os.getenv("NEWS_KEY")
NEW_ENDPOINT = "https://newsapi.org/v2/everything"

TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
FROM_PHONE_NUMBER = os.getenv("FROM_PHONE_NUMBER")
TO_PHONE_NUMBER = os.getenv("TO_PHONE_NUMBER")

today_date = datetime.today().date()
yesterday = str(today_date - timedelta(days=2))
day_before_yesterday = str(today_date - timedelta(days=3))

# STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
stock_params = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY
}

stock_response = requests.get(STOCK_ENDPOINT, params=stock_params)
stock_response.raise_for_status()
stock_data = stock_response.json()
yesterday_price = float(stock_data["Time Series (Daily)"][yesterday]["4. close"])
before_yesterday_price = float(stock_data["Time Series (Daily)"][day_before_yesterday]["4. close"])

day_difference = round(float(((before_yesterday_price - yesterday_price) * 100) / before_yesterday_price))
up_down = ""
if day_difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

# Get the first 3 news pieces for the COMPANY_NAME.
news_params = {
    "q": COMPANY_NAME,
    "from": yesterday,
    "sortBy": "popularity",
    "apiKey": NEWS_API_KEY
}

news_response = requests.get(NEW_ENDPOINT, params=news_params)
news_response.raise_for_status()
news_data = news_response.json()

popular_articles = news_data["articles"][:3]
headlines = [article["title"] for article in popular_articles]
descriptions = [article.get("description", "") for article in popular_articles]
descriptions = [string.replace('\r\n', '').replace('\xa0\xa0', '') for string in descriptions]


# Send a separate message with the percentage change and article's title and description to your phone number.
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)


def send_message():
    for i in range(3):
        client.messages.create(
            body=f"{STOCK}: {up_down}{day_difference}%\n"
                 f"Headline: {headlines[i]}\n"
                 f"Brief: {descriptions[i]}\n",
            from_=FROM_PHONE_NUMBER,
            to=TO_PHONE_NUMBER
        )


if -3 <= day_difference >= 3:
    send_message()
