"""
경로 이동은  Path 모듈로 안되어 os 모듈이 필요하다
"""
import os
import pathlib
import shutil

os.chdir("..")
print(pathlib.Path.cwd())

# shutil.rmtree("temp2") #It can delete directory with in file or folder
# shutil.copy("Ex00.txt", pathlib.Path("./imsi/copy2.txt")) #copy file
# shutil.copytree("imsi", "../copydir") #copy between directory