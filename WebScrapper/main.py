from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import time

driver = webdriver.Chrome(r"C:\Python39\Lib\site-packages\selenium\webdriver\chrome\chromedriver.exe")

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
print("Number of elements : ",len(soup.find_all('div',attrs={'class':'s-result-item s-asin sg-col-0-of-12 sg-col-16-of-20 sg-col sg-col-12-of-16'})))
lines = soup.find_all('div',attrs={'class':'s-result-item s-asin sg-col-0-of-12 sg-col-16-of-20 sg-col sg-col-12-of-16'})

with open(r"C:\Users\mgula\Desktop\Py_Prog\WebScrapper\Out\mytxt.txt","w") as f:
    for line in lines:
        f.write(str(line))
        f.write('\n')



# for a in soup.find_all('div',attrs={'class':'s-result-item s-asin sg-col-0-of-12 sg-col-16-of-20 sg-col sg-col-12-of-16'}):
#     if a.find('span',attrs={'class':'a-size-medium a-color-base a-text-normal'}):
#         name = a.find('span',attrs={'class':'a-size-medium a-color-base a-text-normal'}).text
#         price = a.find('span',attrs={'class':'a-price-whole'}).text
#         rating = a.find('span',attrs={'class':'a-icon-alt'}).text
#         print(name, price, rating)
#         products.append(name)
#         prices.append(price)
#         ratings.append(rating)

driver.quit()
# dt = "_".join(str(datetime.now())[:19].split(':'))
# fname = r'C:\Users\mgula\Desktop\Py_Prog\WebScrapper\Out\products_'+dt+'.csv'
# df = pd.DataFrame({'Product Name':products,'Price':prices,'Rating':ratings})
# df.to_csv(fname, index=False, encoding='utf-8')
