def fplusminus(arg):
    if arg > 0:
        return "plus"
    elif arg < 0:
        return "minus"
    
stra = fplusminus(0)
print(stra)

result1 = fplusminus(1)
print(result1)

print(fplusminus(-2))

# return이 없으면 함수 출력결과는 None 반환

# None : 값이 없다, 아직 정해지지 않았다.

print("----------------------")
# 1. 인수가 0인 경우, "zero" 문자열을 반환하시오.
# 2. 인수로 전달 받은 값도 함께 반환하시오.
# 예) 양수인 경우, "plus", 숫자
#     음수인 경우, "minus", 숫자
#    0인 경우, "zero", 0
def fplusminus(arg):
    if arg > 0:
        return "plus", arg
    elif arg < 0:
        return "minus", arg
    else:
        return "zero", arg
    
stra, num = fplusminus(0)
print(stra, num, sep=',')

stra, num = fplusminus(-3)
print(stra, num, sep=',')

stra, num = fplusminus(14)
print(stra, num, sep=',')

# 다음 프로그램을 동작하도록 수정하시오
#  처리 결과를 출력하시오
#  함수의 기능은 무엇인가요? 절댓값 만들기

def myabs(arg):
    if(arg < 0):
        result = arg * -1
    else:
        result = arg
    return result

print(myabs(10))

