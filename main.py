import time
#from unittest import result
#from urllib import request, response
#from pkg_resources import find_distributions
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
########
#from urllib.request import Request, urlopen #wazne
#from bs4 import BeautifulSoup #wazne
#import requests #wazne

#root = 'https://www.google.pl/'
#link = 'https://www.google.pl/search?q=kryptowaluty&source=hp&ei=Xr5_YpOTFpGOxc8PtbW2gAQ&iflsig=AJiK0e8AAAAAYn_Mbl2vsHZlhayGeNmZBK-UHBj1R_HP&oq=krypto&gs_lcp=Cgdnd3Mtd2l6EAMYADILCAAQgAQQsQMQgwEyCwgAEIAEELEDEIMBMggIABCxAxCDATILCAAQgAQQsQMQgwEyCAgAEIAEELEDMggIABCxAxCDATILCAAQgAQQsQMQgwEyBAgAEAMyFAguEIAEELEDEIMBEMcBENEDENQCMgUIABCABDoFCC4QgAQ6CAguELEDEIMBOggILhCABBCxAzoLCC4QgAQQsQMQgwE6CAguEIAEENQCOgsILhCABBCxAxDUAlD4kApYzJ8KYMGqCmgCcAB4AIABcIgBrASSAQM1LjGYAQCgAQGwAQA&sclient=gws-wiz'
#req = Request(link, headers={'User-Agent': 'Google Chrome'})
#webpage = urlopen(req).read()
#with request.Session() as c:
#    soup = BeautifulSoup(webpage, 'html5lib')
#    print(soup)
 #   for item in soup.find_all('div', attrs={'class':'g.tF2Cxc'}):
 #       print(item)

driver = webdriver.Chrome()
driver.get('https://www.google.pl/')
time.sleep(2)

#cryptokeywords=["Crypto","Kryptowaluty","Giełda","NFT","Blockchain","bitcoin","exchange","wallet"]

#gameskeywords=["Android gry","Gry na androida","King od avalon","coin master","match masters","Idle Miner","Idle games","gry idle"]

#appskeywords= ["pracuj.pl","aplikacja do szukania pracy","praca zdalna","alibaba","shopee"]

#for i in cryptokeywords:
#    result= driver.get_log(i)
#    driver.save_screenshot(result)



search1 = driver.find_element_by_class_name('gLFyf.gsfi')
time.sleep(2)
search1.send_keys('kryptowaluty')
button = driver.find_element_by_class_name('gNO89b')
button.click()