
# # from tkinter import *
# from tkinter import Tk, Button

# def order():
#     print("주문하세요")

# otk = Tk()
# otk.geometry("400x300")
# obtn = Button(otk, text="주문", command=order)
# obtn.pack()
# otk.mainloop()

# print("------------------------")
# # 이벤트 바인드 방식2 : bind() 함수 사용

# from tkinter import Tk, Button

# # event: 이벤트 정보 객체(자동 전달)
# # def 함수명(event):
# #     코드블록

# def order(event):
#     print("주문하세요")

# otk = Tk()
# otk.geometry("400x300")
# obtn = Button(otk, text="주문")

# # 객체명.bind("이벤트 문자열", 함수객체)
# obtn.bind("<Button-1>", order)

# obtn.pack()
# otk.mainloop()

print("------------------------")
from tkinter import Tk, Button, Label

def msg():
    print("start tkinter")

otk = Tk()
otk.geometry("400x300")

olabel = Label(otk, text="시작레이블")
olabel.pack(side = 'top')

obtn = Button(otk, text="시작버튼", command=msg)
obtn.pack(side='bottom')

otk.mainloop()