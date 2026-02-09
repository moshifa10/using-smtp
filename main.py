import smtplib
import random
import os
import pandas
import datetime as dt
from dotenv import load_dotenv


BIRTHDAY = "birthdays.csv"
random_templates = ["./letter_templates/letter_1.txt", "./letter_templates/letter_2.txt", "./letter_templates/letter_3.txt"]
load_dotenv()

email = os.getenv(key="MY_EMAIL")
password = os.getenv(key="MY_PASSWORD")

data = pandas.read_csv(BIRTHDAY)

today = dt.datetime.today()
month = today.month
day = today.day

got = data[(data["month"] == month) & (data["day"] == day)]

if not got.empty:
    print("Birthday Found!")

    # Open and get data and change the name
    chosen = random.choice(random_templates)
    with open(chosen) as file:
        file_data = file.readlines()
        clean_data = []

        for info in file_data:
            # print(type(info))
            # print(f"{got.name.to_string()}")
            name = got.name.to_string()
            print(name)
            name = name.replace("0", "").replace(" ", "")
            x = info.replace("[NAME]", name)
            clean_data.append(x)

        combined_email = ''.join(clean_data)
        # print(combined_email)

        # Now the implematation of email
        sendee_email = got.email.to_string()
        sendee_email = sendee_email.replace("0", "",count=1).replace(" ", "")
        # print(sendee_email)
        try:
            with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
                connection.starttls()
                connection.login(user=email, password=password)
                connection.sendmail(from_addr=email, to_addrs=sendee_email, msg=f"Subject: Happy Birthday \n\n{combined_email}")

        except TimeoutError as e:
            print(f"Not working: because {e}")

        else:
            print(f"Successfully sent an email to: {name}")
    




