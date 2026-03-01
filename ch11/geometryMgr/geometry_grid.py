from tkinter import Tk, Button

# 1. 위젯 생성
otk = Tk()
otk.title("배치 학습")      # 윈도우 제목 변경
otk.geometry("400x300")
obtn1 = Button(otk, text="PUSH1")
obtn2 = Button(otk, text="PUSH2")
obtn3 = Button(otk, text="PUSH3")
obtn4 = Button(otk, text="PUSH4")

# 2. 위젯 배치
obtn1.grid(row=1, column=0)
obtn2.grid(row=1, column=3)
obtn3.grid(row=0, column=2)
obtn4.grid(row=2, column=2)
# obtn3.grid(row=0, column=4, padx=80, pady=100)

otk.mainloop()

print("------------------------")