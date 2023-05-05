#importing libraries
from selenium import webdriver
import time
#Create a Chrome web driver
driver = webdriver.Chrome()

#setting the url
url = "https://amazon.com/"
driver.get(url)

#keep the browser window open for 10 seconds
time.sleep(10)

#close the browser
driver.quit()