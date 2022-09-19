import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import getpass
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
options = Options()

options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.BinaryLocation = "C:/Users/moham_nbdosir/AppData/Local/Google/Chrome SxS/Application/chrome.exe"
# options.add_argument('headless')

url = 'https://eur.shein.com/Women-Tops,-Blouses-Tee-c-1766.html?ici=eur_tab01navbar04menu01&scici=navbar_WomenHomePage~~tab01navbar04menu01~~4_1~~real_1766~~~~0&src_module=topcat&src_tab_page_id=page_real_class1663437350149&src_identifier=fc%3DWomen%60sc%3DCLOTHING%60tc%3DTOPS%60oc%3D0%60ps%3Dtab01navbar04menu01%60jc%3Dreal_1766&srctype=category&userpath=category-CLOTHING-TOPS'
browser_driver = Service(executable_path='C:/Users/moham_nbdosir/AppData/Local/Google/Chrome SxS/chromedriver.exe')
page_to_scrape = webdriver.Chrome(service=browser_driver,options=options)

page_to_scrape.get(url=url)

file  = open("shein.csv","w")
writer = csv.writer(file)

writer.writerow(["NAME",'IMG','PRICE','COLORS'])


closex = page_to_scrape.find_element(By.XPATH, "/html/body/div[1]/div[5]/div[1]/div/i")
page_to_scrape.implicitly_wait(5)
ActionChains(page_to_scrape).move_to_element(closex).click(closex).perform()
html = page_to_scrape.find_element(By.TAG_NAME,'html')
html.send_keys(Keys.END)

names = page_to_scrape.find_elements(By.CLASS_NAME,'S-product-item__link')
imgs = page_to_scrape.find_elements(By.CLASS_NAME,'S-product-item__img-submain')
prices = page_to_scrape.find_elements(By.CLASS_NAME,'S-product-item__retail-price')
colors = page_to_scrape.find_elements(By.CLASS_NAME,'S-product-item__relatecolor-inner falcon-lazyload')
# imgs = page_to_scrape.find_element_by_xpath("//img[contains(@class,'S-product-item__img-submain')]")
# for name, img in zip(names,imgs):
# 	print(name.text + "-" + img.text)
# 	writer.writerow([img.text,img.text])
for name,img,price,color in zip(names,imgs,prices,colors):
	for singleColor in color:
		print(singleColor)
		writer.writerow([singleColor.get_attribute('data-background-image')])
	writer.writerow([name.text,img.get_attribute('data-src'),price.text,color.get_attribute('data-background-image')])
file.close()