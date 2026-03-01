from tkinter import Tk, Button

# 1. 위젯 생성
otk = Tk()
otk.title("배치 학습")      # 윈도우 제목 변경
otk.geometry("400x300")
obtn1 = Button(otk, text="PUSH1")
obtn2 = Button(otk, text="PUSH2")
obtn3 = Button(otk, text="PUSH3")

# 2. 위젯 배치
obtn1.pack(side="left")
obtn2.pack(side="right")
obtn3.pack(side="top")

otk.mainloop()

print("------------------------")