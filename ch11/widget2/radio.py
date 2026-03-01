from tkinter import Tk
from tkinter import Button
from tkinter import Radiobutton
from tkinter import IntVar

oroot = Tk()     # 부모 윈도우(위젯)
oroot.geometry("400x300")

radio_value = IntVar()      # 정수형 변수 생성
# print(radio_value.get())  # 초기값 0
# radio_value.set(1)          # 정수값 설정
radio_value.set(-1)          # 아무것도 선택 안되도록 설정 방법

lunch = {0:"A런치", 1:"B런치", 2:"C런치"}

# variable => 클릭된 버튼의 정보를 저장할 변수명 설정
# value => radio_value에 저장될 데이터 지정하는 인수
orb1 = Radiobutton(oroot, text=lunch[0], variable=radio_value, value=0)
orb1.pack()
orb2 = Radiobutton(oroot, text=lunch[1], variable=radio_value, value=1)
orb2.pack()
orb3 = Radiobutton(oroot, text=lunch[2], variable=radio_value, value=2)
orb3.pack()

def buy():
    value = radio_value.get()
    # print(value)
    if value != -1:
        print(lunch[value])
    else:
        print("선택된 메뉴가 없습니다.")

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