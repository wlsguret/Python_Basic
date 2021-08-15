import time
import keyboard
from PIL import ImageGrab

def screenshot():
    # 2020년 12월 31일 15시 50분 10초 -> _20201231_155010
    curr_time = time.strftime("_%Y%m%d_%H%M%S")
    img = ImageGrab.grab()
    img.save("image{}.png".format(curr_time)) # ex) image_20201231_155010.png

keyboard.add_hotkey("F9", screenshot) # 사용자가 F9 키를 누르면 스크린 샷 저장

keyboard.wait("esc") # 사용자가 esc 를 누를 때까지 프로그램 수행