import os
import smtplib

from dotenv import load_dotenv
from email.mime.text import MIMEText

from .. import config

load_dotenv()

def send(to: str, subject: str, html: str):
    server = smtplib.SMTP(config.SMTP_SERVER, config.SMTP_PORT)
    server.starttls()

    email_from = os.getenv('GMAIL_EMAIL')
    server.login(os.getenv('GMAIL_EMAIL'), os.getenv('GMAIL_PASSWORD'))

    msg = MIMEText(html, 'html')
    msg['Subject'] = subject
    msg['From'] = config.EMAIL_SENDER
    msg['To'] = to

    server.sendmail(email_from, to, msg.as_string())
    server.quit()
