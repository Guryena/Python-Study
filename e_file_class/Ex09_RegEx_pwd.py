"""
    비밀번호 생성시 의 적합성 체크
    1. 비밀번호의 길이는 6-10
    2. 숫자와 알파벳으로만 구성되어야 함
    3. 대문자와 소문자가 섞여야 함 ( 대문자 1개 이상, 소문자 0개 이상)
    4. 위의 조건에 부합하면 잘못된 상황을 출력하고
       조건을 모두 만족하면 가능한 비밀번호임을 출력한다.
"""

import re
def pwd_check(pwd):
    if len(pwd) < 6 or len(pwd) >12:
        print(pwd, "length is wrong")
    elif re.findall("[0-9a-zA-Z]+", pwd)[0] != pwd :
        print(f"{pwd} is composed to number and alphabet")
    elif len(re.findall("[a-z]", pwd)) == 0 or len(re.findall("[A-Z]", pwd)) == 0:
        print(f"{pwd} (은)는 대문자와 소문자가 1개이상 포함되어야 합니다.")
    else :
        print(f"{pwd} is OK")

pwd_check('abcdE')          # 길이오류
pwd_check('abcdef')         # 대문자 포함하지 않아 오류
pwd_check('Abcdef2')        # 성공
pwd_check('Abcdef_2')       # 특수문자 포함