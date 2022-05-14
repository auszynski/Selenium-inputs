import time
from pkg_resources import find_distributions
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get('https://golden-farm.biz/')
time.sleep(1)

emailInput = driver.find_element_by_name('log_email')
time.sleep(1)
emailInput.send_keys('lysech@gmail.com')
passwordInput = driver.find_element_by_name('pass')
passwordInput.send_keys('uszynski13')
loginButton = driver.find_element_by_id('btn_login')
loginButton.click()


# srchbutton = driver.find_element(By.CLASS_NAME,'gNO89b')
# time.sleep(3)
# srchbutton.click()
# time.sleep(2)
# srchbutton1 = driver.find_element(By.CLASS_NAME,'sVXRqc')
# srchbutton1.click()