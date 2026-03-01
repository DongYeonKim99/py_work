# #3
# class Phone:
#     pass

# #4
# my_phone = Phone()

# #5
# class Phone:
#     def __init__(self):
#         print("휴대폰 생성")

# my_phone = Phone()

# #6
# class Phone:
#     def __init__(self, company, made_year, color):
#         print("휴대폰 생성")

# my_phone = Phone("삼성", 2026, "검정")
    
# #7
# class Phone:
#     def __init__(self, company, made_year, color):
#         print("휴대폰 생성")
#         self.company = company
#         self.made_year = made_year
#         self.color = color

# my_phone = Phone("삼성", 2026, "검정")
# print("제조사:", my_phone.company)
# print("출고년도:", my_phone.made_year)
# print("색상:", my_phone.color)

# #8
# class Phone:
#     def __init__(self, company, made_year, color):
#         print("휴대폰 생성")
#         self.company = company
#         self.made_year = made_year
#         self.color = color

#     def info(self):
#         print("제조사:", self.company)
#         print("출고년도:", self.made_year)
#         print("색상:", self.color)

# my_phone = Phone("삼성", 2026, "검정")
# my_phone.info()

#9
class Phone:
    def __init__(self, company, made_year, color):
        print("휴대폰 생성")
        self.company = company
        self.made_year = made_year
        self.color = color

    def info(self):
        print("제조사:", self.company)
        print("출고년도:", self.made_year)
        print("색상:", self.color)

    def setinfo(self, set_company, set_made_year, set_color):
        self.company = set_company
        self.made_year = set_made_year
        self.color = set_color


my_phone = Phone("삼성", 2026, "검정")
my_phone.info()
my_phone.setinfo("LG", 2025, "블루")
my_phone.info()