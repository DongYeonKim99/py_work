# 값 추가
listc = []          # 빈 리스트
print(listc)
listc.append(300)
print(listc)
listc.append("파이썬")
print(listc)
listc.append(3.7)
print(listc)

print('--------------------------')
# 값 제거
subject = ['국어', '수학', '영어', '국사']
print(subject)
subject.append('영어')
print(subject)
subject.remove('영어')
print(subject)

# sub1 = input("과목을 입력하시오: ")
# subject.append(sub1)
# print(subject)

print('--------------------------')
clovers = ['클로버1', '클로버2', '클로버3']
print(clovers[1])
del clovers[1]
print(clovers)
print(clovers[1])
del clovers[1]
print(clovers)

print('--------------------------')
# 특정 위치에 값 추가
clovers = ['클로버1', '클로버2', '클로버3']
clovers.insert(1, '클로버4')
print(clovers)

# 클로버 5를 리스트의 맨 앞에 추가하시오.
clovers.insert(0, '클로버5')
print(clovers)

# 여러 값 추가
clovers.extend(['클로버6', '클로버7'])
print(clovers)

