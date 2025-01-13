import json
from json import loads

jfile = open("./data/temp.json", "r", encoding="utf-8")

jsonData = jfile.read()
print(jfile)

data = loads(jsonData)
print(data)

for i in data:
    print("name : ", i)
    # print(data[i])

    for k in data[i]:
        print(f"{k} : {data[i][k]}")
    print()