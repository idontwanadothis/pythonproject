my_List = []
n = 1
while n != 0:
    n = int(input('정수를 입력하세요(종료는 0입니다.) >>> '))
    my_List.append(n)
my_List.pop()
print(my_List)