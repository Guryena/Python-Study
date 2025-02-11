from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.edge.options import Options

url = "https://www.youtube.com/playlist?list=OLNY56MxFrczc5CoAvnTCDO_3bAdOLExkJQ"

edge_options = Options()
edge_options.add_experimental_option("detach", True)
browser = webdriver.Edge(options=edge_options)

browser.get(url)

html = browser.page_source
soup = BeautifulSoup(html, "html.parser")
musicRank = soup.select(".style-scope ytd-playlist-video-list-renderer")
for mrank in musicRank :
    rank = mrank.select("#index")
    title = mrank.select("#video-title")
    uploader = mrank.select(".yt-simple-endpoint.style-scope.yt-formatted-string")
    for i in range(len(rank)) :
        print(f"{rank[i].text} : {title[i].text} / {uploader[i].text}")
        print()


# musicList = soup.select("#video-title")
# for i in musicList :
#     print(i.text)

# <a id="video-title" class="yt-simple-endpoint style-scope ytd-playlist-video-renderer" title="[MV] ASH ISLAND - 생각이 나서" href="/watch?v=reAiz0wdgTw&amp;list=OLNY56MxFrczc5CoAvnTCDO_3bAdOLExkJQ&amp;index=1&amp;pp=iAQB8AUB">
#           [MV] ASH ISLAND - 생각이 나서
#         </a>