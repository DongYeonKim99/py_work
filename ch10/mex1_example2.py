# from 모듈명 import 클래스명,함수명,변수명
from mex1 import plus   
from mex1 import Cvalue
from mex1 import p1
from mex1 import plus as m1_plus    # 별칭 사용   

value = plus(10, 20)
print(value)

p3 = Cvalue()
print(p3.lista)
p3.add("사과")
p3.add("배")
p3.fprint()

p1.add(5)
print(p1.lista)

# 파이썬 모듈 임포트시 특정 클래스, 함수, 변수를 명시하는 이유
# 1. 코드 간결화(가독성)
# 2. 네임스페이스 충돌 방지
# 3. 기능 사용의 명확성
# 단, 실행 성능 차이는 거의 없음
