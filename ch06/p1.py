# 함수 정의
def draw_stars(num):
    print('*' * num)

# 함수 호출
draw_stars(3)
draw_stars(2)
draw_stars(1)

# * : 문자열 반복 연산자
print("------------------------")
def fadd(pa, pb):
    pc = pa + pb
    return pc

def fsub(pa, pb):
    pc = pa - pb
    return pc

def fmul(pa, pb):
    pc = pa * pb
    return pc

def fdiv(pa, pb):
    pc = pa / pb
    return pc

na = 100
nb = 3
result1 = fadd(na, nb)
result2 = fsub(na, nb)
result3 = fmul(na, nb)
result4 = fdiv(na, nb)
print(na, "+", nb, "결괏값은", result1, "이다.")
print(na, "-", nb, "결괏값은", result2, "이다.")
print(na, "*", nb, "결괏값은", result3, "이다.")
print(na, "/", nb, "결괏값은", result4, "이다.")


# print("------------------------")
# def fadd(pa, pb):
#     pc = pa + pb
#     return pc

# def fsub(pa, pb):
#     pc = pa - pb
#     return pc

# def fmul(pa, pb):
#     pc = pa * pb
#     return pc

# def fdiv(pa, pb):
#     pc = pa / pb
#     return pc

# na = int(input("첫 번째 숫자를 입력하세요:"))
# nb = int(input("두 번째 숫자를 입력하세요:"))
# result1 = fadd(na, nb)
# result2 = fsub(na, nb)
# result3 = fmul(na, nb)
# result4 = fdiv(na, nb)

# print(na, "+", nb, "결괏값은", result1, "이다.")
# print(na, "-", nb, "결괏값은", result2, "이다.")
# print(na, "*", nb, "결괏값은", result3, "이다.")
# print(na, "/", nb, "결괏값은", result4, "이다.")

# print("------------------------")
# sta = "python example"
# lena = len(sta)
# print(lena)

# sta = "python example"
# def string_length(stb):
#     count = 0
#     for i in stb:
#         count += 1
#     return count
# lena = string_length(sta)
# print(lena)

# print("------------------------")
# def fdiv(pa, pb):
#     if pb == 0:
#         #print("0으로는 나눌 수 없다.")
#         return "0으로는 나눌 수 없다."
#     else:
#         #print(pa/pb)
#         return pa/pb 
 
# na = float(input("첫 번째 숫자를 입력하세요:"))
# nb = float(input("두 번째 숫자를 입력하세요:"))
# nc = fdiv(na, nb)
# print(na, "/", nb, "결괏값은", nc, "이다.")

# print("------------------------")

# n1 = int(input("배수의 합을 구하고자 하는 정수를 입력하세요:"))
# sum = 0
# if n1 > 0 and n1 < 10:
#     for i in range(n1, 101):
#         if i % n1 == 0:
#             sum += i
#         else: 
#             continue 
#     print("100까지", n1, "의 배수의 총합:", sum)
# else:
#     print("1부터 9까지의 정수를 입력하세요.")



# print("------------------------")
# def funca(num):
#     sum = 0
#     if num > 0 and num < 10:
#         for i in range(1, 101):
#             if i % num == 0:
#                 sum += i
#             else: 
#                 continue 
#         return sum
#     else:
#         print("1부터 9까지의 정수를 입력하세요.")

# n1 = int(input("배수의 합을 구하고자 하는 정수를 입력하세요:"))
# total = funca(n1)
# print("100까지", n1, "의 배수의 총합:", total)

