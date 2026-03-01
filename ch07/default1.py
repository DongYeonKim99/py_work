# def 함수명(매개변수1=기본값1, 매개변수2=기본값2, ...):
#     코드블록
#     return 반환값

# 함수명(인수1, 인수2, ...)

# 매개변수1 = 인수1
# 매개변수2 = 인수2

print("------------------------------")
def persona(width, height):
    print("함수디폴드값없음, width=", width, "height=", height)

def personb(width=4, height=3):
    print("함수디폴드값없음, width=", width, "height=", height)

persona(10, 20)
# persona()     # 인수가 없어서 에러 발생
persona(30, 40)
personb()       # 인수가 없어도 기본값으로 설정
personb(50, 60) # 기본값보다 인수의 우선순위 높음

