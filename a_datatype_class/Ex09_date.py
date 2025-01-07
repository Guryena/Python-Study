from datetime import datetime, date
from datetime import timedelta
from http.cookiejar import month

today = date.today()
print('today is ', today)
print()

##yymmdd
print(f"{today.year}년 {today.month}월 {today.day}일")
t = datetime.today()
print(t)
print()

##calculate date
today = date.today()
print(today + timedelta(days=-1))
print(today + timedelta())
print()

today = datetime.today()
print(today.strftime("%Y/%m/%d"))
print(today.strftime("%y/%m/%d"))
print()

##change date of string type to date type
str = "2025-01-06 10:30:21"
myDate = datetime.strptime(str, "%Y-%m-%d %H:%M:%S")
print(myDate)