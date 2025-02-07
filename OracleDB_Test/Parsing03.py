from bs4 import BeautifulSoup

html = """
    <html>
        <body>
            <ul>
                <li><a href='https://www.naver.com'>네이브</a></li>
                <li><a href='http://www.daum.net'>다아음</a></li>
            </ul>
        </body>
    </html>
"""

soup = BeautifulSoup(html, 'html.parser')
ul = soup.body.ul
li = soup.find_all('li')
for i in li:
    a = i.find('a')
    href = a.attrs['href']
    print(f'{a.string} : {href}')
    print()
    print(f'{a.text} : {href}')



#tag
#tag.attrs['attribute']