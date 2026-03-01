# print("첫 번째 정수를 입력하세요:")
# ra = input()
# rb = input("두 번째 정수를 입력하세요:")
# rc = ra + rb
# print(ra, "+", rb, "값은", rc, "이다")

ra = input("첫 번째 정수를 입력하세요:")   # 20
rb = input("두 번째 정수를 입력하세요:")   # 5
print(type(ra))   # str '20'
print(type(rb))   # str '5'

rc = ra + rb        # 연결연산자
print(ra, "+", rb, "값은", rc, "이다")

print("--------------")
ra = int(ra)      # '20' => 20
rb = int(rb)      # '5' => 5
print(type(ra))   # int 20
print(type(rb))   # int 5

rc = ra + rb      # 산술연산자
print(ra, "+", rb, "값은", rc, "이다")

rc = ra % rb      # 산술연산자
print(ra, "%", rb, "값은", rc, "이다")

# ra = int(input("첫 번째 정수를 입력하세요:"))
# rb = int(input("두 번째 정수를 입력하세요:"))
# rc = ra + rb
# print(type(ra), type(rb), type(rc))
# print(ra, "+", rb, "값은", rc, "이다")

#리터럴(literal): 그 데이터(값) 자체
# 숫자 리터럴 : 10, 3.14
# 문자열 리터럴 : "python", 'hi'
 