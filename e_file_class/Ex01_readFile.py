"""
@ 파일 읽고 쓰기
    - 파일을 읽고 쓰기 전에 파일을 열어야 한다
    - fileObj = open ( filename, mode )
            mode 첫번째 글자 - 작업 표시
            r(read)  : 파일 읽기
            w(write) : 파일 쓰기 ( 파일이 없으면 생성하고 파일이 있으면 덮어쓴다 )
            x(write) : 파일 쓰기 ( 파일이 없을 때만 생성하고 쓴다 )
            a(append) : 파일 추가 ( 파일이 있으면 파일의 끝에서부터 추가하여 쓴다 )

            mode 두번째 글자 - 파일 타입
            t : 텍스트(text) 타입 ( 기본값 )
            b : 이진(binary) 타입
            두번째 글자가 없으면 텍스트 타입이다.

            encoding='utf-8' : 한글

    - 파일을 열고 사용 후에는 반드시 닫아야 한다
"""
import logging
import os.path
from os import close
from random import sample

try:
    file = open("./data/test.txt", "r", encoding="utf-8")
    print(file.read())
except Exception as e:
    print(e)
    print("Not Found File")
else:
    while (1):
        line = file.readline()
        if not line:
            break
        print(line)
    file.close()
finally:
    print("Exit")
print()



fileAddress = "./data/"
testText = "test.txt"
file = fileAddress + testText
fileName = os.path.basename(file)
try:
    cntWord = 0
    cntSentence = 0
    with (open(file, "r", encoding="utf-8") as f):
        # while (1):
            # line = f.readline()
        contents = f.read()

        sentence = contents.split("\n")
        cntSentence += len(sentence)
            # cntSentence += len(line)
        # while (1):
        #
        #     words = sentence.split()
        #     print(len(words))
        #     cntWord += len(words)
        #
        #     if not line:
        #         break

        print(contents)
        f.close()

    print(f"File Adress is ({file})\nfile name is ({fileName})")
    print(f"count sentence : {cntSentence}")
    print(f"count words : {cntWord}")

except Exception as e:
    print(f"Fail : "+ str(e))