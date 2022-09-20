from selenium import webdriver
from lxml import html
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd
import numpy as np
driver = webdriver.Chrome(ChromeDriverManager().install())

titles=[]
reviews=[]
prices=[]
colors=[]
for page in  range(1,3):
    driver.get('https://www.amazon.com/s?k=iphone+13&page={}'.format(page))
    sleep(5)

    tree = html.fromstring(driver.page_source)

    for product_tree in tree.xpath('//div[contains(@class, "s-card-container")]'):
        title = product_tree.xpath('.//span[@class="a-size-medium a-color-base a-text-normal"]/text()')
        review = product_tree.xpath('.//span[@class="a-size-base s-underline-text"]/text()')
        price = product_tree.xpath('.//span[@class="a-offscreen"]/text()')
        color = product_tree.xpath('.//span[@class="s-color-swatch-inner-circle-fill"]/@style')
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
        reviews.append(review)
        prices.append(price)
        colors.append(color)
driver.close()

data = {'TITLE':titles,'REVIEW':reviews,'PRICE':price,'COLORS':color}
# print(titles)
df = pd.DataFrame({'TITLE':titles,'REVIEW':reviews})
# print(df)

# d = dict(TITLE=np.array(titles), REVIEW=np.array(reviews))

# df = pd.DataFrame(dict([(k, pd.Series(v)) for k, v in d.items()]))
# df['TITLE'] = df['TITLE'].apply(''.join)
# df['REVIEW'] = df['REVIEW'].apply(''.join)
df.to_csv('out.csv')