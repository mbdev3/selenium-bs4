import csv

from selenium import webdriver
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.chrome.options import Options


options = Options()

options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.BinaryLocation = "C:/Users/moham_nbdosir/AppData/Local/Google/Chrome SxS/Application/chrome.exe"
from selenium.webdriver.common.by import By
import time
import getpass
from selenium.common.exceptions import NoSuchElementException
browser_driver = Service(executable_path='C:/Users/moham_nbdosir/AppData/Local/Google/Chrome SxS/chromedriver.exe')
page_to_scrape = webdriver.Chrome(service=browser_driver,chrome_options=options)

page_to_scrape.get(url='http://quotes.toscrape.com')

page_to_scrape.find_element(By.LINK_TEXT, "Login").click()

time.sleep(3)

username = page_to_scrape.find_element(By.ID,"username")
password = page_to_scrape.find_element(By.ID,"password")
username.send_keys('admin')

my_pass = getpass.getpass()
password.send_keys(my_pass)

page_to_scrape.find_element(By.CSS_SELECTOR,'input.btn-primary').click()


file  = open("seleniumfile.csv","w")
writer = csv.writer(file)

writer.writerow(['QUOTES','AUTHORS'])
while True:
    quotes = page_to_scrape.find_elements(By.CLASS_NAME,'text')
    authors = page_to_scrape.find_elements(By.CLASS_NAME,'author')

    for quote, author in zip(quotes,authors):
        print(quote.text + "-" + author.text)
        writer.writerow([quote.text,author.text])
    try:
        page_to_scrape.find_element(By.PARTIAL_LINK_TEXT, "Next").click()
    except NoSuchElementException:
        break
file.close()