# import time
# from pkg_resources import find_distributions
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# driver = webdriver.Chrome()
# driver.get('https://www.google.pl/')
# time.sleep(2)
# agreeButton = driver.find_element_by_id('L2AGLb')
# time.sleep(1)
# agreeButton.click()
# time.sleep(1)
# search1 = driver.find_element_by_class_name('gLFyf.gsfi')
# time.sleep(2)
# search1.send_keys('kryptowaluty')

# srchbutton = driver.find_element(By.CLASS_NAME,'gNO89b')
# time.sleep(3)
# srchbutton.click()
# time.sleep(2)
# link1 = driver.find_element_by_partial_link_text('kryptowaluty')
# time.sleep(2)
# link1.click()

##########

import undetected_chromedriver as uc
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time


options = Options()

options.add_argument(r"--user-data-dir=/Users/Artur/Library/Application Support/Google/Chrome/Profile 2") #Profile path
options.add_argument(r'--profile-directory=Profile 5')

cryptoKeywords = ["Crypto", "Kryptowaluty", "Giedła", "NFT", "Blockchain", "bitcoin", "token", "exchange", "wallet"]
driver = uc.Chrome(use_subprocess=True, options=options)

def initChrome():
    print('Init chrome')



def openGoogleSearch():
    driver.get('https://www.google.pl/')
    time.sleep(1)
    
def runQuery(keyword):
    search1 = driver.find_element_by_name('q')
    time.sleep(1)
    search1.send_keys(keyword)

    srchbutton = driver.find_element(By.CLASS_NAME,'gNO89b')
    time.sleep(1)
    srchbutton.click()
    time.sleep(1)

    

def openAndClickByText(iteration, text):
    print("OPEN AND CLICK", iteration)
    links = driver.find_elements_by_partial_link_text(text)
    
    if len(links) >= iteration:
        try:
           links[iteration].click()
        except:
            print("CATCH ERROR")
            pass
        
    
    time.sleep(3)
    driver.back()
    
def loopByLinks(numberOfCall, text):
    iteration = 0
    for i in range(numberOfCall):
        openAndClickByText(iteration, text)
        iteration = iteration + 1
        time.sleep(3)

        
print('START')
initChrome()

for i in cryptoKeywords:
    print("SEARCH BY", i)
    openGoogleSearch()
    runQuery(i)
    loopByLinks(4, i)
    