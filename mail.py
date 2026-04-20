from email.mime.text import MIMEText
from dotenv import load_dotenv
from database import mail_info
from datetime import date

import smtplib
import os
import time

today_date=date.today()
load_dotenv()
from_mail=os.getenv('from_mail')
password=os.getenv('password')

def mail(mail,name):
     subject="Welcome"
     body=(f"{name}\nYour account created successfully")
     msg=MIMEText(body)
     msg['Subject']=subject
     msg['To']=mail
     try:
         server=smtplib.SMTP("smtp.gmail.com",587)
         server.starttls()
         server.login(from_mail,password)
         server.send_message(msg)
         server.quit()
     except Exception as e:
        print(e)

def final_mail():
    result,today_income,today_expense=mail_info()
    user_t_income=0
    user_t_expense=0
    i=0
    while i<len(result):
        balance = result[i][3]-result[i+1][3]
        for j in today_income:
            if result[i][0]:
                user_t_income=j[1]
            else:
                user_t_income=0
        for k in today_expense:
            if result[i][0]:
                user_t_expense=k[1]
            else:
                user_t_expense=0
        subject="Report"
        body=f"{result[i][0]}\nToday you have {balance} on {today_date}\nExpenditure is {user_t_expense or 0} on {today_date}\nIncome is {user_t_income or 0} on {today_date}\nTill now your income is {result[i][3]} and expenditure is {result[i+1][3]} \nfrom the Hishob"
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['To'] = result[i][1]
        try:
            if result[i][1]=='demo@gmail.com':
                pass
            else:
                server = smtplib.SMTP("smtp.gmail.com", 587)
                server.starttls()
                server.login(from_mail, password)
                server.send_message(msg)
                server.quit()
        except Exception as e:
            print(e)
        i+=2
        time.sleep(10)

def send_mail():
    final_mail()