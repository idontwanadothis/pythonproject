my_List = []
n = int(input('정수를 입력하세요(종료는 0입니다.) >>> '))

while n != 0:
    my_List.append(n)
    n = int(input('정수를 입력하세요(종료는 0입니다) >>> '))
print(my_List)