
# 변수명 = {키1:값1, 키2:값2, 키3:값3, 키4:값4, ...}
my_dict1 = {}
print(my_dict1)
print(type(my_dict1))

my_dict2 = {0: 1, 1: -2, 2: 3.14}
print(my_dict2)
print(my_dict2[0])
print(my_dict2[1])
print(my_dict2[2])

my_dict3 = {'이름': '앨리스', '나이': 10, "시력": [1.0, 1.2]}
print(my_dict3)

print(my_dict3['이름'])
print(my_dict3.get('이름'))

print('----------------------')
# 값 추가하기
# 딕셔너리[키] = 값
clover = {'나이': 27, '직업': '병사'}
print(clover)
clover['번호'] = 9
print(clover)

print('----------------------')
print(clover)
# 값 접근하기
# 딕셔너리명[키]
print(clover['번호'])
print(clover['직업'])
# 딕셔너리.get(키)
print(clover.get('번호'))
print(clover.get('직업'))

print('----------------------')
# 이름, 나이, 성별, 원하는 데이터 1가지를 활용하여
# 딕셔너리를 생성하시오.
# 생성된 딕셔너리에 전화번호와 주소를 추가하시오.
# 생성된 데이터에 접근하시오.

my_data = {'이름': '김동연', '나이': 28, '성별': '남자', '취미': ['축구', '게임']}
print(my_data)

my_data['전화번호'] = '010-1234-5678'
my_data['주소'] = '경기도 안양시'

print(my_data)
print(my_data.get('전화번호'))

#12월 31일이 지났습니다. 나이를 +1 하여 수정하시오.
my_data['나이'] = my_data['나이'] + 1
print(my_data.get('나이'))

#print(my_data['취미'])
#print(my_data['몸무게'])
print(my_data.get('몸무게'))

print('----------------------')
print(my_data.items())

print(my_data.keys())

print(my_data.values())

# for key, value in my_data.items():
#     print(key, ":", value)


# my_dict4 = {'이름': '앨리스', '나이': {'앨리스': '주인공'}}
# print(my_dict4)

# my_dict5 = {'이름': '앨리스', '앨리스': '주인공'}
# print(my_dict5)

# 1. Mutable (뮤터블, 가변객체)
#  : 생성 후 내용을 변경할 수 있는 객체
#  주소를 변경하지 않고 같은 객체를 유지한 채, 내부 값이 변경
#  예) list, dict, set

# 2. Immutable (이뮤터블, 불변객체)
#  : 생성 후 내용을 변경할 수 없는 객체
#  값을 바꾸는 것처럼 보이지만 실제는 새 객체가 생성(주소를 새로 생성)
#  예) int, float, bool, str, tuple