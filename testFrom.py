# link selenium and time 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

# link the chromedriver service 
PATH = "D:/python/python/seleuium/chromedriver.exe"
service = Service(PATH)
driver = webdriver.Chrome(service=service)

# get your link
driver.get('https://docs.google.com/forms/d/e/1FAIpQLSeF67tBAGKyXATahdnxZY9NdLXUpWx7co5LnNPil-OufNE54A/viewform')

# define your function
def testFrom():
    for numbers in range(31,67):
        # least one second
        wait = WebDriverWait(driver, 1)
        time.sleep(1)
        # input numbers
        email = driver.find_element(By.CSS_SELECTOR, 'input[type="text"]')
        email.send_keys(f"{numbers}")
        # get all labels
        labels = driver.find_elements(By.CSS_SELECTOR, '[data-ratingscale="10"]')
        for idx, element in enumerate(labels):
            print(f"Element {idx + 1}: {element.tag_name}, {element.get_attribute('outerHTML')}")
        for element in labels:
            element.click()
        # get button
        button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[aria-label="Submit"]')))
        button.click()
        # get link
        link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT,"提交其他回應")))
        link.click()
        
# start function
testFrom()

# close your chrome
driver.close()