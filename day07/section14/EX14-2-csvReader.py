'''
CSV(comma-seperated values)
    필드의 쉼표(,)로 구분한
    텍스트 데이터 파일이다
'''
student_list = []
with open('학생명단.csv', 'rt', encoding='UTF-8') as file:
    file.readline() # 첫번째 제거
    while True: #한줄씩 읽고 날림
        line = file.readline()
        if not line:
            break
        student = line.split(',') #',' 구분 리스트로 변환
        student_list.append(student) # 리스트 안에 리스트 추가
print(student_list)


