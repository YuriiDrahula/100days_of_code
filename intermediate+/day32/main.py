import smtplib

my_email = "ydtest97@hotmail.com"
password = "usmneuyhwbglmeqd"

with smtplib.SMTP(host="smtp.office365.com", port=587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="ydtest17@yahoo.com",
        msg="Subject:Hello\n\n"
            "This is the body of my email"
    )

import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()
print(day_of_week)

date_of_birth = dt.datetime(year=1995, month=12, day=15)
print(date_of_birth)