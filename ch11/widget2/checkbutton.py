from tkinter import Tk
from tkinter import Button
from tkinter import Checkbutton
from tkinter import BooleanVar

oroot = Tk()     # 부모 윈도우(위젯)
oroot.geometry("400x300")

coffee = {0:"아메리카노", 1:"라떼", 2:"카푸치노", 3:"에스프레소"}

check_value = {}
for i in range(len(coffee)):
   check_value[i] = BooleanVar()
   ocheckbutton = Checkbutton(oroot, text=coffee[i], variable=check_value[i])
   ocheckbutton.pack()

# check_value[0].set(True)

# check_value[0] = BooleanVar()       # 불리언 값(True/False) 저장
# check_value[1] = BooleanVar()
# check_value[2] = BooleanVar()
# check_value[3] = BooleanVar()


# value = check_value[0].get()
# print(value)


# ocheckbutton1 = Checkbutton(oroot, text=coffee[0], variable=check_value[0])
# ocheckbutton1.pack()
# ocheckbutton2 = Checkbutton(oroot, text=coffee[1], variable=check_value[1])
# ocheckbutton2.pack()
# ocheckbutton3 = Checkbutton(oroot, text=coffee[2], variable=check_value[2])
# ocheckbutton3.pack()
# ocheckbutton4 = Checkbutton(oroot, text=coffee[3], variable=check_value[3])
# ocheckbutton4.pack()


def buy():
    for i in check_value:
        if check_value[i].get() == True:
            print(coffee[i])
    # if check_value[0].get() == True:
    #     print(coffee[0])
    # if check_value[1].get() == True:
    #     print(coffee[1])
    # if check_value[2].get() == True:
    #     print(coffee[2])
    # if check_value[3].get() == True:
    #     print(coffee[3])
 
obtn = Button(oroot, text="주문", command=buy)
obtn.pack()

oroot.mainloop()

# # 대략적인 IntVar 클래스의 get(), set() 구현
# class IntVar():
#     def __init__(self):
#         self.value = 0
#     def set(self, value):
#         self.value = value
#     def get(self):
#         return self.value