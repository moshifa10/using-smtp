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

        for index,info in enumerate(file_data):
            if index == 0:
                name = got.name.to_string()
                change = name.split()[-1] 
                info = info.replace("[NAME]", change)
                # print(x)
            clean_data.append(info)

        combined_email = ''.join(clean_data)
        # print(combined_email)

        # Now the implematation of email
        sendee_email = got.email.to_string()
        okay = sendee_email.split()[-1]
        try:
            with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
                connection.starttls()
                connection.login(user=email, 
                                 password=password)
                connection.sendmail(from_addr=email, 
                                    to_addrs=okay, 
                                    msg=f"Subject: Happy Birthday \n\n{combined_email}"
                                    )

        except TimeoutError as e:
            print(f"Not working: because {e}")

        else:
            print(f"Successfully sent an email to: {change}")
    





#  Now I am plannig something using streamlit