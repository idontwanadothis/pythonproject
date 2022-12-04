'''
random
    난수 생성을 해주는 모듈
'''
import random

# 두 수 사이의 난수
print(random.randint(1,10)) #1 ~ 10

# range 함수 비슷
print(random.randrange(10)) # 0 ~ 9
print(random.randrange(1, 10)) # 1 ~ 9
print(random.randrange(1, 10, 2)) # 1 ~ 9, 2씩 증가하는 값들 중(홀수만)
print(random.random()) # 0이상 1미만의 랜덤 값

if random.random() < 0.5:  #일정확률로 출력
    print('안녕하세요')


# choice 함수 - 리스트에서 랜덤
seasons = ['spring', 'summer', 'fall', 'winter']
print(random.choice(seasons))

#
my_List = [1, 2, 3, 4, 5]
random.shuffle(my_List)
print(my_List)

my_tuple = (1, 2, 3, 4)

mylist = list(my_tuple)

print(mylist)

print(type(my_tuple))