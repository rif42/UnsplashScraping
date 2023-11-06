# Installation
- pip install selenium
- pip install beautifulsoup4

# Description
This is a simple image scraping script to download high quality full resolution images (not thumbnail) from unsplash.com using selenium and beautifulsoup.  

Selenium will drive the browser, opening the url, and scrolling downwards while counting the total images shown in the page.  
Once image reaches a certain threshold (default is 1200), the script will call beautifulsoup4 to download all the image contained in the figure tag.  
The browser will still be open while downloading the images, please don't close them.  

Made by : Rifky Ariya Pratama