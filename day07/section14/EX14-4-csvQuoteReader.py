member_list = []
with open('회원명단.csv', 'rt', encoding='UTF-8') as file:
    file.readline()
    while True:
        line = file.readline() #readlines는 한 줄씩 list로 바꿔줌
        if not line:
            break
        member = line.split(',')
        member[0] = member[0].strip('"')
        member[2] = member[2].strip('\n')
        member_list.append(member)

print(member_list)


