from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

driver_path = Service("C:/Users/asus/Downloads/chromedriver_linux64")

driver = webdriver.Chrome(service=driver_path)


# fetch the search input box using xpath
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
# ignore the certificate and SSL errors
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--ignore-ssl-errors')
# maximize the browser window
chrome_options.add_argument("start-maximized")
# define with the driver and open the browser
chrome_driver = webdriver.Chrome(service=driver_path, options=chrome_options)

chrome_driver.get("https://www.smartprix.com/mobiles")

check_box1 = chrome_driver.find_element(by=By.XPATH, value='//*[@id="app"]/main/aside/div/div[5]/div[2]/label[1]/span')
check_box1.click()
time.sleep(1)
check_box2 = chrome_driver.find_element(by=By.XPATH, value='//*[@id="app"]/main/aside/div/div[5]/div[2]/label[2]/span')
check_box2.click()
time.sleep(1)


old_height = chrome_driver.execute_script('return document.body.scrollHeight')
while True:
    load = chrome_driver.find_element(by=By.XPATH, value='//*[@id="app"]/main/div[1]/div[2]/div[3]')
    load.click()
    time.sleep(2)
#
    new_height = chrome_driver.execute_script('return document.body.scrollHeight')
    print(old_height)
    print(new_height)
    if new_height == old_height:
        break
    old_height = new_height
#
html = chrome_driver.page_source
with open('smartprix.html', 'w', encoding='utf-8') as f:
    f.write(html)




