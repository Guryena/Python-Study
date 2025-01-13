'''
    # compile
     - 동일한 정규표현식을 매번 다시 쓰기 번거로움을 해결
     - compile로 해당표현식을 re.RegexObject 객체로 저장하여 사용가능
'''

import re
from contextlib import nullcontext

email_reg = re.compile(r"[\w-]+@[\w.]+")
email = "test@gmail.com asdfsadfsafaf1232!@"
reg = email_reg.search(email)
print(reg)
print(reg.group())
print()
#----------------------------------------
webs = ['http://www.test.co.kr',
        'https://www.test1.com',
        'http://www.test.com',
        'ftp://www.test.com',
        'http:://www.test.com',
       'htp://www.test.com',
       'http://www.google.com',
       'https://www.homepage.com.']

web_reg = re.compile(r"https?://[\w.]+\w+$")
result = list(map(lambda w :web_reg.search(w) != None, webs))
print(result)

for i in webs:
    result1 = web_reg.search(i)
    if result1:
        print(result1.group())
