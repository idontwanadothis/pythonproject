"""
mutable - 메모리 값을 변경저장 가능 객체
"""
me = [1,2,3]
print(id(me))
me.append(4)
print(id(me))

"""
immutable - 메모리 값 변경 불가
    정수(int), 실수(float), 문자별(str), 튶플(tuple)
"""
me = 10
print(id(me))
me +=1 #me = me+1
print(id(me))
