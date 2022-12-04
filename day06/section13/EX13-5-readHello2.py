'''
file 객체 read() -> 전체 읽어오기

'''

file = open('hello.txt', 'rt', encoding='UTF-8')
while True:
    str = file.read(5)
    print(str)
    if not str:
        break
    print(str, end='')












