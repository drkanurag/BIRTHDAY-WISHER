import random
import smtplib
import datetime as dt
import random
my_email = "anurag.podder@gmail.com"
password= "wqzcdtowibwtgfdt"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 1:
    with open("quotes.txt") as quotes_file:
        all_quotes = quotes_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="anurag.podder2@gmail.com",
        msg=f"Subject:Monday\n\n{quote}"
    )
    connection.close()








# import smtplib
#
# my_email = "anurag.podder@gmail.com"
# password = "wqzcdtowibwtgfdt"
# connection = smtplib.SMTP("smtp.gmail.com")
#
# connection.starttls()
# connection.login(user=my_email, password=password)
# connection.sendmail(
#     from_addr=my_email,
#     to_addrs="anurag.podder2@gmail.com",
#     msg="Subject:hello\n\nThis is the body of Email"
# )
# connection.close()
#

# import smtplib
#
# my_email = "anurag.podder@gmail.com"
# password = "wqzcdtowibwtgfdt"
#
# connection = smtplib.SMTP("smtp.gmail.com")
# connection.starttls()
# connection.login(user=my_email, password=password)
# connection.sendmail(from_addr=my_email, to_addrs="anurag.podder2@gmail.com", msg="Happy Birthday")
# connection.close()

# import datetime as dt

# now = dt.datetime.now()
# year = now.year
# month = now.month
# day = now.day
# print(f"Year is: {year}")
# print(f"Month is: {month}")
# print(f"Day is: {day}")
#
#
# date_of_birth = dt.datetime(year=1990, month=2, day=1)
# print(date_of_birth)
#
# now = dt.datetime.now()
# today = now.weekday()
# print(today)
