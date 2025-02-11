"""
 간단하게 크롬 브라우저를 실행하여 페이지 열기
"""
import time

from selenium import webdriver
from selenium.webdriver.edge.options import Options

# 1. webdriver 객체생성

# driver_path = "/Users/guryena/.wdm/drivers/edgedriver/mac64/132.0.2957.140/msedgedriver"
# driver = webdriver.Edge(executable_path=driver_path)
edge_options = Options()
edge_options.add_experimental_option("detach", True)
driver = webdriver.Edge(options=edge_options)

# 2. 페이지 접근
url = "https://google.com"
driver.get(url)

# 3. 화면을 캡처해서 저장하기
# driver.save_screenshot("Page.png")