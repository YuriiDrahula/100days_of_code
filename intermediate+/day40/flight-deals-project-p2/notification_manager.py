import os
import smtplib
from twilio.rest import Client
from dotenv import load_dotenv


load_dotenv()
ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
FROM_PHONE_NUMBER = os.getenv("FROM_PHONE_NUMBER")
TO_PHONE_NUMBER = os.getenv("TO_PHONE_NUMBER")
MY_EMAIL = os.getenv("MY_EMAIL")
MY_PASSWORD = os.getenv("MY_PASSWORD")


class NotificationManager:

    def __init__(self):
        self.client = Client(ACCOUNT_SID, AUTH_TOKEN)

    def send_message(self, message):
        self.client.messages.create(
            body=message,
            from_=FROM_PHONE_NUMBER,
            to=TO_PHONE_NUMBER
        )

    def send_emails(self, emails, message, google_flight_link):
        with smtplib.SMTP(host="smtp.office365.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_PASSWORD,
                to_addrs=emails,
                msg=f"Subject:Low Price Flight\n\n"
                    f"{message}\n {google_flight_link}"
            )
