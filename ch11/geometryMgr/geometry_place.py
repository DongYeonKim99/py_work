from tkinter import Tk, Button

# 1. 위젯 생성
otk = Tk()
otk.title("배치 학습")      # 윈도우 제목 변경
otk.geometry("400x300")
obtn1 = Button(otk, text="PUSH1")
obtn2 = Button(otk, text="PUSH2")
obtn3 = Button(otk, text="PUSH3")

# 2. 위젯 배치
obtn1.place(x=10, y=60)
obtn2.place(x=140, y=60)
obtn3.place(x=80, y=10)
# obtn3.grid(row=0, column=4, padx=80, pady=100)

otk.mainloop()

print("------------------------")
# ** 배치 매니저 혼합 사용 주의사항
# pack()과 grid() 혼합 사용 불가
# grid()와 place() 혼합 사용 불가
