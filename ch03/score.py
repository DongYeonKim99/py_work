# score = 90   # 초기화
# #score = 79   # 재할당
# if score > 80:
#     print("합격입니다.")
# else:
#     print("불합격입니다.")
# print("프로그램 종료")

# print("----------------")
# na = 21
# if na % 2 == 0 :
#     print(na, "짝수")
# else:
#     print(na, "홀수")
# print("if 문 종료 됨")

print("----------------")
tscore = 700
if tscore >= 900:
    print("당신의 토익 점수는", tscore, "점으로 상위권 점수입니다.")
elif tscore >= 700:
    print("당신의 토익 점수는", tscore, "점으로 중위권 점수입니다.")
else:
    print("당신의 토익 점수는", tscore, "점으로 하위권 점수입니다.")
print("if 문 종료됨")

# 토익 점수를 4분류 하는 프로그램
# 900이상 : 상위권
# 900미만 ~ 600이상 : 중상위권
# 600미만 ~ 300이상 : 중위권
# 300미만 : 하위권

print("----------------")
tscore = 700
if tscore >= 900:
    print("당신의 토익 점수는", tscore, "점으로 상위권 점수입니다.")
elif tscore >= 600:
    print("당신의 토익 점수는", tscore, "점으로 중상위권 점수입니다.")
elif tscore >= 300:
    print("당신의 토익 점수는", tscore, "점으로 중위권 점수입니다.")
else:
    print("당신의 토익 점수는", tscore, "점으로 하위권 점수입니다.")
print("if 문 종료됨")

# 400미만 ~ 300이상 : 중위권
# elif tscore < 400 and tscore >= 300:
#     print(tscore, "중위권")
