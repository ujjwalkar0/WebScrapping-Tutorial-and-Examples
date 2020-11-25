import requests
from bs4 import BeautifulSoup

url="https://www.youtube.com/c/GreatLearningOfficial/featured"

r = requests.get(url)
htmlContent = r.content
soup = BeautifulSoup(htmlContent, 'html.parser')
print(soup.find_all("a",class_="yt-simple-endpoint style-scope ytd-grid-video-renderer"))

# print(soup.find_all('a'))