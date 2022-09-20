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
page = webdriver.Chrome(service=browser_driver,options=options)

page.get(url=url)

file  = open("shein.csv","w")
writer = csv.writer(file)

titles = []
title_path = '/html/body/div[1]/div[1]/div[2]/div[2]/section/div[1]/section[1]/div[2]/div[1]/a'



