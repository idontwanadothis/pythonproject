'''
추상 메소드(Abstract method)
    선언만 하고 구현되지 않은 미완성 메소드

추상 클래스(Abstract class)
    추상 메소드를 하나이상 가지고 있는 클래스

오버라이딩
    슈퍼클래스 메소드 재정의

'''

from abc import*

class Family(metaclass=ABCMeta):
    @abstractmethod
    def introduce(self):
        pass

class Person(Family):
    pass

a = Person()













