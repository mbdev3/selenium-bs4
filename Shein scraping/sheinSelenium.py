from selenium import webdriver
from lxml import html
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd
import numpy as np
driver = webdriver.Chrome(ChromeDriverManager().install())
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

titles=[]
mainImages = []
secondaryImages = []
prices=[]
salePrices = []
retailPrices = []
colors=[]
labels = []
for page in  range(1,2):
    driver.get('https://eur.shein.com/Women-Tops,-Blouses-Tee-c-1766.html')
    closex = driver.find_element(By.XPATH, "/html/body/div[1]/div[5]/div[1]/div/i")
    driver.implicitly_wait(5)
    ActionChains(driver).move_to_element(closex).click(closex).perform()
    htmlpage = driver.find_element(By.TAG_NAME, 'html')
    htmlpage.send_keys(Keys.END)
    sleep(5)

    tree = html.fromstring(driver.page_source)

    for product_tree in tree.xpath('//section[@class="S-product-item j-expose__product-item product-list__item"]'):
        title = product_tree.xpath('.//a[@class="S-product-item__link S-product-item__link_jump"]/text()')
        price = product_tree.xpath('.//span[@class="S-product-item__retail-price"]/text()')
        mainImage = product_tree.xpath('.//img[@class="falcon-lazyload"]/@data-src')
        secondaryImage = product_tree.xpath('.//img[@class="S-product-item__img-submain image-fade-out"]/@data-src')
        color = product_tree.xpath('.//div[@class="S-product-item__relatecolor-inner falcon-lazyload"]/@data-background-image')
        label = product_tree.xpath('.//label[@class="S-label kceoyn S-label__sellpoint"]')
        salePrice = product_tree.xpath('.//span[@class="S-product-item__sale-price"]')
        retailPrice = product_tree.xpath('.//span[@class="S-product-item__retail-price S-product-item__retail-price_line"]')
        # colors = product_tree.find_element(By.xpath('//*[@id="search"]/div[1]/div[1]/div/span[3]/div[2]/div[2]/div/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/div[6]/div/div[1]/div/a/span')).getCssValue("background-color")
        # if len(title) == 0:
        #     title.append('empty')
        # else:
        #     titles.append(title)
        # if len(review) == 0:
        #     reviews.append('empty')
        #
        # else:
        #     reviews.append(review)
        titles.append(title)
        mainImages.append(mainImage)
        secondaryImages.append(secondaryImage)
        prices.append(price)
        salePrices.append(salePrice)
        retailPrices.append(retailPrice)
        colors.append(color)
        labels.append(label)
driver.close()

data = {'title':titles,'mainImage':mainImages,'secondaryImage':secondaryImages,'prices':prices,
        'salePrices':salePrices,'retailPrices':retailPrices,'colors':color,'labels':labels}
# print(titles)
df = pd.DataFrame({'TITLE':titles})
# print(df)

# d = dict(TITLE=np.array(titles), REVIEW=np.array(reviews))

# df = pd.DataFrame(dict([(k, pd.Series(v)) for k, v in d.items()]))
# df['TITLE'] = df['TITLE'].apply(''.join)
# df['REVIEW'] = df['REVIEW'].apply(''.join)
df.to_csv('out.csv')