import csv
from symbol import continue_stmt

# type csv is trans txt text or excel

# 1 save to csv file from list data
# data = [[1, 'Kim', "PM"], [2, "Pak", "Sales"], [3, "Lee", "PL"]]
# with open("./data/imsi.csv", "wt", encoding="utf-8") as f:
#     cout = csv.writer(f)
#     cout.writerows(data)

#2 read csv file, save variation in list
data = []
with open("./data/imsi.csv", "rt", encoding="utf-8") as fin:
    #read all
    cin = csv.reader(fin)
    #input data[]
    data = [row for row in cin
            if row]

print(data)
