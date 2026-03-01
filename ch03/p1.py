# 어떤 웹사이트에 로그인 하려고 한다.
# 중첩 if 문을 활용하여
# 아이디와 암호를 입력하는 프로그램을 작성하시오.
# (둘 다 일치해야 로그인 가능)

# 예시)
# 아이디를 입력하시오: kenneth
#  아이디 일치!
#  존재하지 않는 아이디!
# 암호를 입력하시오: 1234
#  로그인 성공!!
#  압호 불일치!!

user_id = "kenneth"
user_pw = "1234"

input_id = input("아이디를 입력하시오:")
input_pw = input("암호를 입력하시오:")

if input_id == user_id:
    print("아이디 일치!")
    if input_pw == user_pw:
        print("로그인 성공!!")
    else:
        print("암호 불일치!!")
else:
    print("존재하지 않는 아이디!")


# print(3==5)

# print((3==3) and (4 != 3))

# if 4 < 3:
#     print("Hello World.")
# else:
#     print("Hi, there.")

# if True:
#     if False:
#         print("1")
#         print("2")
#     else:
#         print("3")

# else:
#     print("4")

# print("5")

# num = int(input("양의 정수 하나를 입력하시오:"))
# if num >= 0:
#     if num % 2 == 0:
#         print("짝수")
#     else:
#         print("홀수")
# else: 
#     print("양의 정수를 입력하세요.")

# num = int(input("정수를 입력하시오:"))
# sum = num + 20
# if sum <= 255:
#     print(sum)
# else:
#     print("255")

# num = int(input("정수를 입력하시오:"))
# sum = num - 20
# if sum > 255:
#     print("255")
# elif sum < 0:
#     print("0")
# else: 
#     print(sum)

# hour = int(input("시(0~23)를 입력하세요:"))
# minute = int(input("분(0~59)을 입력하세요:"))
# if minute == 0:
#     print("정각 입니다.")
# else:
#     print("정각이 아닙니다.")

# score = float(input("score:"))
# if 80 < score and score <= 100:
#     print("grade is A")
# elif score > 60:
#     print("grade is B")
# elif score > 40:
#     print("grade is C")
# elif score > 20:
#     print("grade is D")
# elif score >= 0:
#     print("grade is E")
# else:
#     print("0~100 까지의 숫자를 입력하세요")

