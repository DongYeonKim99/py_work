# 선택 정렬1
# 1차 목표: [10, 21, 11, 15, 13]
ca = [21, 10, 11, 15, 13]
mina = ca[0]    # 현 최소값
minix = 0       # 현 최소값 위치(인덱스)
for sb in range(1,5,1):     # 1,2,3,4
    if mina > ca[sb]:       # 21>10 => True
        mina = ca[sb]       # mina = 10
        minix = sb

temp = ca[0]        
ca[0] = ca[minix]   
ca[minix] = temp    
print(ca)           

# 2차 목표:[10, 11, 21, 15, 13]
print("------------------------")
mina = ca[1]    # 현 최소값
minix = 1       # 현 최소값 위치(인덱스)
for sb in range(2,5,1):     # 2,3,4
    if mina > ca[sb]:       # 21>11 => True
        mina = ca[sb]       # mina = 11
        minix = sb          # minix = 2

temp = ca[1]        
ca[1] = ca[minix]   
ca[minix] = temp    
print(ca)           

# 3차 목표: [10, 11, 13, 15, 21]
print("------------------------")
mina = ca[2]    # 현 최소값
minix = 2       # 현 최소값 위치(인덱스)
for sb in range(3,5,1):     # 3,4
    if mina > ca[sb]:       # 21>13 => True
        mina = ca[sb]       # mina = 13
        minix = sb          # minix = 4

temp = ca[2]        
ca[2] = ca[minix]   
ca[minix] = temp    
print(ca)     

# 4차 목표: [10, 11, 13, 15, 21]
print("------------------------")
mina = ca[3]    # 현 최소값
minix = 3       # 현 최소값 위치(인덱스)
for sb in range(4,5,1):     # 4
    if mina > ca[sb]:       # 15>21 => False
        mina = ca[sb]       # mina = 15
        minix = sb          # minix = 3

temp = ca[3]        
ca[3] = ca[minix]   
ca[minix] = temp    
print(ca)   

print("------------------------")
ca = [21, 10, 11, 15, 13]
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
    print(ca)