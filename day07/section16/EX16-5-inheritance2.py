class A:
    def greeting(self):
        print('안녕하세요. A입니다.')

class B(A):
    def greeting(self): #오버 라이팅
        print('안녕하세요. B입니다.')

class C(A):
    def greeting(self):
        print('안녕하세요. C입니다.')

class D(B, C):
    pass        #내부 동작 필요없고 빈껍데기만 필요할 때 pass 사용


x = D()
x.greeting()
print(D.mro()) # D 내부에서 우선순위 출력. 이 경우에는 B가 선순위











