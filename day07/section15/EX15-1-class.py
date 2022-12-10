'''
클래스
    객체를 만드는 설계도
    붕어빵 틀, 와플 기계
    인스턴스화 - 메모리


객체(object)
    현실세계에서 존재하는 물리적, 추상적 식별할 수 있는 모든 것
    예) 컴퓨터, 학생, 주문,

객체 구성
    생성자 - 초기화용
    속성 값 - 변수
    기능 - 메소드(함수)
'''

# Computer 클래스 정의
class Computer:

    # 첫번째 매개변수가 self 이므로 인스턴스 메소드이다.

    def set_spec(self, cpu, ram, vga, ssd):
        self.cpu = cpu
        self.ram = ram
        self.vga = vga
        self.ssd = ssd

    def hardware_info(self):
        print('CPU = {}'.format(self.cpu))
        print('RAM = {}'.format(self.ram))
        print('VGA = {}'.format(self.vga))
        print('SSD = {}'.format(self.ssd))
        print('')

desktop = Computer()
desktop.set_spec('17', '16GB', 'GTX3060', '512GB')
desktop.hardware_info()
desktop.cpu = 19
desktop.hardware_info()

macbook = Computer()
macbook.set_spec('N2', '16GB', 'M2', '512GB')
macbook.hardware_info()

print(id(desktop))
print(id(macbook))
















