print("------------------------------")
def personC(height=170, weight=50, age=22):
    print("함수기본값설정")
    print("신장=", height, end=" ")
    print("체중=", weight, end=" ")
    print("나이=", age)
    
    
personC(168, 55)

# 1. 모든 매개변수에 기본값 설정 가능
# 2. 부분 매개변수에 기본값 설정시 뒤에서부터 설정할 것
# 3. 기본값이 있더라도 인수를 설정 가능(인수 우선 처리)
# 4. 인수 전달시 앞에서부터 설정 가능

print("------------------------------")
# 키워드 인수 : 이름을 지정해서 전달하는 인수
# 위치 인수 : 순서대로 전달하는 인수
personC(168, 55, age=33)
personC(168, age=33, weight=55)
# personC(168, 33, weight=55)   # 에러: 중복 데이터값 사용

print("hello")
print("thanks", end=" ")
print("hello", "world", end=" ", sep="/")

# 가변 위치 인수(*args) : 개수가 정해지지 않은 인수
def total(*numbers):
    print(numbers)
total(1)
total(1,2)
total(1,2,3)

# 가변 키워드 인자(**kwargs) : 이름 붙은 인수를 여러개 받음
def profile(**info):
    print(info)
profile(name="홍길동", age=553, address="한양외곽")

# 전체 정리 예제
def example(a, b=10, *args, **kwargs):
    print("a: ", a)
    print("b: ", b)
    print("args: ", args)
    print("kwargs: ", kwargs)

example(1, 2, 3, 4, x=100, y=200)