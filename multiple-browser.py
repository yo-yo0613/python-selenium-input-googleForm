# link selenium module for testing mutiple browsers
# link time module
# link firefox and chrome and edge drivers
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.chrome.service import Service as ChromeService
import time

# link firefox and chrome and edge services
EDGE_PATH = "D:/python/python/seleuium/broswers/msedgedriver.exe"
FIREFOX_PATH = "D:/python/python/seleuium/broswers/geckodriver.exe"
CHROME_PATH = "D:/python/python/seleuium/broswers/chromedriver.exe"

# define the firefox function
def test_firefox():
    service = FirefoxService()
    driver = webdriver.Firefox(service=service)
    driver.get("https://www.google.com")
    time.sleep(5)
    driver.quit()

# define the edge function
def test_edge():
    service = EdgeService(EDGE_PATH)
    driver = webdriver.Edge(service=service)
    driver.get("https://www.google.com")
    time.sleep(5)
    driver.quit()

# define the chrome function
def test_chrome():
    service = ChromeService(CHROME_PATH)
    driver = webdriver.Chrome(service=service)
    driver.get("https://www.google.com")
    time.sleep(5)
    driver.quit()

# call the functions to test multiple browsers
test_chrome()  
test_edge()
test_firefox()    