import requests
from bs4 import BeautifulSoup
headers = {'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) '
           'AppleWebKit/537.36 (KHTML, like Gecko)'
           ' Chrome/132.0.0.0 Safari/537.36 Edg/132.0.0.0'}
#녹색 글자만 추출하여 출력
url = "http://www.pythonscraping.com/pages/warandpeace.html"
ParsingURL = requests.get(url)
soup = BeautifulSoup(ParsingURL.text, "html.parser")
#print("check")
green = soup.select(".green")

for g in range(len(green)):
  g_text = green[g].text.replace("\n", " ")
  print(g_text)

#-------------------------------------------
