from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480") # 가로 * 세로

Label(root, text="메뉴를 선택해 주세요").pack(side="top")

Button(root, text="주문하기").pack(side="bottom")

# 메뉴 프레임
frame_burger = Frame(root, relief="solid", bd=1) # relief(모양) bd(borderwidth=너비) 외곽선 두께   
# relief 종류
# 1. flat 기본값으로 경계선이 보이지 않는다.
# 2. raised 경계 안쪽이 바깥보다 볼록하게 보인다.
# 3. sunken 경계 안쪽이 바깥보다 오목하게 보인다.
# 4. solid 경계에 단선한 선이 그어진다.
# 5. ridge 경계선만 볼록해 보인다.
# 6. groove 경계선만 오목해 보인다.
frame_burger.pack(side="left", fill="both", expand=True)

Button(frame_burger, text="햄버거").pack()
Button(frame_burger, text="치즈버거").pack()
Button(frame_burger, text="치킨버거").pack()

# 음료 프레임
frame_drink = LabelFrame(root, text="음료")
frame_drink.pack(side="right", fill="both", expand=True)

Button(frame_drink, text="콜라").pack()
Button(frame_drink, text="사이다").pack()

root.mainloop()