from random import *



i = 0

for customer in range(1,51):
    time = randint(5,50)
    if 5 <= time <16:
        print("[o] {0}번째 손님 (소요시간 :{1}분)".format(customer,time))
        i = i+1
    else:
        print("[ ] {0}번째 손님 (소요시간 :{1}분)".format(customer,time))    

print("총 탑승 승객 : {0}손님".format(i))
   