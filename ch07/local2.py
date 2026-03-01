# print("------------------------------")
# b = 0       # 초기화
# print("b의 값은", b)
# b = 1       # 재할당
# print("b의 값은", b)

# def scope_test():
#     global a        # 지역변수 => 전역변수
#     a = 1
#     print("scope_test() 함수 안의 a 값은", a)

# a = 0
# print("scope_test() 함수 밖의 a 값은", a)
# scope_test()
# print("scope_test() 함수 호출 후 a 값은", a)

# 전역변수는 함수 내에서 읽기(read) 가능
# print("------------------------------")
# def scope_test():
#     # 지역변수 a 정의 없음
#     print("scope_test() 함수 안의 a 값은", a)

# a = 0       # 전역변수
# print("scope_test() 함수 밖의 a 값은", a)
# scope_test()
# print("scope_test() 함수 호출 후 a 값은", a)

# 하지만! "쓰기(write)"는 불가능
#  => 함수 내에서 쓰기를 하는 순간 지역변수로 처리
# global 키워드 활용시 전역변수로 쓰기 가능

# print("------------------------------")
# def scope_test():
#     # 지역변수 a 정의 없음
#     print("scope_test() 함수 안의 a 값은", a)
#     a = a + 1       # error

# a = 0       # 전역변수
# print("scope_test() 함수 밖의 a 값은", a)
# scope_test()
# print("scope_test() 함수 호출 후 a 값은", a)

print("------------------------------")
def scope_test():
    global a        # 전역변수
    a = a + 3
    print("scope_test() 함수 안의 a 값은", a)

a = 0
print("scope_test() 함수 밖의 a 값은", a)
scope_test()
print("scope_test() 함수 호출 후 a 값은", a)

print("------------------------------")
def scope_test():
    a = 0          # 지역변수
    a = a + 3
    print("scope_test() 함수 안의 a 값은", a)
    return a

a = 0
print("scope_test() 함수 밖의 a 값은", a)
a1 = scope_test()       # 전역변수
print("scope_test() 함수 밖의 a 값은", a)
print("scope_test() 함수 호출 후 a1 값은", a1)

# global 키워드
# 1. 지역변수 => 전역변수
# 2. 지역변수 생성 차단

