# Please, install the following libraries before
# pip install requests
# pip install lxml
# pip install bs4

import requests
import bs4
import lxml

result = requests.get('http://www.example.com/')

# print(type(result))
soup = bs4.BeautifulSoup(result.text,'lxml')
# print(result.text)
# print(soup)
print(soup.select('title')[0].getText())
print(soup.select('p'))
print(soup.select('h1'))

res = requests.get('https://en.wikipedia.org/wiki/Grace_Hopper')

soup = bs4.BeautifulSoup(res.text,"lxml")

for item in soup.select('.toctext'):
    print(item.text)

# Taking an image

res2 = requests.get('https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)')
soup = bs4.BeautifulSoup(res2.text,"lxml")
computer = soup.select('.thumbimage')[0]
image_link = requests.get('https:' + computer['src'])

f = open('my_computer_image.jpg','wb')
f.write(image_link.content)
f.close()





