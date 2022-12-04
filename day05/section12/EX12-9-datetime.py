'''
datetime
    날짜와 시간 데이터를 처리할 때 사용함
'''

import datetime
# 현재 날짜와 시간 변환
print(datetime.datetime.now())
print(datetime.datetime.today())

# date()함수를 이용하여 특정날짜 만들어 전환
print(datetime.date(2022,12,4))
print(datetime.time(10,40,0))
y = datetime.datetime.now().year
m = datetime.datetime.now().month
d = datetime.datetime.now().day

H = datetime.datetime.now().hour
M = datetime.datetime.now().minute
s = datetime.datetime.now().second

print('{}년 {}월 {}일 {}:{}:{}'.format(y, m, d, H, M, s))

today = datetime.datetime.now()
yesterday = today - datetime.timedelta(days=1)
print(yesterday)

tomorrow = today + datetime.timedelta(days=1)
print(tomorrow)

date1 = datetime.date(2022, 1, 1)
date2 = datetime.date(2023, 1, 1)

print((date2 - date1).total_seconds()) # 전체 초 계산












