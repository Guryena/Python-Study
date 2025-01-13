'''
    # [참고] 파이썬 정규식 표현
            - https://docs.python.org/3/library/re.html
            - https://wikidocs.net/4308 > re

    # findall(검색어, 문자열) : 문자열에서 검색어와 일하는 내용들을 리스트로 반환
                search가 최초로 매칭되는 패턴만 반환한다면, findall은 매칭되는 전체의 패턴을 반환
                매칭되는 모든 결과를 리스트 형태로 반환

'''

import re

msg = 'We_are_happy!! You are happy?? Happy2019-2020 안녕'

a = re.findall("happy", msg)
# print(a)




# 소문자를 모두 찾아서 리스트로 반환
r = re.findall("[a-z]", msg)
print(r)

# 소문자가 아닌 것들을 모두 찾아서 리스트로 반환 ( 대괄호 안에 ^ )
r = re.findall("[^a-z]", msg)
print(r)
# +반복 옵셥으로 소문자를 연속해서 찾음 ( 즉, 단어 )
r = re.findall("[a-z]+", msg)
print(r)
# 대문자를 모두 찾음
# r = re.findall("[\x41-\x5A]", msg)
r = re.findall("[A-Z]", msg)
print(r)
# 소문자와 대문자를 단어 단위로 찾음
r = re.findall("[a-zA-Z]+", msg)
print(r)
# 숫자를 모두 찾음
# r = re.findall("\d", msg)
r = re.findall("[0-9]", msg)
print(r)
# +반복 옵션으로 숫자를 연속해서 찾음


# 소문자, 대문자, 숫자가 아닌 문자들 ( 공백문자나 특수문자 )


# 문자 숫자 _ 를 검색


# 영문자 숫자 _가 아닌 것들 검색

