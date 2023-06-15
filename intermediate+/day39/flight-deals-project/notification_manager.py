import os
from twilio.rest import Client
from dotenv import load_dotenv


load_dotenv()
ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
FROM_PHONE_NUMBER = os.getenv("FROM_PHONE_NUMBER")
TO_PHONE_NUMBER = os.getenv("TO_PHONE_NUMBER")


class NotificationManager:

    def __init__(self):
        self.client = Client(ACCOUNT_SID, AUTH_TOKEN)

    def send_message(self, message):
        self.client.messages.create(
            body=message,
            from_=FROM_PHONE_NUMBER,
            to=TO_PHONE_NUMBER
        )
