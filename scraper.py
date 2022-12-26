#this comment is to test initial GitHub commit
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
import pandas as pd
from matplotlib import pyplot as plt

#create empty lists to add book titles and prices to
titles = []
prices = []
#loop through the 50 pages of books, grabbing every book title on each page
for i in range(1, 51):
    url = "http://books.toscrape.com/catalogue/page-"+str(i)+".html"
    page = urlopen(url)
    html = page.read().decode('utf-8')
    soup = bs(html, 'html.parser')
    #find relevant tags on the page
    books = soup.find_all("a")
    #find relevant prices on page
    costs = soup.find_all("p", class_="price_color")
    #loop through the books on the page, passing over irrelevant tag data
    for book in books:
        if "title" in book.attrs:
            titles.append(book.attrs.get('title'))
        else: 
            pass
    for price in costs:
        prices.append(price.text)
#combine titles and prices
#create data frame
df = pd.DataFrame(list(zip(titles, prices)))

#change column names of dataframe
df.rename(columns = {0:"Titles", 1:"Prices"}, inplace = True)

#clean prices and change to float
df.Prices = df.Prices.apply(lambda x: x[1:])
df.Prices = df.Prices.astype(float)

#create a histogram of the prices
xticks = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65]
plt.hist(df.Prices, bins = 10, edgecolor = "black")
plt.title("Distribution of Book Prices")
plt.xlabel("Book Price")
plt.ylabel("Number of Books")
plt.xticks(xticks)
plt.savefig('prices.png')




