#Monday Motivation Project
import smtplib
from datetime import datetime
import random
import pandas
myemail = "holly1233490@gmail.com"
password = "wrcvitovxfxzfocf"

today=(datetime.now().month,datetime.now().day)
data=pandas.read_csv("birthdays.csv")

new_dict={(data_row["month"],data_row["day"]):data_row for (index,data_row) in data.iterrows()}

if today in new_dict:
       no = random.randint(1, 3)
       filepath=f"letter_templates/letter_{no}.txt"
       with open(filepath) as letter_content:
              birthday_person=new_dict[today]
              content=letter_content.read()
              new_content=content.replace("[NAME]",birthday_person["name"])
       email=birthday_person["email"]


       with smtplib.SMTP("smtp.gmail.com") as connection:
              connection.starttls()
              connection.login(user=myemail, password=password)
              connection.sendmail(from_addr=myemail, to_addrs=email,msg=f"Subject:Happy Birthday!\n\n{new_content}")
              connection.close()





