'''
파일복사
    원본 -> 버퍼변수 (memory) -> 복사본
'''

buffer_size = 1024 #1024byte로 1KB 의미
with open('hello.txt', 'rb')as source: # hello.txt.를 소스로 꺼내옴
    with open('hello2.txt', 'wb') as copy: # 복사(copy) 기능 가져 옴
        while True:
            buffer = source.read(buffer_size) #1024Byte 단위로 읽기
            if not buffer:
                break
            copy.write(buffer)
print('hello.txt 파일이 복사되었습니다.')