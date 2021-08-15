import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480") # 가로 * 세로

values = [str(i) + "일" for i in range(1, 32)]
# 텍스트를 입력 할 수 있음 (설정하지 않은 값을 쓸 수 있음)
combobox =ttk.Combobox(root, height=5, values=values)
combobox.pack()
combobox.set("카드 결제일") # 최초 목록 제목 설정

# 읽기 전용 (설정된 값만 선택가능)
readonly_combobox =ttk.Combobox(root, height=10, values=values, state="readonly")
readonly_combobox.current(0) # 최초 목록 0번째 인덱스 값 선택
readonly_combobox.pack()

def btncmd():
    print(combobox.get())
    print(readonly_combobox.get())

btn = Button(root, text="선택", command=btncmd)
btn.pack()

root.mainloop()