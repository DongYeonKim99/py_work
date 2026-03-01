count = 0
while count < 3:
    count = count + 1
    if count == 2:
        continue
    print(count)
print("반복문이 종료되었습니다.")

print('------------------------')
count = 0
while count < 3:
    count += 1
    if count == 2:
        break
    print(count)
print("반복문이 종료되었습니다.")

print('------------------------')
for j in range(5):
    for i in range(10):
        print("*", end="")
    print()

print('------------------------')
print('**********')
print('**********')
print('**********')
print('**********')
print('**********')

print('------------------------')
for i in [1,2,3,4,5]:
    print("*", end="")
    print("*", end="")
    print("*", end="")
    print("*", end="")
    print("*", end="")
    print("*", end="")
    print("*", end="")
    print("*", end="")
    print("*", end="")
    print("*", end="")
    print(end="\n")
