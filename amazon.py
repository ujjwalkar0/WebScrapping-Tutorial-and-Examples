import requests
import pandas as pd 
from bs4 import BeautifulSoup as bs
import re
import numpy as np

b=input("Enter products name you want to scrap : ").split()
num_pages=int(input("Enter the number of pages you want to scrap"))
c=0
for m in b:
    lst=list()
    for n in range(1,num_pages+1):
        r2 = "https://www.flipkart.com/search?q="+str(m)+"&sort=popularity&page="+str(n)
        r = requests.get(r2)
        soup = bs(r.content,'html.parser')
        for i,j,k in zip(soup.find_all('div',class_='col col-7-12'),soup.find_all('ul',class_='vFw0gD'),soup.find_all('div',class_='_1vC4OE _2rQ-NK')):
            print(i)
            print(j)
            print(k)
            print("""
            
            """)