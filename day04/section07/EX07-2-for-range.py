'''
for문과 range 함수
'''

'''
range(stop)
'''
dan = int(input('출력할 구구단을 입력하세요 >>> '))
for n in range(10):
    print('{} x {} = {}'.format(dan, n, dan * n), end='')
print()
'''
range(start, stop, step)
'''
# 1부터 2씩 증가 <10
for n in range(1, 10, 2):
    dan = int(input('출력할 구구단을 입력하세요 >>> '))
    for n in range(10):
        print('{} x {} = {}'.format(dan, n, dan * n), end='')
        print()