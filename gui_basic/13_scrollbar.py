from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480") # 가로 * 세로

frame = Frame(root)
frame.pack()

scrollbar = Scrollbar(frame)
scrollbar.pack(side="right", fill="y")

# set 이 없으면 스크롤을 내려도 다시 올라옴
listbox = Listbox(frame, selectmode="extended", height=10, yscrollcommand = scrollbar.set)

for i in range(1, 32):
    listbox.insert(END, str(i) + "일")
listbox.pack(side="left")

# listbox에 scrollbar를 적용 했듯이
# scrollbar에도 listbox를 넣어줘야 서로 작동이됨
scrollbar.config(command=listbox.yview)

root.mainloop()