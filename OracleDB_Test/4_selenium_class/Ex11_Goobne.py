"""
    [ 굽네치킨 매장 주소 가져오기 ]

    굽네치킨 http:www.goobne.co.kr > 매장찾기 > 매장찾기
                  http://www.goobne.co.kr/store/search_store.jsp

    개발자모드( F12 ) 열고 페이지 번호를 누르면
    <tbody> 부분이 교체되는 것을 볼 수 있다

    또한 2번 페이지 번호에 <a href="javascript:store.getList('2');">2</a>로 자바스트립트 함수를 호출한다.

    이 때 WebDriver 라는 특정 웹 브라우저의 원격 제어 인터페이스를 이용하고
    selenium 패키지를 이용하여  DOM  요소를 가져오거나 자바스크립트에서 제어하는 동작을 할 수 있도록 한다.
"""
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options

#-------------------------------1. 웹 페이지 접근
# 웹드라이버 객체 생성

# [1]
edge_options = Options()
edge_options.add_experimental_option("detach", True)
driver = webdriver.Edge(options=edge_options)

# 페이지 접근
# url = "http://www.goobne.co.kr/store/search_store.jsp"
url = "http://www.goobne.co.kr/store/search_store"
driver.get(url)
html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

loc = soup.select("div.search-select-area.search-select-area_new.search_select_zindex > div.nice-select.selectpicker > ul.list > li.option")
sidoList = []
nameList = []
locList = []
telList = []
for i in loc :
    if i.text == "선택" :
        continue
    else :
        sidoList.append(i.text)
print(sidoList)


store = soup.select("div#srchLocList > div.list")


#<지역 담기
choice = soup.select_one("div.search-select-area.search-select-area_new.search_select_zindex > div.nice-select.selectpicker >span.current")
for x in range(len(sidoList)) :
    handle = driver.find_element(By.CLASS_NAME, "current")
    handle.send_keys(sidoList[x])
    
for j in store :
    storeInfo = j.select("dl")
    for k in storeInfo :
        print(f"{k.find(".name").text}")
        print(f"{k.find(".local").text}")
        print(f"{k.find(".num").text}")
        print()


# for i in range(len(locList)) :
#     if


