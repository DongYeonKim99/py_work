# for num in [3, 1, 2]:
#     print(num)

# print('------------------------')

# for num in range(2):
#     print(num)

# print('------------------------')
# clovers = ['클로버1', '클로버2', '클로버3']
# for clover in clovers:
#     print(clover)

# print('------------------------')
# clovers = ['클로버1', '클로버2', '클로버3']
# for clover in range(3):
#     print(clovers[clover])

# print('------------------------')
# count = 0
# while count < 3:
#     print(count)
#     count += 1

# print('------------------------')
# count = 1
# while count < 4:
#     count += 1
#     print(count)
    
# print('------------------------')
# count = 0
# while count <= 5:
#     if count % 2 !=0:
#         print(count)
#     count += 1
    
# print('------------------------')
# price = 0
# while price != -1:
#     price = int(input('가격을 입력하세요 (종료:-1): '))
#     if price > 10000:
#         print("너무 비싸요.")
#     elif price > 5000:
#         print("괜찮은 가격이네요.")
#     elif price > 0:
#         print("정말 싸요.")

# print('------------------------')
# for num in range(101):
#     if num % 3 == 0:
#         print(num)

# print('------------------------')
# for num in range(1,11):
#     if num % 3 == 0:
#         continue
#     print(num)

# print('------------------------')
# sum = 0
# num = int(input("총합을 구하려는 수를 입력하세요."))
# for i in range(1,num+1):
#     sum += i
# print("1부터", num, "까지의 총합은", sum, "이다.")

# print('------------------------')
# for sb in range(1, 11, 1):
#     total = 0
#     total += sb
# print(total)


# print('------------------------')
# total = 0
# for sb in range(1, 11, 1):
#     total += sb
# print(total, end=" ")
# print("끝")

# print('------------------------')
# total = 0
# for sb in range(1, 11, 1): 
#     total += 1
# print(total)

# print('------------------------')
# for sb in range(1, 11, 1):
#     total = 0
#     total += 1
# print(total)

# print('------------------------')
# sum = 0
# i = 1
# num = int(input("총합을 구하려는 수를 입력하세요."))
# while i <= num:
#     sum += i
#     i += 1
# print("1부터", num, "까지의 총합은", sum, "이다.")

# print('------------------------')
# sum = 0
# i = 1
# num = int(input("총합을 구하려는 수를 입력하세요."))
# while True:
#     if i > num:
#         break
#     sum += i
#     i += 1
# print("1부터", num, "까지의 총합은", sum, "이다.")

# print('------------------------')
# sum = 0
# n1 = int(input("계산할 첫 번째 수를 입력하시오:"))
# n2 = int(input("계산할 마지막 수를 입력하시오:"))
# if n1 < n2:
#     for i in range(n1,n2+1):
#         sum += i
# else:
#     for i in range(n2,n1+1):
#         sum += i

# print(n1, "부터", n2, "까지의 총합은", sum, "이다.")

# print('------------------------')
# sum = 0
# n1 = int(input("계산할 첫 번째 수를 입력하시오:"))
# n2 = int(input("계산할 마지막 수를 입력하시오:"))

# if n1 < n2:
#     i = n1
#     while True:
#         if i > n2:
#             break
#         sum += i
#         i += 1
# else:
#     i = n2
#     while True:
#         if i > n1:
#             break
#         sum += i
#         i += 1

# print(n1, "부터", n2, "까지의 총합은", sum, "이다.")

# print('------------------------')
# sum = 0
# n1 = int(input("계산할 첫 번째 수를 입력하시오:"))
# n2 = int(input("계산할 마지막 수를 입력하시오:"))
# if n1 < n2:
#     for i in range(n1,n2+1):
#         if i % 3 == 0:
#             sum += i
#         else:
#             continue
# else:
#     for i in range(n2,n1+1):
#         if i % 3 == 0:
#             sum += i
#         else:
#             continue
# print(n1, "부터", n2, "까지 3의 배수의 총합은", sum, "이다.")

# print('------------------------')
# sum = 0
# n1 = int(input("계산할 첫 번째 수를 입력하시오:"))
# n2 = int(input("계산할 마지막 수를 입력하시오:"))

# if n1 < n2:
#     i = n1
#     while True:
#         if i > n2:
#             break
#         if i % 3 == 0:
#             sum += i
#             i += 1
#         else: 
#             i += 1
#             continue
        
# else:
#     i = n2
#     while True:
#         if i > n1:
#             break
#         if i % 3 == 0:
#             sum += i
#             i += 1
#         else: 
#             i += 1
#             continue

# print(n1, "부터", n2, "까지 3의배수의 총합은", sum, "이다.")


# print('------------------------')
# total = 1
# for i in range(1,10):
#     total = 1*i
#     print("1 x", i, "=", total)

# print('------------------------')
# for i in range(1,6):
#     for j in range(1,10):
#         print(i ,"x", j ,"=", i*j)
#     print()
 
#1
# 과일 = ["사과", "귤", "수박"]
# for 변수 in 과일:
#     print(변수)
    
#2
# for i in range(1,4):
#     변수 = 10 * i
#     print(변수)
 
#3
# price_list = [100, 200, 300]
# for price in price_list:
#     total = price + 10
#     print(total)

#4
# list = ['dog', 'cat', 'parrot']
# for animal in list:
#     print(animal, len(animal))

#5
# list = ['가', '나', '다', '라']
# for letter in list[1:]:
#     print(letter)

#6
# list = [3, -20, -3, 44]
# for i in list:
#     if i >= 0:
#         continue
#     else:
#         print(i)

#7
# for i in range(2002,2051,4):
#     print(i)

#8
#2번

#9
# i = 1
# sum = 0
# while i < 101:
#     sum += i
#     i += 1
# print("1부터 100까지의 자연수의 합:", sum)

#10
# for i in range(1,31):
#     if i % 2 == 0:
#         print(i, ":짝수")
#     else: 
#         print(i, ":홀수")

#11
odd = []
even = []
for i in range(1,31):
    if i % 2 == 0:
        even.append(i)
    else: 
        odd.append(i)

print("홀수:", odd)
print("짝수:", even)
