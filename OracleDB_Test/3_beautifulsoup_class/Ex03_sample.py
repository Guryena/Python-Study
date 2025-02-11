from bs4 import BeautifulSoup
from urllib import request
import requests
headers = {'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) '
           'AppleWebKit/537.36 (KHTML, like Gecko)'
           ' Chrome/132.0.0.0 Safari/537.36 Edg/132.0.0.0'}
    # 기상청 사이트에서 필요한 데이타를 추출하고자 한다면?
    #     - 데이타 가져오기     ` requests 모듈
    #                          ` urllib.request 모듈의 urlopen() 이용
    #     - 데이타 추출    BeautifulSoup 이용




# 1. 데이타 가져오기
URL = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=109"
ParsingData = requests.get(URL)
soup = BeautifulSoup(ParsingData.text, "html.parser")

# 2. 필요 데이타 추출하기
# title = soup.find("title")
ch_title = soup.channel.title
print(ch_title.text)

city = soup.find_all("city")
# for i in city :
#     print(i.text)

wfs = soup.find_all("wf")
# for i in wfs :
#     print(i.text)

data = soup.find_all("data")
# for i in data:
#     t = i.find("wf")
#     print(t.text)

location = soup.select("location")
for loc in location :
    cities = loc.select("city")
    for city in cities :
        tmEf = loc.select("tmEf")
        wf = loc.select("wf")
        for i in range(len(tmEf)) :
            print(f"{city.text} = {tmEf[i].text} : {wf[i].text}")

#제목/도시/시간대별 날씨 상태 등