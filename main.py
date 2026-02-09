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
            name = name.replace("0", "").replace(" ", "")
            x = info.replace("[NAME]", name)
            clean_data.append(x)

        combined_email = ''.join(clean_data)
        # print(combined_email)

    

    

    

##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.




