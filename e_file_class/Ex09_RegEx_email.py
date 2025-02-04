"""
    이메일 주소의 적합성 체크
        kim@encore.com   : 올바른 이메일
        kim@encore       : 잘못된 이메일 ( . 하나 없어서 )
        k!m@encore.com  : 잘못된 이메일 ( 특수문자 ! 안됨 )

     [참고]
        ^[]: 시작
        [^] : not
        {2,9} : 최소 2개 최대 9개
        {2,} : 최소 2개만 지정하고 최대는 지정하지 않음
        $ 끝
"""
import re
def email_check(email):
    # 여기에 코드 작성
    email_reg = re.compile(r"[0-9A-Za-z]+@[\w.]+[\w]$")
    if email_reg:
        print("True")
        return True
    else:
        print("False")
        return False
email_check('kim@encore.com')       # 올바른 이메일
email_check('kim@encore')           # 잘못된 이메일 ( . 하나 없어서 )
email_check('k!m@encore.com')      # 잘못된 이메일 ( 특수문자 ! 안됨 )
