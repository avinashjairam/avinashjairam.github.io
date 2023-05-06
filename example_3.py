#importing the webdriver library from selenium
from selenium import webdriver
#importing the Options libary from the chrome options
from selenium.webdriver.chrome.options import Options
#the BY keyboard tells specifies what parameter to limit to search to
#E.g. ID, CLASS_NAME, etc.
from selenium.webdriver.common.by import By

#importing the webdriver library from selenium
from selenium import webdriver
#importing the Options libary from the chrome options
from selenium.webdriver.chrome.options import Options
#the BY keyboard tells specifies what parameter to limit to search to
#E.g. ID, CLASS_NAME, etc.
from selenium.webdriver.common.by import By

#wait and EC allows the program to wait while the webpage loads
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

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
keywords = ["wireless headphones", "usb drive", "usb-c charger"]

#lists to store data
asin_list = []
product_name_list = []
product_price_list = []
product_ratings_list = []
product_ratings_num_list = []
link_list = []

for keyword in keywords:
    #selecting the search box by using its ID
    search = driver.find_element(By.ID, 'twotabsearchtextbox')

    #using send keys to enter text into the form field using .sendkeys()
    search.send_keys(keyword)

    #selecting the search button by using its ID
    search_button = driver.find_element(By.ID, 'nav-search-submit-button')

    #clicking the search button using .click()
    search_button.click()

    #waiting 5 seconds for the page to load
    driver.implicitly_wait(5)

    #collecting a list of the all divs which contain the search results
    scraped_items = wait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//div[contains(@class, "s-result-item s-asin")]')))



    #iterating through the list of divs to find specifics of each item in the search result
    for item in scraped_items:

        # find ASIN number
        asin = item.get_attribute("data-asin")

        # find name
        product_name = item.find_element(By.XPATH, './/span[@class="a-size-medium a-color-base a-text-normal"]')


        # find price
        whole_price_list = item.find_elements(By.XPATH, './/span[@class="a-price-whole"]')
        fraction_price_list = item.find_elements(By.XPATH, './/span[@class="a-price-fraction"]')

        if whole_price_list != [] and fraction_price_list != []:
            product_price = '.'.join([whole_price_list[0].text, fraction_price_list[0].text])
        else:
            product_price = 0

            # find ratings box
        ratings_box_list = item.find_elements(By.XPATH, './/div[@class="a-row a-size-small"]/span')

        # find ratings and ratings_num
        if ratings_box_list != []:
            product_ratings = ratings_box_list[0].get_attribute('aria-label')
            product_ratings_num = ratings_box_list[1].get_attribute('aria-label')
        else:
            product_ratings, product_ratings_num = 0, 0

        # append scraped information to respective lists
        link = item.find_element(By.XPATH, './/a[@class="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"]').get_attribute("href")

        asin_list.append(asin)
        product_name_list.append(product_name.text)
        product_price_list.append(product_price)
        product_ratings_list.append(product_ratings)
        product_ratings_num_list.append(product_ratings_num)
        link_list.append(link)

        print(product_name.text)
        print(product_price)
        print(product_ratings)
        print(product_ratings_num)
        print(link)
        print('\n')

    #clearing the search field
    driver.find_element(By.ID, 'twotabsearchtextbox').clear()

    #wait 5 seconds to search again 
    time.sleep(5)
    
    # waiting 5 seconds for the page to load
    driver.implicitly_wait(5)

    #remove the comment on the following line to close the browser after script completion
    #driver.quit()

#creating a dictionary to store the data
df = pd.DataFrame({
                    'Asin': asin_list,
                    'Product Name': product_name_list,
                    'Product Rating': product_ratings_list,
                    'Num Ratings': product_ratings_num_list,
                    'Link': link_list
})

#printing the contents of the dataframe
print(df)

#exporting the data to csv file
df.to_csv('products.csv', index=False)
