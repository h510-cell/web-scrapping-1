import csv
from bs4 import BeautifulSoup
from selenium import webdriver
import time

START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser = ("/Users/apoorvelous/Downloads/chromedriver")
browser.get(START_URL)
time.sleep(10)

def scrape():
    headers = ["Name","Distance","Radius","Mass"]
    stars_data = []
    for i in range(0,428):
        soup = BeautifulSoup(browser.page_source,"html.parser")
        for ul_tag in soup.find_all("ul",attrs ={"class","List_of_brightest_stars_and_other_record_stars"}):
            li_tags = ul_tag.find_all("li")
            stars_list =[]
            for index,li_tags in enumerate(li_tags):
                if index == 0:
                    stars_list.append(li_tags.find_all("a")[0].contents[0])
                else:
                    try:
                        stars_list.append(li_tags.contents[0])
                    except:
                        stars_list.append("")
            stars_data.append(stars_list)
        browser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
scrape()

df.to_csv('hemaagam.csv')
with open('hemaagam.csv','w') as f:
    csvwriter = csv.writer(f)
    csvwriter = writerow(headers)
    csvwriter = writerows(stars_data)