'''
r (read mode) : 읽기 전용 모드 / 파일없으면 에러 반드시 디렉토리 안에 파일이 먼저 형성되어 있어야 함

절대 경로 예) C:\hello.txt
상대 경로 예) ../test/hello/txt
            .. -> 상위 폴더
            . -> 현재 폴더

'''

file = open('hello.txt', 'rt', encoding='UTF-8')
str = file.read()
print(str, end='')
file.close()

with open('hello.txt', 'rt', encoding='UTF-8') as file:
    str = file.read()
    print(str, end='')
    file.close()














