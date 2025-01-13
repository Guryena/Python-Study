import pathlib
import stat

# ------------------------------------------------
# 1. 경로의 상태보기
print(pathlib.Path.cwd())
print(pathlib.Path.home())

p1 = pathlib.Path("Ex03_createPath.py")
print(p1.stat())
print("----------------------------------------------------")
# 2. 경로(파일) 생성시간 알아보기
p2 = pathlib.Path("Ex03_createPath.py")
tm = p2.stat()[stat.ST_CTIME]
print(tm)


print("----------------------------------------------------")
# 3. 디렉토리 생성
# p3 = pathlib.Path("imsi")
# p3.mkdir()
#
# p3 = pathlib.Path("imsi")
# p3.mkdir(exist_ok=True)
#
# p3 = pathlib.Path("imsi")
# p3.mkdir(parents=True) ##여러개의 디렉토리를 한번에 생성
# ------------------------------------------------
# 4. 파일 생성
# f = open("imsi/1.txt", "w", encoding="utf-8")
# f.write("하이")
# f.close()
f2 = "./imsi/2.txt"
# with open(f2, "w", encoding="utf-8") as f:
#     f.write("헬로")
    # f2.close()
f3 = pathlib.Path("./imsi/3.txt")
# f3.write_text("こんにちは")
# print(f3.read_text())

##rename
# f3.rename("./imsi/3-1.txt")

# ------------------------------------------------
#  5. 경로 제거
# If exist directory, can't remove
# f4 = pathlib.Path("./imsi/1.txt")
# f4.rmdir()

# It can
f4 = pathlib.Path("./imsi/1.txt")
# f4.unlink()
f4 = pathlib.Path("./imsi/2.txt")
# f4.unlink()
f4 = pathlib.Path("./imsi/3-1.txt")
# f4.unlink()
f4 = pathlib.Path("./imsi")
# f4.rmdir()