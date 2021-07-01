from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import time

driver = webdriver.Chrome(r"C:\Python38\Lib\site-packages\selenium\driver\chromedriver_84.exe")

products=[] #List to store name of the product
prices=[] #List to store price of the product
ratings=[] #List to store rating of the product
page = "https://www.amazon.com/s?k=professional+gaming+laptops&ref=nb_sb_noss"
driver.get(page)

content = driver.page_source
driver.implicitly_wait(100)
# print(content)
soup = BeautifulSoup(content, 'html.parser')
# print(soup)

for a in soup.elements():
    name = a.find('span',attrs={'class':'a-size-medium a-color-base a-text-normal'})
    price = a.find('span',attrs={'class':'a-price-whole'})
    rating = a.find('span',attrs={'class':'a-icon-alt'})
    products.append(name.text)
    prices.append(price.text)
    ratings.append(rating.text)

driver.quit()
dt = "_".join(str(datetime.now())[:19].split(':'))
fname = r'C:\Users\mgula\Desktop\Py_Prog\WebScrapper\Out\products_'+dt+'.csv'
df = pd.DataFrame({'Product Name':products,'Price':prices,'Rating':ratings})
df.to_csv(fname, index=False, encoding='utf-8')
