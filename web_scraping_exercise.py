import requests
import bs4

res = requests.get('http://quotes.toscrape.com')

soup = bs4.BeautifulSoup(res.text,'lxml')

authors = set()
for name in soup.select('.author'):
    authors.add(name.text)

print(authors)

quotes = []
for quote in soup.select('.text'):
    quotes.append(quote.text)

print(quotes)

for item in soup.select('.tag-item'):
    print(item.text)

url = 'http://quotes.toscrape.com/page/'

page_still_valid = True

authors = set()

page=1

while page_still_valid:

    page_url = url+str(page)

    res = requests.get(page_url)

    if 'No quotes found!' in res.text:
        break
    
    soup = bs4.BeautifulSoup(res.text,'lxml')

    for name in soup.select('.author'):
        authors.add(name.text)

    page = page + 1


print(authors)
