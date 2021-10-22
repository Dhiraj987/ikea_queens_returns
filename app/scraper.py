import time
import random
from bs4 import BeautifulSoup
import requests


""" the function below gets the soup for a provided url using the requests """
def get_soup(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup


""" The function below checks the ikea queens website if it is open for returns """

def check_returns():
    url = 'https://www.ikea.com/us/en/stores/queens/'
    soup = get_soup(url)
    returns_container = soup.find('div',{'id':'a216ae70-1bec-11ec-8acd-b5297c6147dd'}).find('ul')
    text = returns_container.text.lower()
    return_open = False if 'returns' in text else True
    return return_open


def test_check_returns():
    url = 'https://www.ikea.com/us/en/stores/queens/'
    assert requests.get(url).status_code == 200