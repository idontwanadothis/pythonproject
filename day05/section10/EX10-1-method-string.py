'''
메소드(method) 란
    특정 객체가 가지고 있는 함수를 의미한다
    객체, 메소드() 사용가능
'''
# String 객체 format 메소드
print("10자리 쪽 왼쪽 정렬 '{:<10}'".format(123))
print("10자리 쪽 오른쪽 정렬 '{:>10}'".format(123))
print("10자리 쪽 가운데 정렬 '{:^10}'".format(123))
print()
print("10자리 폭 왼쪽 정렬 채움문자'{:*<10d}'".format(123))
print("10자리 폭 오른쪽 정렬 채움문자'{:*>10d}'".format(123))
print("10자리 폭 가운데 정렬 채움문자'{:*^10d}'".format(123))

# count() 메소드
s = '내가 그린 기린 그림'
result = s.count('기린')
print(result)

s = 'best of best'
result = s.count('best', 5) #index번호 5번 부터 찾기 시작
print(result)

# find() 메소드 위치한 인덱스 번호 변환
s = 'apple'
result = s.find('p')
print(result)

if result == -1 :
    print("존재하지 않는 문자 입니다.")
print(result)

s = 'best of best'
result = s.count('best', 5) #index번호 5번 부터 찾기 시작
print(result)

# index() find() 메소드와 같지만 문자열이 존재하지 않을 경우 에러 발생 !!
s = 'apple'
result = s.index('p')
print(result)















