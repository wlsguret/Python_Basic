import time
import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480") # 가로 * 세로

# progressbar = ttk.Progressbar(root, maximum=100, mode="indeterminate") # indeterminate = 불확실한
# progressbar = ttk.Progressbar(root, maximum=100, mode="determinate") # determinate = 한정된
# progressbar.start(10) # 10 ms 마다 움직임
# progressbar.pack()

# def btncmd():
#     progressbar.stop() # 작동 중지

# btn = Button(root, text="중지", command=btncmd)
# btn.pack()

p_var2 = DoubleVar()
progressbar2 = ttk.Progressbar(root, maximum=100, length=150, variable=p_var2)
progressbar2.pack()

def btncmd2():
    for i in range(1, 101):
        time.sleep(0.01) # 0.01 초 대기

        p_var2.set(i) # progress bar 의 값 설정
        progressbar2.update() # ui 업데이트 # for가 동작 할 때 마다 업데이트 /안하면 버튼 클릭 후 1~100까지 동작완료 후 보이게 됨
        print(p_var2.get())
        
btn = Button(root, text="시작", command=btncmd2)
btn.pack()

root.mainloop()