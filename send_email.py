import smtplib, ssl
import datetime
from scraper import check_returns as is_returns_open_method


def generate_message_body(is_returns_open):
    if is_returns_open is True:
        body = "Yay, the returns is finally open!"
    else:
        body = "The returns in not yet open. Hang tight!"
    return body


def send_email(password):
    port = 465
    smtp_server = "smtp.gmail.com"
    sender_email = "pythonemaildhiraj@gmail.com"
    receiver_email = "dhirajc963+ikea_update@gmail.com"
    message = f""" \
    Subject: IKEA QUEENS \n
    \n{generate_message_body(is_returns_open_method())} \
    \n
    At {datetime.datetime.now().strftime("%d %B, %Y, %I:%M %p")}
    \n
    - Python program!
    """
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
        print(f'sent an update at {datetime.datetime.now()}')
    