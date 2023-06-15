from datetime import datetime
import pandas
import smtplib
import random

my_email = "ydtest97@hotmail.com"
password = "usmneuyhwbglmeqd"
now = datetime.now()
current_month = now.month
current_day = now.day


file = pandas.read_csv("birthdays.csv")
birthdays = file.to_dict(orient="records")
choice = random.randint(1, 3)

for birthday in birthdays:
    if current_month == birthday["month"] and current_day == birthday["day"]:
        with open(f".\\letter_templates\\letter_{choice}.txt") as file:
            letter = file.read()
            wish_letter = letter.replace("[NAME]", birthday["name"])
        with smtplib.SMTP(host="smtp.office365.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs="ydtest17@yahoo.com",
                msg=f"Subject:Happy Birthday, {birthday['name']}\n\n"
                    f"{wish_letter}"
            )
