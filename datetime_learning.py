import datetime

my_time = datetime.time(13,20,1,20)

print(my_time)
print(my_time.hour)
print(my_time.minute)

today = datetime.date.today()

print(today)
print(today.year)
print(today.month)
print(today.day)
print(today.ctime())

from datetime import datetime

t = datetime(2021,10,3,14,20,1)

print(t)

t = t.replace(year=2020)

print(t)

from datetime import date

date1 = date(2021,11,3)
date2 = date(2020,11,3)

result = date1 - date2

print(result)

print(type(result))


datetime1 = datetime(2021,11,3,22,0)
datetime2 = datetime(2020,11,3,12,0)

my_diff = datetime1 - datetime2

print(my_diff.seconds)
print(my_diff.total_seconds())