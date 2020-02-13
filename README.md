# WhatsappAutomatedGreetings
## Welcome to my Whatsapp script to automate greetings 
(more features coming soon)

Steps to get the script working:
1. Install python (3.5+ to be safe)
2. Install selenium for python using **pip install selenium**
3. Download Chrome driver from here: [chromedriver](http://chromedriver.chromium.org/)
4. Change path to where the driver is located: 
`driver = webdriver.Chrome(r'your_path\\chromedriver.exe')`
5. Replace Recipient with name of contact as per your whatsapp account
`driver.find_element_by_xpath("//span[@title='Recipient']").click()`
6. Replace "Good Afternoon" with any greeting you like
`driver.find_element_by_xpath('//div[@class="_3u328 copyable-text selectable-text"][@dir="ltr"][@data-tab="1"]').send_keys("Good Afternoon Man"+Keys.ENTER)`
7. Feel free to change the time to whenever you want the greeting to bbe sent:
`if current_time[0:8]=="13:15:00"`

To run the script automatically in the background, set the script as a Windows Service or a Cron job on Unix systems.
(Steps to do this will be added soon)

---
To fix: 
1. Need to scan QR code on [Whatsapp Web](web.whatsapp.com) everytime a browser instance opens
