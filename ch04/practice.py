#1
movie_rank = ['하얼빈', '무파사:라이온킹', '소방관']
print(movie_rank)

#2
movie_rank.append('위키드')
print(movie_rank)

#3
movie_rank = ['하얼빈', '무파사:라이온킹', '소방관', '위키드']
movie_rank.insert(3, '모아나2')
print(movie_rank)

#4
# movie_rank.remove('소방관')
# print(movie_rank)

del movie_rank[2]
print(movie_rank)

#5
nums = [1, 2, 3, 4, 5]
sum = 0
for i in range(len(nums)):
    sum += nums[i]
print(sum)

#6 
cook = ["피자", "김밥", "만두" , "양념치킨", "족발", "피자", "김치만두"
        , "쫄면", "쏘세지", "라면", "팥빙수", "김치전"]
print(len(cook))

#7 
t = 1,2,3,4
print(type(t))

#8
t = ('a', 'b', 'c')
list_t = list(t)
list_t[0] = 'A'
t = tuple(list_t)
print(t)
print(type(t))

#9
icecream = {'메로나': 1000, '폴라포': 1200, '빵빠레': 1800}
print(icecream)

#10
icecream = {'메로나': 1000, '폴라포': 1200, '빵빠레': 1800}
icecream['죠스바'] = 1200
icecream['월드콘'] = 1500
print(icecream)

#11
icecream['메로나'] = 1300
print(icecream)

#1주차 과제
# a = 3.14
# b = True
# c = "False"
# print(type(a),type(b),type(c))

# n1 = int(input("첫 번째 숫자를 입력하세요: "))
# n2 = int(input("두 번째 숫자를 입력하세요: "))
# print("덧셈: n1 + n2 = ", n1 + n2)
# print("뺄셈: n1 - n2 = ", n1 - n2)
# print("곱셈: n1 * n2 = ", n1 * n2)
# print("나눗셈: n1 / n2 = ", n1 / n2)

# water = 700
# if water >= 1000:
#     print("충분")
# elif water < 1000 and water >= 500:
#     print("적절")
# else:
#     print("부족")

# score = int(input("학점을 입력학세요: "))
# if score <= 100 and score >= 90 :
#     print("A학점")
# elif score >= 80 and score < 90:
#     print("B학점")
# elif score >= 70 and score < 80:
#     print("C학점")
# elif score < 70:
#     print("F학점")
# else: 
#     print("0~100사이의 숫자를 입력하세요")

# fruits =["banana", "peach", "lemon", "grape"]
# print(fruits[2])

student3 = {"나이": 22, "직업": "학생", "취미": "게임"}
student3["도시"] = "수원"
print(student3.keys())