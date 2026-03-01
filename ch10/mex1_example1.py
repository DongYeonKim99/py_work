# import 모듈명
import mex1     # 모듈 불러오기
import mex1 as m1    # 별칭(alias) 사용

print("mex1_example.py 실행")

p2 = mex1.Cvalue()
p2.add(11)
p2.add(21)
p2.add(31)
print(p2.lista)
p2.fprint()

# mex1.py 함수 활용
value = mex1.plus(10, 20)
print(value)

# mex1.py 변수 활용
# print(mex1.p1)
# print(mex1.p1.lista)
# mex1.p1.add(4)
# mex1.p1.fprint()

# 내장 변수(메인모듈): __main__
print(__name__)    
