from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv

START_URL = 'https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'
browser = webdriver.Chrome('/path/to/chromedriver')
browser.get(START_URL)
time.sleep(10)
soup = BeautifulSoup(browser.page_source, "html.parser")
for ul_tag in soup.find_all("ul", attrs={"class", "exoplanet"}):
    li_tags = ul_tag.find_all("li")

def scrape():p