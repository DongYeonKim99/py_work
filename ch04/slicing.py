week = ['월', '화', '수', '목', '금', '토', '일']
print(week)
print(week[2:5])
print(week)

# 문제1: 토/일 데이터를 출력하시오.
print(week[5:7])

# 문제2: 월~목 데이터를 출력하시오.
print(week[0:4])

print('음수 인덱싱 -------------------')
print(week[-1])
print(week[-2])
print(week[-3])

print('음수 슬라이싱 -------------------')
print(week[-3:-1])      # ['금', '토']
print(week[-5:5])       # ['수', '목', '금']
# 좌 => 우
print(week[-1:4])       # []
print(week[7:5])

print('인덱스 번호 생략하는 경우 -------------------')
# 1. 시작 인덱스 생략
print(week[:5])
# 2. 끝 인덱스 생략
print(week[2:])
# 3. 모든 인덱스 생략 => 전체 데이터 대상
print(week[:])

print('-------------------')
#리스트명[start:end:step]
print(week[0:6:2])      # ['월', '수', '금']
print(week[0::3])       # ['월', '목', '일']

print(week[-1:-8:-1])