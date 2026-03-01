# 두 데이터(na 와 nb)를 스왑하는 합수를 작성하시오.
def swap_func(pa, pb):
    temp = pa
    pa = pb
    pb = temp
    # return 반환값

na = 10
nb = 11

print("na값:", na, end =" ")
print("nb값:", nb)

swap_func(na, nb)

print("na값:", na, end =" ")
print("nb값:", nb)

print("------------------------------")
def swap_func(pa, pb):
    temp = pa
    pa = pb
    pb = temp
    print("함수 내 pa 값:", pa, end =" ")
    print("함수 내 pb 값:", pb)
    return pa, pb
    
na = 10
nb = 11

print("na값:", na, end =" ")
print("nb값:", nb)

na, nb = swap_func(na, nb)

print("na값:", na, end =" ")
print("nb값:", nb)

