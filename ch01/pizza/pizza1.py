import tkinter as tk
from tkinter import messagebox

# 피자 메뉴와 가격
pizza_menu = {
    "페퍼로니 피자": 3000,
    "치즈 피자": 2500,
    "불고기 피자": 3500
}

def order():
    total_price = 0
    order_list = []

    for pizza, var in check_vars.items():
        if var.get() == 1:
            qty = qty_entries[pizza].get()
            if qty.isdigit() and int(qty) > 0:
                price = pizza_menu[pizza] * int(qty)
                total_price += price
                order_list.append(f"{pizza} x {qty}조각")
            else:
                messagebox.showwarning("입력 오류", f"{pizza} 수량을 올바르게 입력하세요.")
                return

    if not order_list:
        messagebox.showwarning("주문 오류", "피자를 하나 이상 선택하세요.")
        return

    order_text = "\n".join(order_list)
    messagebox.showinfo(
        "주문 확인",
        f"주문 내역:\n{order_text}\n\n총 가격: {total_price}원"
    )

# 메인 창
root = tk.Tk()
root.title("조각 피자 주문 프로그램")
root.geometry("350x300")

tk.Label(root, text="🍕 조각 피자 주문", font=("Arial", 14, "bold")).pack(pady=10)

frame = tk.Frame(root)
frame.pack()

check_vars = {}
qty_entries = {}

# 메뉴 UI 생성
for pizza, price in pizza_menu.items():
    row = tk.Frame(frame)
    row.pack(anchor="w", pady=5)

    var = tk.IntVar()
    chk = tk.Checkbutton(row, text=f"{pizza} ({price}원)", variable=var)
    chk.pack(side="left")

    tk.Label(row, text="수량:").pack(side="left", padx=5)
    entry = tk.Entry(row, width=5)
    entry.pack(side="left")

    check_vars[pizza] = var
    qty_entries[pizza] = entry

tk.Button(root, text="주문하기", command=order, bg="orange").pack(pady=20)

root.mainloop()
