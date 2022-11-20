'''
문자열(string)
    하나 이상의 연속된 문자(character) 들의 나열.
    파이썬에서 문자열자료형은 큰 따옴표("")
    또는 작은 따옴표('')
'''

#'hello' 와 "hello"는 동일
print("hello" == 'hello')

'''
변수에 문자열 할당
'''
a="Hello"
print(a)

'''
여러줄 문자열
    세개의 따옴표를 사용한 변수에 여러 줄 문자열 할당
'''

a = """피카츄, 라이츄, 파이리, 꼬부기
버터플, 야도란"""
print(a)
'''
문자열 배열
    문자열 인덱싱(indexing)
    h   e   l   l   o <== 문자열
    0   1   2   3   4
   -5  -4  -3  -2  -1 <== 마이너스 인덱스도 가능'''
a='hello'
print(a[1])
print(a[-4] == a[1])

'''
문자열 슬라이싱
    슬라이싱 구문을 사용하여 문자 범위를 반환할 수 있다.
    문자열의 일부를 변환하려면 시작 인덱스를 결론으로 구분하며 저장한다
    a:b 일시, a<= <b까지 출력'''
b="Hello, World"
print(b[2:5])
# 처음부터 슬라이스
print(b[:5])
# 마지막까지 슬라이스
print(b[2:])
a='Hello, World'
#소문자를 대문자로 자동변환
print(a.upper())
#대문자를 소문자로 자동변환
print(a.lower())

#문자열 바꾸기
a= 'Hello World'
print(a.replace("H", "J"))

#문자열 연결
a= "Hello"
b= "World"
c= a + b
print(c)
c= a+ " "+b
print(c)








