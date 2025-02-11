import urllib.parse
from contextlib import nullcontext
from http.client import responses
from urllib import request, parse
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options

def movieLink (baseURL, link):

    movieLink = baseURL + link
    parsingURL = requests.get(movieLink, timeout = 5)

    soup = BeautifulSoup(parsingURL.text, "html.parser")

    comment = soup.select("span.comment")
    title = soup.select_one("p.tit")
    print(title.text)
    for i in comment :
        print(f"{i.text}")
try :
    edge_options = Options()
    edge_options.add_experimental_option("detach", True)
    driver = webdriver.Edge(options=edge_options)


    baseURL = "http://www.cine21.com"
    movieURL = "/movie"
    listsURL = "/lists"
    playingURL = "/playing"
    indexURL = urllib.parse.urljoin(base = baseURL,
                                    url = movieURL + listsURL + playingURL,
                                    allow_fragments = True)
    driver.get(indexURL)
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")

    ##Movie INFO
    links = []
    movieInfo = soup.select("li.mov_info_li")

    for i in movieInfo :
        href = i.select("a")
        for j in href :
            links.append(j["href"])


    for n in range(len(links)) :
        movieLink(baseURL, links[n])




except TimeoutError as e :
    print("Timeout Error")
finally:
    driver.close()