# 클래스: 가방
# 객체: 숄더백, 캐리어, 핸드백, 클러치백, 더플백
# 속성: 재질, 색, 무게, 용량, 가격, 수납개수
# 기능: 넣다, 꺼내다, 꾸미다, 보호하다

class Bag:
    # 클래스 멤버 변수
    # color = "검정색"
    # name = "shoulder"
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.data = []

    # 메서드 : 넣다
    def add(self, x):
        self.data.append(x)

    # 기능: 두번 넣다
    def addtwice(self, x):
        self.add(x)
        self.add(x)

    
shoulder = Bag("숄더백", "검정색")
print(shoulder.color)
shoulder.add("휴대폰")
print(shoulder.data)
shoulder.addtwice("돈")
print(shoulder.data)
print(shoulder.name)

print("------------------")
carrier = Bag("캐리어", "파란색")
print(carrier.color)
carrier.add("지갑")
carrier.add("전공책")
print(carrier.data)