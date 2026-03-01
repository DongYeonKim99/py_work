#1 b)
#2 d)
#3 c)
#4 c)
# #5
# def print_hello():
#     print("안녕하세요")

# #6  
# print_hello()
    
# #7
# for i in range(100):
#     print_hello()

# #8
# def greet(name = "Guest"):
#     print("Hello, ", name, "!", sep="")
# greet("Alice")

#9 함수가 정의되기 전에 함수를 호출했기 때문에

#10 20, 함수 실행 결과로 돌려주는 값으로, 함수의 종료 역할을 한다.

# 2주차
# # 문제 1)
# Numbers = [1, 2, 3, 4, 5]
# for i in Numbers:
#     print(i)

# # 문제 2)
# fruits = ['바나나', '파인애플', '복숭아', '사과', '포도']
# for fruit in fruits:
#     if fruit == "사과":
#         print("사과를 찾았습니다!")
#     else:
#         print(fruit)

# # 문제 1)
# def solution(a, b):
#     sum = a + b
#     sub = a - b
#     multi = a * b
#     return sum, sub ,multi
# print(solution(2, 3))

# 문제 2)
def fsum(num):
    sum = 0
    for i in range(1, num + 1):
        sum += i
    return sum
n = int(input("자연수 n을 입력해주세요:"))
print("1부터 자연수 n 까지의 합:", fsum(n))
