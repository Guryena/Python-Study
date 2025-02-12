'''
1. 크롬웹드라이버로 구글 사이트 열기

2. 실제 크롬창에서 '플레이데이터'라고 검색버튼을 누른다.
    개발자모드(F12)에서 이 부분을 보면
    <input name='q' value='플레이데이터'~~ >
    그리고 'google검색' 버튼이 type='submit' 인거 확인
'''
from re import search
from tkinter.font import names

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options

# [1]
edge_options = Options()
edge_options.add_experimental_option("detach", True)
driver = webdriver.Edge(options=edge_options)
url = "https://google.com"
driver.get(url)
#----------------------------------------------
# [2]
# search_bar = driver.find_element(By.CLASS_NAME, "gLFyf")
search_bar = driver.find_element(By.NAME, "q")
search_bar.send_keys("playdata")
search_bar.send_keys(Keys.ENTER)



