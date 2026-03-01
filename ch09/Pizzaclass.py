# # 클래스 정의
# class 클래스명:
#     # 멤버 변수(=필드)
#     변수명 = 데이터값
#     # 멤버 함수(=메서드)
#     def 함수명(self, 매개변수, ...):
#         # 멤버 변수
#         self.변수명 = 데이터값
#         return 반환값

# # 객체 생성(생성자함수 사용)
# 객체변수명 = 클래스명()

# # 객체 접근
# 객체변수명.변수명
# 객체변수명.함수명(인수1, ...)

# 빈 클래스 작성법
# class 클래스명:
#     pass

class Pizzaclass:
    # 멤버 변수(=필드)
    # 변수명 = 데이터값  # 생략가능

    # 멤버 함수(=메서드) : 주문하다
    def order(self):
        # 멤버 변수
        print("주문하다.")
        self.kind = 10
        # return 반환값  # 생략가능
        

# 객체 생성(생성자함수 사용)
combo = Pizzaclass()     # 객체 생성
combo.order()            # 멤버 함수 사용
print(combo.kind)        # 멤버 변수 접근

potato = Pizzaclass()
potato.order()
print(potato.kind)


