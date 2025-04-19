import requests
from bs4 import BeautifulSoup
import time

headers = {'User-Agent': 'Mozilla/5.0'}
url = 'https://www.forethought.co.in/founders'

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')
titles = soup.find_all('ul')
for title in titles:
    print(title.text)



