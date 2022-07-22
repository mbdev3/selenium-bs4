from  bs4 import BeautifulSoup
import requests

text = requests.get('https://eur.shein.com/Women-T-Shirts-c-1738.html?ici=eur_tab01navbar04menu01dir01&scici=navbar_WomenHomePage~~tab01navbar04menu01dir01~~4_1_1~~real_1738~~~~0&src_module=topcat&src_tab_page_id=page_home1656085819680&src_identifier=fc%3DWomen%60sc%3DCLOTHING%60tc%3DTOPS%60oc%3DT-Shirts%60ps%3Dtab01navbar04menu01dir01%60jc%3Dreal_1738&srctype=category&userpath=category-CLOTHING-TOPS-T-Shirts').text
soup = BeautifulSoup(text,'lxml')

articles = soup.find_all(class_='S-product-item__name')
 

# span = articles.find_all('div')
for article in articles:
    # img = article.find("div", class_='S-product-item__wrapper').img.attrs['data-src']
    # info = article.find("div", class_='S-product-item__info').section
    print(article)
#     print(f'''img: {img}
#     info: {info}
#     ''')
# print(articles)

