candies = ['딸기맛', '레몬맛', '수박맛', '박하맛', '우유맛']
print(candies)

lista = ['list', 1, 0.7, True, [1,2]]
print(lista)
print(type(lista))

print(lista[3])
print(type(lista[3]))


print('---------------')
ca = [10, 11, 21]
print(ca)
print(ca[0])
print(ca[1])
print(ca[2])
print(type(ca[0]))

print('---------------')
lista = [1, "python", 3.9, '프로그래밍', [10, 11, 21]]
print(lista)
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])
print(lista[4])

print(lista[4][0])
print(lista[4][1])
print(lista[4][2])

print('---------------')
# 값 변경하기
#리스트변수명[인덱스] = 데이터값
a = [1, 2, 3, 4, 5]
a[2] = 30
print(a)
a[3] = 40
print(a)
a[1] ='hi'
print(a)
a[4] = False
print(a)
a[0] = 3.14
print(a)

# a[5] = 'thanks'      # IndexError

