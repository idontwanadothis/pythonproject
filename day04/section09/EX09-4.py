'''
내장함수 보충
'''
result = format(10000) #string과 같음
print(type(result))
result = format(10000, ',') # 천단위 쉼표
print(result)


# abs() = 절댓값
result = abs(10)
print(result)
result = abs(-10)
print(result)

# max() = 최댓값
# min() = 최솟값

result = max(1, 10)

print(result)
li = [5, 4, 3, 2, 1]
result = max(li)
print(result)

# pow() 거듭제곱 함수
result = pow(10, 2)
print(result)

# sorted() 함수 = 정렬
my_li = [5, 6, 3, 4, 1, 2]
result = sorted(my_li)
print(result) # 오름차순 정렬
result = sorted(my_li, reverse = True)
print(result) # 내림차순 정렬

# zip()함수 - 같은 인덱스 번호끼리 tuple로 묶어줌
names = ['james', 'emily', 'amanda']
scores = [60, 70, 80]
for student in zip(names, scores):
    print(student)

names = ['james', 'emily', 'amanda']
scores = [60, 70, 80]
for name, score in zip(names, scores):
    print('{}의 점수는 {}점 입니다'.format(name, score))





























