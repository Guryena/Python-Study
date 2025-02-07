import requests
from bs4 import BeautifulSoup

html = """
    <html>
        <body>
            <h1>스크래핑 연습</h1>
            <p>웹 페이지 분석</p>
            <p>데이터 정제</p>
        </body>
    </html>
"""
# data parsing
soup  =BeautifulSoup(html, 'html.parser')

# approach elements
h1 = soup.html.body.h1
p = soup.find('p')

#extract elements
#print(h1)
#print(p.text)

p2 = soup.find_all('p')
#for i in p2:
#    print(i)

    
