import os
import smtplib

from email.mime.text import MIMEText

from dotenv import load_dotenv
load_dotenv()

def send(to: str, subject: str, html: str):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    email_from = os.getenv('GMAIL_EMAIL')
    server.login(os.getenv('GMAIL_EMAIL'), os.getenv('GMAIL_PASSWORD'))

    msg = MIMEText(html, 'html')
    msg['Subject'] = subject
    msg['From'] = 'Team Arctus <team@arctus.me>'
    msg['To'] = to

    server.sendmail(email_from, to, msg.as_string())
    server.quit()
