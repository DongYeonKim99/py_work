# (조건식에 사용된)변수 초기화
# while 조건(식):
#     코드블록
#     증감식(while문을 빠져나올수 있도록)

for num in range(3):
    print('안녕 거북이', num)

print('------------------------')

num = 0
while num < 3:
    print('안녕 거북이', num)
    num = num + 1

# print('------------------------')
# while True:
#     print("Ctrl + C를 누르세요.")


print('------------------------')
a = 10
b = 5
a = a - b
print(a)
a = 10
b = 5
a -= b
print(a)

print('------------------------')
stra = "파이썬"
strb = "프로그래밍"
stra = stra + strb
print(stra)

stra = "파이썬"
strb = "프로그래밍"
stra += strb
print(stra)


