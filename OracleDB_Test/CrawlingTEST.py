import requests
from bs4 import BeautifulSoup
headers = {'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) '
           'AppleWebKit/537.36 (KHTML, like Gecko)'
           ' Chrome/132.0.0.0 Safari/537.36 Edg/132.0.0.0'}

data = requests.get('http://www.cgv.co.kr/movies/?lt=1&ft=0')
#print(data.content)
soup = BeautifulSoup(data.text, 'html.parser')
#print((soup))
ol = soup.find('ol')
li = ol.find_all('li')

for i in li:
    div = i.find('div', {'class': 'box-contents'})
    a = div.find('a')
    strong = a.find('strong').text
