'''
함수(function)
    하나의 특별한 목적의 작업을 수행하기 위해
    독립적으로 설계된 프로그램 코드의 집합.

def 함수이름(매개변수)
    코드 실행문
    return 반환값
'''

def welcome(): #매개변수 X 리턴 X
    print('Hello Python')
    print('Nice to meet you')

welcome() #함수 호출(살행)

def Introduce(name, age):
    print('내 이름은 {}이고, 나이는 {}살 입니다.'.format(name, age))
Introduce('James', 25)

def show(*args):
    print(type(args)) #튜플로 변환
    for item in args:
        print(item)
show('python')
show('python', 'happy', 'birthday')

#반환 값이 있는 함수
def address():
    str = '우편번호 12345\n'
    str += '서울시 영등포구 여의도동'
    return str
result = address()
print(result)

#매개변수 o 리턴 o
def plus(num1, num2):
    return num1 + num2

print(plus(1,3)) #4

area = 0
def move():
    global area #글로벌로 정의해서 내외부 다 사용할 수 있게 해야 retuen값 선언가능
    area +=1
    return area
























