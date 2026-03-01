clovers = ('클로버1', '하트2', '클로버3')
print(clovers[1])
print(type(clovers))

my_tuple1 = ()
print(my_tuple1)
print(type(my_tuple1))

my_tuple2 = (1, -2, 3.14, True, "hi", [1,2])
print(my_tuple2)

my_tuple3 = 1, -2, 3.14, True, "hi", [1,2]
print(my_tuple3)
print(type(my_tuple3))

# my_tuple3[3] = False
# print(my_tuple3)

my_int = (1)
print(my_int)
print(type(my_int))

my_tuple = (1,)
print(my_tuple)
print(type(my_tuple))

my_tuple11 = "hi",
print(my_tuple)
print(type(my_tuple11))

# 튜플끼리 + 연결 연산 가능
t1 = (1,2)
t2 = (3,4)
t3 = t1 + t2
print(t3)

print("---------------------")
# 튜플을 수정할 경우
a = (1, 2, 3)
print(type(a))
b = list(a)
print(type(b))
# a[0] = 7
b[0] = 7
print(b)

c = tuple(b)
print(type(c))

print("---------------------")
a = (1, 2, 3,[4,7])
print(type(a))
print(a)

# a[3] = [5,8]
a[3][0] = 5
a[3][1] = 8
print(a)

d = [1,2],
print(d)
print(type(d))
d[0][0] = 3
d[0][1] = 4
print(d)

print("---------------------")
e = [1,2]
print(e)
print(type(e))

f = [1,2],
print(f)
print(type(f))