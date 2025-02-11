from bs4 import BeautifulSoup
from urllib import parse
from urllib import request
import os, time, re  # re : 정규식

    # 파일을 다운받고 저장하는 함수
    #  [참고] 파이썬 정규식 표현 : https://wikidocs.net/4308



def download_file(url):
    p = parse.urlparse(url)
    print("1-", p)
    savepath = "./" + p.netloc + p.path
    print("2-", savepath)

    #check file in PC
    if os.path.exists(savepath) :
        return savepath

    #create folder with download file
    savdir = os.path.dirname(savepath)
    if not os.path.exists(savdir) :
        os.mkdir(savdir)

    #download file
    # try :
    #     print(f"download = {url}")
    #     request.urlretrieve(url, savepath)
    #     time.sleep(2) #Because  delay protocol
    #     return savepath
    # except :
    #     print("fail download")
    #     return None




if __name__ == '__main__':
    url = 'https://docs.python.org/3.6/library/'
    result = download_file(url)
    # print(result)



