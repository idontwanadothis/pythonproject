'''
Set
    순서가 없음
    변경할 수 없음
    인덱싱 되지 않는 컬렉션
    중복값이 없음
'''

thisset = {"피카츄", "라이츄", "파이리"}
print(thisset)

#항목 가져오기
for x in thisset:
    print(x)

#값이 있는지 확인
thisset = {"피카츄", "라이츄", "파이리"}
print("피카츄" in thisset)
print("꼬부기" in thisset)
print("파이리" in thisset)

#항목 추가하기
thisset.add("꼬부기")
print(thisset)

# 다른 set 항목 추가 (중복값은 추가가 안됨)
thisset1 = {"피카츄", "라이츄", "파이리"}
thisset2 = {"꼬부기", "잠만보", "뮤츠"}
thisset1.update(thisset2)
print(thisset1)

# 항목제거
thisset = {"피카츄", "라이츄", "파이리"}
#thisset.remove("피카츄")
#print(thisset)

thisset.discard("피카츄")
print(thisset)
thisset.discard("피카츄")
print(thisset)

#비우기
thisset.clear()
print(thisset)


