"""Recently twitter has stopped giving thier Apis for everyone so i write simple python script using selenium to scrap 
all the tweets from a user and store into a csv file """
#Please read instruction file to get link of a user



from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
import csv

#opneing taget page with firefox
driver = webdriver.Firefox()
driver.set_page_load_timeout(100)
#paste userprofile link into the single qoutes
url = 'https://twitter.com/search?q=from%3AXbox%20%20since%3A2015-09-20%20until%3A2016-11-28&src=typd&lang=en'
driver.get(url)
sleep(10)


#scrolling down to find posts
driver.find_element_by_css_selector(".u-size2of3").click()
i = 0
lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
match = False
while(match == False):
    lastCount = lenOfPage
    sleep(3)
    lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    if lastCount == lenOfPage:
        match = True


#function for writing tweets to csv
def append_data(file_path, name,):
    fieldnames = ['paragraph']
    
    with open(file_path, "a") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        #writer.writeheader()
        writer.writerow({
            "paragraph": name,
            
        })


#scraping tweets
links = []
main1 = driver.find_element_by_css_selector("#timeline>div>div.stream")
articles = main1.find_elements_by_tag_name("li")
for alphas in articles:
    try:
        a = alphas.find_element_by_tag_name("p").text
        #print a remove # for printing tweets on terminal
        links.append(a)
        append_data("data.csv", a,)
    except:
        pass
    

#total number of tweets scraped    
#print len(articles)









#regards Zeeshan Ahmad 
