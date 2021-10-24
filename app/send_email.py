import os
import datetime
import smtplib, ssl
from dotenv import load_dotenv
from scraper import check_returns as is_returns_open_function


""" to read the .env file from top directory """
APP_ROOT = os.path.join(os.path.dirname(__file__), '..')   # refers to the project directory
dotenv_path = os.path.join(APP_ROOT, '.env')
load_dotenv(dotenv_path)


""" the function below takes in true/false and generates a body text for the email """
def generate_message_body(is_returns_open):
    if is_returns_open is True:
        body = "Yay, the returns is finally open!"
    else:
        body = "The returns in not yet open. Hang tight!"
    return body


""" 
-- the function below takes in the password and send an email
-- it also calls the check_returns function (located in the scraper file) where
    the status of if the store's returns department is open is updated
"""
def send_email():
    port = 465
    smtp_server = "smtp.gmail.com"
    sender_email = os.getenv('sender_email')
    password = os.getenv('password')
    receiver_email = "dhirajc963+ikea_update@gmail.com"
    message = f""" \
    Subject: IKEA QUEENS \n
    \n{generate_message_body(is_returns_open_function())} \
    \n
    At {datetime.datetime.now().strftime("%d %B, %Y, %I:%M %p")}
    \n
    - Python program!
    """
    print(sender_email, password)
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
        print(f'sent an update at {datetime.datetime.now()}')
