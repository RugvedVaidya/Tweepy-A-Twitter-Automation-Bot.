import requests
from bs4 import BeautifulSoup

 
url = 'https://www.bbc.com/news/technology'

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Find the container elements that wrap the headlines
headlines = soup.find('body').find_all('h3')
