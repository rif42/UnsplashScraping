import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import requests
from bs4 import BeautifulSoup
import os
import lxml

driver = webdriver.Firefox()
url = "https://unsplash.com/s/photos/calm-scenery?orientation=landscape"
driver.get(url)


while True:
    image_count=0
    try:
        # count number of figure tags
        image_count = len(driver.find_elements(By.XPATH, "//figure"))

        # scroll down to the page
        driver.execute_script("window.scrollBy(0, 200);")   
        time.sleep(0.25)

        # if load more button exists, click it
        loadMoreButton = driver.find_elements(By.XPATH, "//button[contains(text(), 'Load more')]")
        
        # If load more button exists, click it
        if loadMoreButton:
            loadMoreButton[0].click()
            print("button clicked")
            time.sleep(1)

        print(image_count)

        # if image_count is over 1000, download everything
        if image_count > 1200:
            soup = BeautifulSoup(driver.page_source, 'lxml')
            images = soup.find_all("figure",itemprop="image")
            count = 0 
            for i in images:
                url = i.find('a',rel="nofollow") 
                if url != None:
                    photo_url = url["href"]
                    photo_bytes =requests.get(photo_url,allow_redirects=True)
                    with open(f'{count}wallpapers.jpg','wb') as photo:
                        photo.write(photo_bytes.content)
                        count +=1
            break
    except Exception as e:
        print ("ERROR",e)
        break

print ("Complete")

