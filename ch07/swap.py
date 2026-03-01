# 변수간 데이터 스왑1
na = 10
nb = 11
print("na값:", na, end =" ")
print("nb값:", nb)
temp = na
na = nb
nb = temp
print("na값:", na, end =" ")
print("nb값:", nb)

print("---------------------")
# 변수간 데이터 스왑2
na = 10
nb = 11
print("na값:", na, end =" ")
print("nb값:", nb)
na, nb = nb, na
print("na값:", na, end =" ")
print("nb값:", nb)


