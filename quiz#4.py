from random import *

st = range(1,21)
st = list(st)
shuffle(st)
chicken = st.pop()
coffee = sample(st,3)
coffee.sort


print("-- 당첨자 발표 --\n치킨 당첨자 :",chicken)
print("커피 당첨자 :",coffee,"\n-- 축하합니다 --")