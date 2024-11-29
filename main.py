from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

PATH = "D:/python/python/seleuium/chromedriver.exe"
service = Service(PATH)
driver = webdriver.Chrome(service=service)

driver.get("https://docs.google.com/forms/d/e/1FAIpQLSe2sEszu74T0qo0JbNE_lk2dKmvFqWi1ARoc5jiDo1wfrfdQA/viewform")

wait = WebDriverWait(driver, 10)
# login = driver.find_element(By.CSS_SELECTOR, '[jscontroller="A2m8uc"]').click()
# email = driver.find_element(By.CSS_SELECTOR, '[jsname="YPqjbf"]').send_keys("chengyouli37@gmail.com")

# email.send_keys(Keys.ENTER)

selector = wait.until(EC.element_to_be_clickable((By.ID, 'i9')))
selector.click()
email = driver.find_element(By.CSS_SELECTOR, 'input[type="text"]')
email.send_keys("chengyouli37@gmail.com")
list = driver.find_element(By.CSS_SELECTOR, '[role="listbox"]')
list.click()
time.sleep(2)
options=[]
college = "是"
for selections in (driver.find_elements(By.XPATH,"//span[contains(@class,'vRMGwf oJeWuf')]")):
    if college in selections.text:
        selections.click()
time.sleep(2)
button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[aria-label="Submit"]')))
button.click()
# yes = driver.find_element(By.XPATH, '//div[@jsname="wQNmvb"]')
# yes.click()

# yes = driver.find_element(By.CSS_SELECTOR, '[aria-selected="true"]')
# yes.click()
# button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[aria-label="Submit"]')))
# button.click()
# button_value = button.get_attribute("role")

# print(f"{button_value}")
# selector_id = selector.get_attribute('id')

# print(f"{selector_id}")

time.sleep(10)

