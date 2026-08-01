import smtplib
import datetime as dt
import random
import pandas

# +++++++++++ PARCTICE ++++++++++++++ #
my_email = "sumitsheoran4264@gmail.com"
password = "uzvabppjbzvfkrbj"

# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.sendmail(from_addr=my_email, 
#                         to_addrs="sheorana691@gmail.com",
#                         msg="Subject:Hello\n\nThis is the body of my email.") 
#     connection.login(user=my_email, password=password)


# now = dt.datetime.now()
# weekday = now.weekday()
# if weekday == 2:
#     with open("Day-32/quotes.txt", mode="r") as quotes_files:
#         quotes = quotes_files.readlines()
#         quote = random.choice(quotes)
#     print(quote)

#     with smtplib.SMTP("smtp.gmail.com") as connection:
#         connection.starttls()
#         connection.login(user=my_email,password= password)
        
#         connection.sendmail(from_addr=my_email, 
#                             to_addrs=my_email,
#                             msg= f"Subject:Monday Motivation\n\n{quote}")


#_______________________________________________________________________________#
#========================== BIRTHDAY WISH ======================================#
#_______________________________________________________________________________#

# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
day = now.day
month = now.month
today = (month, day)


data = pandas.read_csv("Day-32/birthdays.csv")


birthday_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}


if today in birthday_dict:
    birtday_person = birthday_dict[today]
    PLACEHOLDER = "[NAME]"
    with open("Day-32/letter.txt") as letter:
        letter = letter.read()

        new_letter = letter.replace(PLACEHOLDER, birtday_person["name"])
        print(new_letter)



    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email,password=password)
        
        connection.sendmail(from_addr=my_email, 
                            to_addrs=birtday_person["email"],
                            msg= f"Subject: Happy Birthday\n\n{new_letter}")

    # with smtplib.SMTP("smtp.gmail.com") as connection:
    #     connection.starttls()
    #     connection.login(user= my_email, password=password)
    #     connection.sendmail(from_addr=my_email, to_addrs=my_email, msg=f"Subject:HAPPY BIRTHDAY\n\n{new_letter}")
        

