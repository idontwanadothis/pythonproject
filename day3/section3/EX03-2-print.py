"""
print() 함수 사용법
    sep : 출력할 value의 구분 문자
"""
print("재미있는", "파이썬")
print("Python", "JAVA", "C", sep=',') # 사이사이에 해당 값이 들어가서 print 됨
print("안녕", end='') #줄 바꿈 안하고 바로 다음 결과 출력
print("하세요")

fos = open('sample.py', mode='wt') #sample.py라는 메모장을 생성 한다는 의미
print('print("Hello World")', file=fos) # 해당 메모리 공간에 저장 하겠다는 것
fos.close()