import json
from http.client import responses
from urllib import request
from urllib import parse
'''
    http://www.data.go.kr
            - 회원가입필수
            - 일반인증키 요청 ( 바로 받을 수 있고 자료요청시 바로 승인됨 )

    >  관광자원통계서비스  >  상세기능 > 유료관광지방문객수조회
    : 전국의 주요 유로관광지 방문객수를 조회하기 위한 서비스로서
    기간,지역, 관광지별 외국인 방문객수와 내국인 방문객수를 조회한다.

    의미있는 데이타를 추출하여 출력한다

'''

access_key = 'gfv%2FQE9WxM7Y%2FZR%2BmfEXdk%2FYnRE9aixgUEIdoaDaKsWZGVNxhkpD83ZzAhbY3cIttskRXHal0dSoUPiF4M0EhQ%3D%3D'
url = 'http://openapi.tour.go.kr/openapi/service/TourismResourceStatsService/getPchrgTrrsrtVisitorList'
queryParams = '?_type=json'
queryParams += '&serviceKey=' + access_key
queryParams += '&YM=' + '201201'
queryParams += '&SIDO=' + parse.quote('부산광역시')
queryParams += '&GUNGU=' + parse.quote('해운대구')
queryParams += '&RES_NM=' + parse.quote('부산시립미술관')

req = request.Request(url + queryParams)
response = request.urlopen(req)
returnData = response.read().decode("UTF-8")
#print(returnData)

jsonData = json.loads(returnData)
#print(jsonData["response"]["body"]["items"]["item"])
resp = jsonData["response"]
body = resp["body"]
items = body["items"]
item = items["item"]

#해운대구 값 추출
gungu = item["gungu"]
print(gungu)
