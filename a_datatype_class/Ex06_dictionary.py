"""
    [ dictionary 형 ]

    1- 키와 값으로 구성 ( 자바의 map 와 유사 )
    2- 저장된 자료의 순서는 의미 없음
    3- 중괄호 {} 사용
    4- 변경가능

    ` 사전.keys() : key만 추출 (임의의 순서)
    ` 사전.values() : value만 추출 (임의의 순서)
    ` 사전.items() : key와 value를 튜플로 추출 (임의의 순서)
"""

print('--------- 1. 딕셔너리 요소 --------------- ')
dt = {1: 'one', 2: 'two', '3': 'three'}
print(dt[1])
print(dt.values())
for k, v in dt.items():
    if v == 'two':
        print(k)
# dt.setdefault(1, "first")
dt[1] = "first"
dt.setdefault(3, "third") ## If exist key already, return to previous key:value
print(dt)

# 키는 숫자와 문자 그리고 튜플이여야 한다. 즉 리스트는 안된다.
# 리스트의  값이 변경 가능하다. 그러나 키값을 변경하면 안되므로 리스는 안된다
dt2 = {1: 'one', 2: 'two', (3, 4): 'turple'}
print(dt2[(3, 4)])

print('--------- 2. 딕셔너리 추가 및 수정  --------------- ')
dt2["4"] = "forth"
print(dt2)
# 여러개 추가할 때
dt2.update({5: "five", (0, 4): "six"})
print(dt2)
print()

dt3 = dict(ten="ten", one="one")  ## This dict() function is unable to int in key
## Key is must have string type
print(dt3)
print('--------- 3. Key로 Value값 찾기  --------------- ')

# Key와 Value만 따로 검색
print(dt.keys())
print(dt.values())
print(dt.items())