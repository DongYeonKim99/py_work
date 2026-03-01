print("------------------------------")
b = 0       # 초기화
print("b의 값은", b)
b = 1       # 재할당
print("b의 값은", b)

def scope_test():
    a = 1
    print("scope_test() 함수 안의 a 값은", a)

a = 0
print("scope_test() 함수 밖의 a 값은", a)
scope_test()
print("scope_test() 함수 호출 후 a 값은", a)

