import pandas
import datetime as dt
import random
import smtplib
import os

MY_EMAIL = "costipen57@gmail.com"
PASSWORD = os.environ.get('GMAIL_PASS')

df = pandas.read_csv('birthdays.csv')
now = dt.datetime.now()
current_month = now.month
current_day = now.day

for index, row in df.iterrows():
    if row.month == current_month and row.day == current_day:
        birthday_email = row.email
        birthday_name = row['name']
        with open(f'./letter_templates/letter_{random.randint(1,3)}.txt') as letter:
            to_amend = letter.read()
            final_letter = to_amend.replace("[NAME]", birthday_name)
        with open(f"letter_to_{birthday_name}.txt", 'w') as file:
            file.write(final_letter)
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=birthday_email,
                msg=f"Subject:Birthday Wishes\n\n{final_letter}"
            )
