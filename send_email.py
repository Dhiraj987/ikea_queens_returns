import smtplib, ssl
import datetime
from scraper import check_returns as is_returns_open


def generate_message_body(is_returns_open):
    if is_returns_open is True:
        body = "Yay, the returns is finally open!"
    else:
        body = "The returns in not yet open. Hang tight!"
    return body


message = f""" \
Subject: Ikea queens
{generate_message_body(is_returns_open)} \n
At {datetime.datetime.now().strftime("%d %B, %Y, %I:%M %p")}

"""

def send_email():
    port = 465
    smtp_server = "smtp.gmail.com"
    sender_email = "pythonemaildhiraj@gmail.com"
    receiver_email = "dhirajc963+ikea_update@gmail.com"
    password = input("Type your password and press enter: ")
    message = f""" \
    Subject: Ikea queens \ \n
    \n\n{generate_message_body(is_returns_open)} \
    \n
    At {datetime.datetime.now().strftime("%d %B, %Y, %I:%M %p")}

    """

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)

send_email()