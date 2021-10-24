import time
from send_email import send_email


""" 
-- the app_loop function takes in the password inputand sends it to 
send_email function in the other file
-- it repeats the same every two hours
"""
def app_loop():
    while True:
        send_email()
        time.sleep(7200)


""" when this file is called the app_loop method is executed """
if __name__ == '__main__':
    app_loop()
    