import csv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class crawledArticle():
    def __init__(self, title, price):
        self.title = title
        self.price = price


class Bot:

    def article(self, name):
        count = 1
        page = 1
        pageIncrement = 10
        maxRetrieves = 30
        file = open("result.csv", "w")
        writer = csv.writer(file)

        writer.writerow(["title", 'price'])
        url = 'https://www.amazon.com/s?k=' + name + '&page=' + str(page)
        result = []
        options = Options()
        options.headless = False
        options.add_experimental_option('detach', True)

        browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        browser.maximize_window()
        browser.get(url)
        browser.set_page_load_timeout(10)

        while True:
            try:
                if pageIncrement * page > maxRetrieves:
                    break

                if count > pageIncrement:
                    count = 1
                    page += 1

                xPathTitle = '/html/body/div[1]/div[2]/div[1]/div[1]/div/span[3]/div[2]/div['+str(count)+']/div/div/div/div/div/div[2]/div/div/div[1]/h2/a/span'
                title = browser.find_element(By.XPATH,xPathTitle)
                xPathLink = '//*[@id="search"]/div[1]/div[1]/div/span[3]/div[2]/div['+str(count)+']/div/div/div/div/div/div[2]/div/div/div[1]/h2/a'
                link = browser.find_element(By.XPATH,xPathLink)
                titleText = title.get_attribute("innerHTML")
                link.click()

                xPathPrice = '/html/body/div[1]/div[2]/div[10]/div[6]/div[1]/div[4]/div/div/div/form/div/div/div/div/div[2]/div[1]/div/span/span[1]'
                price = browser.find_element(By.XPATH,xPathPrice)
                priceText = price.get_attribute("innerHTML")

                url = 'https://www.amazon.com/s?k=' + name + '&page=' + str(page)

                browser.get(url)
                browser.set_page_load_timeout(10)

                info = crawledArticle(titleText, priceText)
                result.append(info)
                count += 1
                writer.writerow([titleText,priceText])

            except Exception as e:
                print('Exception', e)
                count += 1

                if pageIncrement * page > maxRetrieves:
                    break

                if count > pageIncrement:
                    count = 1
                    page += 1

                url = 'https://www.amazon.com/s?k=' + name + '&page=' + str(page)

                browser.get(url)
                browser.set_page_load_timeout(10)
        browser.close()
        return result


fetcher = Bot()
fetcher.article('iPhone 13')
# with open('results.csv', 'w', newline='', encoding='utf-8') as csvfile:
#     articleWriter = csv.writer(csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#     for article in fetcher.article('iPhone 13'):
#         articleWriter.writerow([article.title, article.price])
