# 함수 정의는 호출할 때만 실행
# 호출한 함수 종료시 호출 위치로 되돌아온다.

def funca():
    print("funca 함수 호출")

def funcb():
    funca()
    print("funcb 함수 호출")

def funcc():
    funcb()
    print("funcc 함수 호출")

funcc()

print("------------------------")
# 컴퓨터는 위에서 아래로 코딩을 기억하고 계획
def funcb():
    funca()
    print("funcb 함수 호출")

def funcc():
    funcb()
    print("funcc 함수 호출")

def funca():
    print("funca 함수 호출")

funcc()

print("------------------------")
# 함수에 전달된 두 인수의
# 뺄셈 연산을 수행하는 함수를 작성하시오.
# 결과 값을 반환하고 출력하시오.

def fsub(pa, pb):
    pc = pa - pb
    return pc

na = 10
nb = 20
nc = fsub(na, nb)
print(na, "-", nb, "결괏값은", nc, "이다.")

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

print(fadd(100,3))
print(fsub(100,3))
print(fmul(100,3))
print(fdiv(100,3))

