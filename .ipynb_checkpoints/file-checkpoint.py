# If you have to scrap a website:
# 1. Use the API
# 2. HTML Web Scrapping using some tool like bs4

# Step 0 : Install requests,bs4
# pip install requests
# pip install bs4
# pip install html5lib


import requests
from bs4 import BeautifulSoup

url="https://codewithharry.com"


# Step 1: Get the HTML
r = requests.get(url)
htmlContent = r.content

# print(htmlContent)


# Step 2: Parse the HTML
soup = BeautifulSoup(htmlContent, 'html.parser')
# print(soup)
# print(soup.prettify)


# Step 3: HTML Tree transerval

#
#Commonly used typrs of objects :
# print(type(title)) 1. Tag
# print(type(title.string)) 2. NavigableString
# print(type(soup)) 3. BeautifulSoup
# 4. Comment

# print(soup.title) # Get title of html page

# paras = soup.find_all('p') #Get all the paragraphs
# print(paras)

# paras = soup.find('p') #Get 1st paragraphs
# print(paras)
# paras = soup.find('p')['class'] #Get class paragraphs
# print(paras)

# print(soup.find_all("p",class_="lead"))

# print(soup.get_text())

# Get all the links on the page

# anchors = soup.find_all('a')

# for link in anchors:
#     print('https://codewithharry.com'+link.get('href'))

# markup = "<p> <!-----This is comment---> </p>"

# soup2 = BeautifulSoup(markup)

# print(soup2.p)

abc = soup.find(id="navbarSupportedContent")

# .contents - A tag's children are available as a list
# .children - A tag's children are available as a generator

# for i in abc.strings:
#     print(i)

print(i for i in abc.parents)

# print(abc.contents)