# print("-----------------------")
# x = 10
# def fadd(num):
#     b = x + num
#     print("변수x값:", x)
#     print("변수b값:", b)

# fadd(10)

# print("-----------------------")
# x = 10
# def fadd(num):
#     x = x + num
#     print("변수x값:", x)

# fadd(10)

# print("-----------------------")
# x = 10
# def fadd(num):
#     global x
#     x= x + num
#     print("변수x값:", x)


# fadd(10)
# print("변수x값:", x)

# #3 
# def calculate_area(length, width=10):
#     return length*width
# print(calculate_area(5))
# print(calculate_area(5,20))

# #4
# def add_numbers(a, b):
#     return a + b
# print(add_numbers(10, 20))

# #5
# def inner_function(x,y):
#     return x + y

# def outer_function(x,y):
#     return inner_function(x,y)

# add_10 = outer_function(10, 5)
# print(add_10)

# #6
# def add_numbers(a,b):
#     global result
#     result = a + b
    
# add_numbers(10,20)
# print(result)

# #7
# def message():
#     print("A")
#     print("B")
# message()
# print("C")
# message()

# #8
# print("A")
# def message():    
#     print("B")
# print("C")
# message()

# #9
# def check_odd_even(num):
#     if num % 2 == 0:
#         return "Even"
#     else:
#         return "Odd"
    
# print(check_odd_even(4))
# print(check_odd_even(7))

#10
def calculate_average(Num_list):
    sum = 0
    avg = 0
    for num in Num_list:
        sum += num
    avg = sum / len(Num_list)
    return avg

num_list = [10, 20, 30, 40, 50, 60]
average = calculate_average(num_list)
print("평균:", average)

