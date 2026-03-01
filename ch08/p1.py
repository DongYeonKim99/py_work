# #1
# a = [1, 2, 3, 4]
# a[0], a[3] = a[3], a[0]
# print(a)

# #2
# lst = [40, 20, 30, 10]
# lst[0], lst[3] = lst[3], lst[0]
# print(lst)

# #3
# arr = [3, 6, 9, 12]
# arr[0], arr[2] = arr[2], arr[0] 
# print(arr)

# #4
# a = [1,2,3]
# b = a
# print(id(a) == id(b))

# #5
# x = 42
# y = 42
# print(id(x) == id(y))

# #6 
# a = [3, 6, 7, 4, 9, 10, 13]
# even_list =[]
# odd_list =[]
# even_index = []
# odd_index = []
# for i in range(len(a)):
#     if a[i] % 2 == 0:
#         even_list.append(a[i])
#         even_index.append(i)
#     else: 
#         odd_list.append(a[i])
#         odd_index.append(i)
# # print(even_list)
# # print(odd_list)
# # print(even_index)
# # print(odd_index)
# a[even_index[0]], a[odd_index[-1]] = a[odd_index[-1]], a[even_index[0]]
# print(a) 

# #7
# a = [10, 25, 18, 30, 15]
# max = a[0]
# for i in range(1,len(a)):
#     if max < a[i]:
#         max = a[i]

# print(max)

# #9
# def selection_sort(arr):
#     for i in range(len(arr)):
#         min_idx = i
#         for j in range(i+1, len(arr)):
#             if arr[j] < arr[min_idx]:
#                 min_idx = j
#         arr[i], arr[min_idx] = arr[min_idx], arr[i]
#     return arr
# data = [64, 25, 12, 22, 11]
# print(selection_sort(data))
                           
#10
def sum_dict(dict):
    list_a = list(dict.values())
    sum = 0
    for i in range(len(dict)):
        sum += list_a[i]
    return sum
        
num_dict = {'a' : 10, 'b' : 20, 'c' : 30}
print(sum_dict(num_dict))

# a = [10, 20, 25, 35, 18]
# for i in range(0,len(a)):
#     max = a[i]
#     for j in range(i+1, len(a)):
#         if max < a[j]:
#             max = a[j]
#             a[j] = a[i]
#             a[i] = max
# print(a)
 
 