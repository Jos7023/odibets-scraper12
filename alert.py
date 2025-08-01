import smtplib
from config import EMAIL, EMAIL_PASS, ALERT_TO

def send_error_email(subject, body):
    msg = f"Subject: {subject}\n\n{body}"
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(EMAIL, EMAIL_PASS)
        server.sendmail(EMAIL, ALERT_TO, msg)