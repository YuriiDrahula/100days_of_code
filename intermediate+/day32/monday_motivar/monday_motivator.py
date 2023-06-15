from random import choice
import smtplib
import datetime as dt

my_email = "ydtest97@hotmail.com"
password = "usmneuyhwbglmeqd"
current_date = dt.datetime.now()
current_day = current_date.weekday()

with open(file="quotes.txt") as file:
    quotes = file.readlines()
    motivation_phrase = choice(quotes)


if current_day == 0:
    with smtplib.SMTP(host="smtp.office365.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="ydtest17@yahoo.com",
            msg=f"Subject:Monday Motivation\n\n"
                f"{motivation_phrase}"
        )
