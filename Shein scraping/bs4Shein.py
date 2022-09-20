import bs4
import requests;
import pandas as pd
from lxml import etree

url = 'https://eur.shein.com/Women-Tops,-Blouses-Tee-c-1766.html?ici=eur_tab01navbar04menu01&scici=navbar_WomenHomePage~~tab01navbar04menu01~~4_1~~real_1766~~~~0&src_module=topcat&src_tab_page_id=page_real_class1663437350149&src_identifier=fc%3DWomen%60sc%3DCLOTHING%60tc%3DTOPS%60oc%3D0%60ps%3Dtab01navbar04menu01%60jc%3Dreal_1766&srctype=category&userpath=category-CLOTHING-TOPS'
titles=[]
page = requests.get(url)

soup = bs4.BeautifulSoup(page.content,'html.parser')
dom = etree.HTML(str(soup))
print(dom.xpath('//*[@id="product-list-v2"]/div[2]/div[2]/section/div[1]/section[1]/div[2]')[0])
i = 0
for s in soup.findAll('section',class_='S-product-item j-expose__product-item product-list__item'):
    titles.append(s['aria-label'])
    p = s.findAll('div',class_='S-product-item__wrapper')

for p in soup.findAll('div',class_='S-product-item__info'):
    price = p.findAll(attrs={'class': None})

for p in soup.findAll('div',attrs={'class': None}):
    price = p.findAll('section')
