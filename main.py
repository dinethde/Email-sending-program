import datetime as dt
import smtplib
import pandas

MY_EMAIL = "smma.socialinfluence@gmail.com"
MY_PASSWORD = "bxjw aldi zwhe xngb"

date = dt.datetime.now()
DAY = date.day
MONTH = date.month
YEAR = date.year

file = pandas.read_csv('leadlist.csv')
data_dic = file.to_dict('records')

for item in data_dic:
    print(item)
    name = item['name']
    email = item['email']

    r_letter = 2
    letter_filename = f'letter_{r_letter}.txt'

    with open(f'letter_templates/{letter_filename}', encoding='utf-8') as letter_file:
        letter = letter_file.read()

    final_letter = letter.replace('[NAME]', name)

    print(final_letter)

    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=email,
            msg=f"Subject: The Real Secret to Getting 7 New Clients Every Month?\n\n{final_letter}"
        )



