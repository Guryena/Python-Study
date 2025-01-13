"""
 - import pathlib 만 선언하면
        Path클래스 사용시 pathlib.Path라고 명시해야 한다. 
"""
import pathlib
p = pathlib.Path("..")
print(p)
print(p.resolve())
print()
# (1) 해당 경로와 하위 목록들 확인
test = []
for x in p.iterdir():
    if x.is_dir():
        test.append(x)
print(test)

i = [x for x in p.iterdir()
     if x.is_dir()]
print(i)

j = list(p.glob("**/data/*.*"))
print(j)

k = list(p.glob("a_datatype_class/*.py"))
print(k)