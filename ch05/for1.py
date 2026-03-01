# for 변수 in 리스트:
#     코드블록

for num in [0,1,2]:
    print('hi', num)

characters = ['앨리스', '도도새', '3월토끼']
for character in characters:
    print(character) 

print('리스트 ------------------------')
characters = ['앨리스', '도도새', '3월토끼']
for character in characters:
    pass                     # 문장을 비워두겠다, 문법적으로 문제가 없도록

print('문자열 ------------------------')
for letter in '체셔고양이':
    print(letter)

print('------------------------')
nums = [0, 1, 2]
for num in nums:
    print(num)
print(nums)

print('------------------------')
nums = [0, 1, 2]
for num in nums:
    print(num)
    print(nums)

print('튜플 ------------------------')
nums = (0, 1, 2)
for num in nums:
    print(num)

 