# 클래스(분류:가수) 정의
class Singer:
    # (클래스)멤버 변수
    name = "아이유"
    # 메서드
    def sing(self):
        self.name = "아이유2"   # (인스턴스)멤버변수
        print("이 밤 그날의 반딧불을 당신의 창 가까이 보낼게요~")

# 객체 생성(생성자 함수 활용)
iu = Singer()
# print(iu.name)
print(Singer.name)  # 클래스 멤버 변수 접근
iu.sing()           # 객체 기능/동작 호출
print(iu.name)      # 인스턴스 멤버 변수 접근

print("------------------------")
bts = Singer()
bts.sing()
print(bts.name)