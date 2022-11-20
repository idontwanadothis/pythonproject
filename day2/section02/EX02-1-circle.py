'''파일명 : EX02
개요: 반지름을 전달하면 원의 넓이를 변환하는 get_area()함수'''

import math
#get_area() 함수 정의
def get_area(radius):
        """반지름을 입력받아서 원의 넓이를 반환하는 get_area() 함수"""
        area = math.pi * math.pow(radius, 2)
        return area

radius = 1.5
print(radius)

#get_area() 함수 정의
area= get_area(radius)
print(area)
print(get_area.__doc__) #Docstring 확인