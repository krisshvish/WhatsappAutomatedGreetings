from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
import time 
import datetime

  
driver = webdriver.Chrome(r'C:\\Users\\akshay.kumar\\Desktop\\chrome\\chromedriver.exe') 
  
driver.get("https://web.whatsapp.com/") 
wait = WebDriverWait(driver, 600) 
  
wait.until(EC.presence_of_element_located((By.XPATH, "//span[@title='Me 2' and @dir='auto']"))) 
driver.find_element_by_xpath("//span[@title='Me 2']").click()
wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="_3u328 copyable-text selectable-text"][@dir="ltr"][@data-tab="1"]'))) 

while True:

    current_time= str(datetime.datetime.now().time())
    hour = int(current_time[:2])
    minutes = int(current_time[3:5])
    seconds = int(current_time[6:8])
    message = ""

    if current_time[0:8]=="13:15:00":
        driver.find_element_by_xpath('//div[@class="_3u328 copyable-text selectable-text"][@dir="ltr"][@data-tab="1"]').send_keys("Good Afternoon Man"+Keys.ENTER)
        time.sleep(2)
    elif current_time[0:8]=="17:00:00":
        driver.find_element_by_xpath('//div[@class="_3u328 copyable-text selectable-text"][@dir="ltr"][@data-tab="1"]').send_keys("Good Evening Man"+Keys.ENTER)
        time.sleep(2)
    elif current_time[0:8]=="22:00:00":
        driver.find_element_by_xpath('//div[@class="_3u328 copyable-text selectable-text"][@dir="ltr"][@data-tab="1"]').send_keys("Good Night Man"+Keys.ENTER)
        time.sleep(2)
    elif current_time[0:8]=="10:00:00":
        driver.find_element_by_xpath('//div[@class="_3u328 copyable-text selectable-text"][@dir="ltr"][@data-tab="1"]').send_keys("Good Morning Man"+Keys.ENTER)
        time.sleep(2)

    

driver.close()
