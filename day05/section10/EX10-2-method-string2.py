# join 메소드
s = '-'.join('python')
print(s)

s = '+'.join(['a', 'b', 'c', 'd'])
print(s)
s = ''.join(['a', 'b', 'c', 'd'])
print(s)

# split() 메소드
s = 'Life is too short'
result = s.split()
print(result)

s = '010-1234-5678'
result = s.split('-')
print(result) #['010', '1234', '5678']

# replace()
s = 'Life is too short'
result = s.replace('short', 'long')
print(result)

# strip(), lstrip(), rstrip() 공백제거
s = '            apple'
print(s)
result = s.lstrip() #왼쪽 공백제거
print(result)
s = 'apple            '
print(s)
result = s.rstrip() #오른쪽 공백제거

# 전체 공백제거
s = ' a p p l e '
result = s.strip()
print(s)

result =s.replace(' ', '')
print(result)
