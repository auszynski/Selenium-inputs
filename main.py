import time
from pkg_resources import find_distributions
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get('https://www.google.pl/')
time.sleep(2)

search1 = driver.find_element_by_class_name('gLFyf.gsfi')
time.sleep(2)
search1.send_keys('kryptowaluty')

srchbutton = driver.find_element(By.CLASS_NAME,'gNO89b')
time.sleep(3)
srchbutton.click()
time.sleep(2)
srchbutton1 = driver.find_element(By.CLASS_NAME,'sVXRqc')
srchbutton1.click()