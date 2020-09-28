from splinter import Browser
from bs4 import BeautifulSoup as bs
import pandas as pd
import requests

def init_browser():
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)


def scrape():
    browser = init_browser()
    ###NASA Mars News###
    # Bring in the website to be scraped
    url = 'https://mars.nasa.gov/news'
    browser.visit(url)
    mars = {}

    #Iterate through x number of pages:
    for x in range(2):
        
        html=browser.html
        
        soup=bs(html, 'html.parser')
        articles = soup.find_all('li', class_='slide')
        
        #Iterate through each news article
        for article in articles:
            news_title = article.find('div', class_='content_title').text
            news_p = article.find('div', class_='article_teaser_body').text
            mars["News Title"] = news_title
            mars["News Text"] = news_p

        # Click the 'More' button on each page
        try:
            browser.click_link_by_partial_text('More')
            
        except:
            print("Scraping Complete")

    return mars

    # ###JPL Mars Space Images - Featured Image###
    # #  Bring in the website to be scraped
    # url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    # browser.visit(url)

    # ##Get featured image from url
    # html = browser.html
    # soup = bs(html, 'html.parser')

    # result = soup.find('div', class_='fancybox-inner')

    # featured_image_url = f"https://www.jpl.nasa.gov{result.img['src']}"
    # featured_image_url

    # ###Mars Facts###
    # url = 'https://space-facts.com/mars/'
    # tables = pd.read_html(url)
    

    # ##Save Mars information to dataframe and set the index to the info fields
    # df = tables[0]

    # df.set_index(0, inplace=True)
    

    # #transpose the dataframe 
    # df = df.transpose()
   

    # ##create and HTML table string
    # html_table = df.to_html()
    

    # ###Mars Hemispheres###
    # #Bring in the website to be scraped
    # url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    # browser.visit(url)

    # ##Get hemisphere search results
    # html = browser.html
    # soup = bs(html, 'html.parser')

    # results = soup.find_all('div', class_='item')
    # title = []
    # img_url = []

    # ##iterate through the hemisphere pages by visiting each page to get title and image url
    # for result in results:
        
    #     link = "https://astrogeology.usgs.gov" + result.find('a', class_='itemLink product-item')['href']
    #     browser.visit(link)
    #     html = browser.html
    #     soup = bs(html,'html.parser')
    #     page_result = soup.find('div', class_='content')
        
    #     title.append(page_result.find('h2', class_='title').text)
    #     img_url.append(page_result.find('a')['href'])

    


    # print(title, img_url)

    # #Save hemisphere info to a dataframe
    # hemisphere_image_urls = pd.DataFrame({
    #     "title": title,
    #     "img_url": img_url
    # })
        
    