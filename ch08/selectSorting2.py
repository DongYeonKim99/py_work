# 함수 정의 및 호출
def fselsort(ca):
    for sa in range(0,4,1):
        mina = ca[sa]    
        minix = sa       
        for sb in range(sa+1,5,1):
            if mina > ca[sb]:
                mina = ca[sb]
                minix = sb
    
        temp = ca[sa]
        ca[sa] = ca[minix]
        ca[minix] = temp
        #print(ca)
    return ca

ca = [21, 10, 11, 15, 13]
ca = fselsort(ca)
ca1 = [31, 10, 20, 9, 12]
ca1 = fselsort(ca1)
print(ca)
print(ca1)

