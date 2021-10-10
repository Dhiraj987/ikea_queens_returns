from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
CHROME_DRIVER = './chromedriver'


""" the function below sets up the webdriver that it uses to parse the soup """
def setup_driver(headless=True) -> webdriver:
    options = ChromeOptions()
    driver_type=CHROME_DRIVER
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    if headless:
        options.add_argument('-headless')
    driver = webdriver.Chrome(executable_path=driver_type, chrome_options=options)
    return driver


""" the function below gets the soup for a provided url """
def get_soup(url):
    driver = setup_driver()
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    driver.quit()
    return soup


""" The function below checks the ikea queens website if it is open for returns """
def check_returns():
    url = 'https://www.ikea.com/us/en/stores/queens/'
    soup = get_soup(url)
    returns_container = soup.find('div',{'id':'a216ae70-1bec-11ec-8acd-b5297c6147dd'}).find('ul')
    text = returns_container.text.lower()
    return_open = False if 'returns' in text else True
    return return_open
