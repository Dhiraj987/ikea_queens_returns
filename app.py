import time
from send_email import send_email


def app_loop():
    while True:
        send_email(password)
        time.sleep(120)

if __name__ == '__main__':
    password = input("Type your password and press enter: ")
    app_loop()