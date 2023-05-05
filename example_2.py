#importing the webdriver library from selenium
from selenium import webdriver
#importing the Options libary from the chrome options
from selenium.webdriver.chrome.options import Options
#the BY keyboard tells specifies what parameter to limit to search to
#E.g. ID, CLASS_NAME, etc.
from selenium.webdriver.common.by import By

#Create a Chrome web driver and setting the options
chrome_options = Options()

#keep the browser window open until the user closes it
chrome_options.add_experimental_option("detach", True)

#instantiating the driver
driver = webdriver.Chrome(options= chrome_options)

#setting the url
url = "https://amazon.com/"
driver.get(url)

#setting the keyword to be entered into the search bar
keyword = "wireless headphones"

#selecting the search box by using its ID
search = driver.find_element(By.ID, 'twotabsearchtextbox')

#using send keys to enter text into the form field using .sendkeys()
search.send_keys(keyword)

#selecting the search button by using its ID
search_button = driver.find_element(By.ID, 'nav-search-submit-button')

#clicking the search button using .click()
search_button.click()

#remove the comment on the following line to close the browser after script completion
#driver.quit()


