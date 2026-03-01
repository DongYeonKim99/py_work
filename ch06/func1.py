# # 함수 정의(생성) 
# def 함수명([매개변수1, 매개변수2, ...]):
#     코드블록
#     [return 반환값]

# # 함수 호출(사용)
# 함수명([인수1,인수2, ...])

def my_func():
    print("토끼야 안녕!")

my_func()

# 가변 인자
# : 여러 개의 인수를 튜플로 묶어서 입력
# def print(*object):
#     코드블록
# print(10)
# print(10, "hi")

print("-------------------------")
def fhello():
    print("매개변수 없는 함수 호출하기")
    print("토끼야 안녕!")
    print("거북아 안녕!")
    print("코끼리야 안녕!")

fhello()
fhello()
fhello()

print("-------------------------")
# na = 10
# nb = 11
# nc = na + nb
# print(na, "+", nb, "=", nc)

def funca(na, nb):
    nc = na + nb
    print(na, "+", nb, "=", nc)

funca(10, 11)
funca(20, 21)
funca(30, 31)
# func(10)      # 인수 개수 불일치

print("-------------------------")
def add (num1, num2):   
    return num1 + num2

print(add(2,3)) 

print("-------------------------")
def add (num1, num2):
    sum = num1 + num2
    return sum

sum1 = add(2,3)
print(sum1)