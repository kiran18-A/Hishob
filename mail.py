from email.mime.text import MIMEText
from dotenv import load_dotenv

import smtplib
import os

load_dotenv()

from_mail=os.getenv('from_mail')
password=os.getenv('password')

def mail(mail):
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
         print("done")
     except Exception as e:
        print(e)