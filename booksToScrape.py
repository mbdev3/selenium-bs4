import bs4
import requests;
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

pages = []
prices = []
ratings = []
titles = []
urls = []

no_of_pages = 1
# print("Encoding method :",soup.original_encoding)
for i in range(1, no_of_pages + 1):
    url = ('http://books.toscrape.com/catalogue/page-{}.html'.format(i))
    pages.append(url)
for item in pages:
    page = requests.get(item)
    soup = bs4.BeautifulSoup(page.text, 'html.parser')

for t in soup.findAll('h3'):
    title = t.getText()
    titles.append(title)
# print(titles)
soup.p.encode("utf-8")
for p in soup.findAll('p', class_='price_color'):
    price = p.getText()
    prices.append(price)
# print(prices)

for s in soup.findAll('p', class_='star-rating'):
    for k, v in s.attrs.items():
        star = v[1]
        ratings.append(star)
divs = soup.findAll('div', class_='image_container')
# print(divs)
for thumbs in divs:
    tags = thumbs.find('img', class_='thumbnail')
    # print(tags)
    links = 'http://books.toscrape.com' + str(tags['src']).replace('..', '')
    # print(links)
    urls.append(links)

webData = {'title': titles, 'price': prices, 'rating': ratings}
df = pd.DataFrame(webData)
df.index += 1
df['price'] = df['price'].str.replace('Â£', '')
df['price'] = df['price'].astype(float)


df['rating'] = df['rating'].replace({'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5})
df.sort_values(by='price', ascending=False,inplace=True)
print(df)
print(df.dtypes)
print(df.corr(numeric_only=True))


plt.figure(figsize=(5,5))
sns.heatmap(df.corr(numeric_only=True))
plt.show()