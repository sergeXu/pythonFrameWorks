# coding=utf-8

import random


# guess number game
def guessOnce(num, result):
    #	print "guessOnce: "+str(num)+ " "+str(result)
    is_right = (int(num) == int(result))
    if is_right:
        print ("#" * 3 + "_" * 30 + "#" * 3)
        print ("猜正确了!!! 你赢了！！")
        print ("数字是 " + str(num))
        # print ("#"*3+"_"*30+"#"*3)
        return is_right
    elif int(num) < int(result):
        print ("数值太小了")
        return is_right
    else:
        print ("数值太大了")
        return is_right


def guessStart():
    print ("*" * 70)
    isRight = False;
    #	max_num = raw_input("输入最大值整数范围:\n")
    max_num = input("输入最大值整数范围:\n")
    while (int(max_num) <= 0):
        print ("数字不合法")
        max_num = input("输入最大值整数范围:\n")
    return max_num;


# 暂时不用
def checkMacNum(inputNum, maxNum):
    print ("Guess a number in 0 to " + str(max_num))
    input_num = input("")
    if 0 < input_num < maxNum:
        return input_num
    else:
        print ("the number is not fit")


########### 主流程
def game():
    print ("猜数字游戏开始：")
    isContinue = True;
    while isContinue:
        max_num = guessStart()
        random_num = random.randint(0, int(max_num))
        #	checkMacNum();
        isRight = False
        while not isRight:
            try:
                guess_num = input("猜一个整数: ")
                isRight = guessOnce(guess_num, random_num)
            except Exception as ex:
                print ("输入错误")
        cmdStr = "";
        try:
            cmdStr = input("点击任意键继续\n")
        except Exception as ex:
            cmdStr = str(cmdStr)
            print ("")
        # 退出逻辑
        if cmdStr == 'end':
            isContinue = False
            print ("exit success")
            print ("_" * 60)
            print ("_" * 60)
            print ("_" * 60)
        else:
            print("\n")
            print("———— 游戏重新开始 ————")

##### 执行部分
game()