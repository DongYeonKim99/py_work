
# # super class(부모)
# class 부모클래스명:
#     # 멤버변수
#     # 메서드

# # sub class(자식)
# class 자식클래스명(부모클래스명):
#     # 멤버변수
#     # 메서드

# super class(부모)
class Human:
    # 멤버변수(속성)
    eyes = 2 
    nose = 1
    mouth = 1

    # 메서드(기능/동작)
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"이름:{self.name}")
        print(f"나이:{self.age}")

    def eat(self):
        print('먹다')

    def sleep(self):
        print('자다')

    def talk(self):
        print('말하다')

# sub class(자식)
class Student(Human):
    # 멤버변수(속성)
    # 메서드(기능/동작)
    def __init__(self, name, age, studentNum):
        # self.name = name
        # self.age = age
        super().__init__(name, age)
        self.studentNum = studentNum

    def introduce(self):
        # print(f"이름:{self.name}")
        # print(f"나이:{self.age}")
        super().introduce()
        print(f"학번:{self.studentNum}")

    def study(self):
        print("공부하다")


lee = Human("이수근", 49)
lee.introduce()
lee.eat()
lee.sleep()
print("코 개수:", lee.nose)

print("-----------------------")

student1 = Student("휘석", 28, 20260226)
student1.introduce()
student1.study()
student1.eat()
student1.sleep()
print("눈 개수:", student1.eyes)

print("-----------------------")
kim = Student("창모", 27, 20260225)
kim.introduce()
kim.study()
print("학번:", kim.studentNum)