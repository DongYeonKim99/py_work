# 엔트리 위젯
from tkinter import Tk, Label, Entry
from tkinter import StringVar   # 문자열 변수 

# 1. 위젯 생성
otk = Tk()
otk.geometry("400x300")

# (문자열) 변수 값 위젯과 연결 가능
ostring = StringVar()
# textvariable: 값 변화 자동 반영
oentry = Entry(otk, textvariable=ostring)
olabel = Label(otk, textvariable=ostring)


# 2. 위젯 배치
oentry.pack()
olabel.pack()


otk.mainloop()

print("------------------------")