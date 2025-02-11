"""
http://www.seoul.go.kr > 청사안내 > 자치구
https://www.seoul.go.kr/seoul/autonomy.do

BeautifulSoup  : 파서를 이용해서 html 의 요소를 추출하게 해주는 모듈
        - 단점은 개행문자를 고려해야 한다
Tag : 태그
NavigableString : 원래는 tag 사이의 문자열

#  xpath를 사용하면 개행문자를 고려하지 않아도 된단다
#  https://developer.mozilla.org/ko/docs/XPath
"""
import re

import requests
from bs4 import BeautifulSoup, NavigableString

# 웹 문서 가져오기
url = 'https://www.seoul.go.kr/seoul/autonomy.do'
parsingURL = requests.get(url)
site = parsingURL.content

#구청이름/주소/전화번호/홈페이지
soup = BeautifulSoup(parsingURL.text, "html.parser")
name = soup.select("li.tabcont > strong")
getAddress = soup.select("li.tabcont > ul > li:first-child")
address = []
for i in getAddress :
    # print(i.text)
    address.append(i.text.split(" / ", 1)[1])

tel = soup.select("li.tabcont > ul > li:nth-child(2)")
homepage = soup.select("li.tabcont > ul > li:nth-child(3)")

for i in range(len(name)) :
    print(f"{name[i].text} : {address[i]} / {tel[i].text} / {homepage[i].text}")