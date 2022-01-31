# _*_  coding: utf-8 _*_
'''
猜数字游戏：
计算出一个1~100之间的随机数由人来猜
计算机根据人猜的数字分别
给出提示大一点/小一点/大一点
'''
import random  #生成随机数函数

def guess_game():
    computer_num = random.randint(1,100)
    for person_num in range(1,101):
        person_num = int(input("请输入数字:"))
        if person_num > computer_num:
            print("小一点")
        elif person_num < computer_num:
            print("大一点")
        else:
            print("猜对了")
            break

if __name__ == '__main__':
    guess_game()