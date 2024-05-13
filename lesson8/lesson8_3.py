import random
import pyinputplus as pyip

while True:
    min = 1
    max = 100
    count = 0
    target = random.randint(min,max)
    print(target)
    print("=========猜數字遊戲============\n")
    while True:
        count += 1
        keyin = pyip.inputInt(f"猜數字的範圍{min}~{max}:")
        print(keyin)
        if keyin == target:
            print(f"賓果!猜對了, 答案是:{target}")
            print(f"您總共猜了{count}次")
            break
        elif(keyin > target):        
            print("再小一點")
            max = keyin-1        
        elif(keyin < target):
            print("再大一點")
            min = keyin + 1
        print(f'您已經猜了{count}次')
    play_again = pyip.inputYesNo("還要繼續嗎?(y,n)")
    if play_again == 'no':
        break

print("遊戲結束")
