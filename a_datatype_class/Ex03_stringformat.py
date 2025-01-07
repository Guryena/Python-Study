from lib2to3.pgen2.tokenize import group

# -----------------------------------------
#  문자열 포맷
#       0- 문자열 포맷팅
#               print('내가 좋아하는 숫자는 ', 100 )
#       1- format() 이용
#               print('내가 좋아하는 숫자는 {0:d} 이다'.format(100) )
#       2- % 사용
#               print('내가 좋아하는 숫자는 %d 이다' % 100 )
#       성능(속도)는 %이 더 빠르다고는 하지만 코드가 깔끔하게 하는 것이 더 중요하다고 하고는
#       어느 것으로 선택하라고는 안 나옴
msg = '{}님 오늘도 행복하세요'
print(msg.format('X'))
msg = '{}님 오늘도 행복하세요~ from {}'
print(msg.format("X", "Y"))
msg = '{1}님 오늘도 행복하세요~ from {0}'
print(msg.format("Y", "X"))
msg = '{name}님 오늘도 행복하세요~ from {group}'
print(msg.format(name="X", group="Y"))

# [참고] http://pyformat.info
# [나만참고] http://blog.naver.com/PostView.nhn?blogId=ksg97031&logNo=221126216595&parentCategoryNo=&categoryNo=172&viewDate=&isShowPopularPosts=true&from=search

# print format - printf() 역할
name = '홍길동'
age = 22
height = 170.456
print("%s님은 %d세이며, %.1fcm입니다" %(name, age, height))
print(f"{name}은 {age}, {height:.1f}cm")
height = 170.456
print("{:.1f}cm".format(height))
#--------------------------------------------------
# 실수인 경우


