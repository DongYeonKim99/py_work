print(True and True)
print(True and False)
print(False and True)
print(False and False)
print('-------------------')

print(True or True)
print(True or False)
print(False or True)
print(False or False)
print('-------------------')

print(not True)
print(not False)

print('-------------------')

print(9>4 and 3>2)
print(9<4 and 3>2)
print(9<4 or 3<2)
print(9<4 or 3>2)

print('-------------------') 
#문제 1                      
print(9>4 or 3<2 and 4>2)    

# True or (False and True)
# 논리 연산자 우선순위
# not > and > or
print(9>4 or (3<2 and 4>2))

print('-------------------')
#문제 2
print((3-5)+3<1 and 3-5>1)

# 괄호>산술(연결)>비교>논리>대입

print('-------------------')
# 비교 연산자 체이닝
# 비교 연산자를 여러개 이어서 하나의 식처럼 쓰는 문법 
#print(3<2 == False)
#print((3<2) == False)  # 괄호를 치면 체이닝이 끊어짐
#실제해석: (3<2) and (2==False)

# 2 < x < 5 : x는 2보다 크고, x가 5보다 작다
# (2 < x) and (x < 5) 

