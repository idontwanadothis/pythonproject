'''
모듈 (module)
    변수나 함수 또는 클래스를 모아 놓은 파일을 모듈이라고 함

모듈 사용
import 모듈명

미리 같은 디렉토리에 모듈명에 해당하는 코드를 저장해야함(math 같은 기본 모듈 제외)

'''

import converter

miles = converter.kilometer_to_miles(150)
print('150km = {}miles'.format(miles))

pounds = converter.grams_to_pounds(1000)
print('1000g = {}pounds'.format(pounds))
