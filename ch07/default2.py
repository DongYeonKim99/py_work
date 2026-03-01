print("------------------------------")
def persona(width, height):
    print("함수디폴드값없음, width=", width, "height=", height)

def persona():
    print("매개변수 없는 함수")

def personb(width=4, height=3):
    print("함수디폴드값없음, width=", width, "height=", height)

#persona(10, 20) #인수가 없어야 동작
persona()     # 인수가 없어서 에러 발생
personb()       # 인수가 없어도 기본값으로 설정

# 동일한 이름의 함수가 있으면 아래에 있는 함수의 우선순위가 높음
# 나중에 정의된 함수가 기존에 있던 함수를 덮어쓴다고 생각
# 하지만 동일한 이름의 함수 정의 의미x


