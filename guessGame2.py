#coding=utf-8  

import random
#guess number game
def guessOnce(num,result):
#	print "guessOnce: "+str(num)+ " "+str(result)
	is_right=(int(num) == int(result))
	if is_right:
		print "#"*3+"_"*30+"#"*3
		print "猜正确了!!! 你赢了！！"
		print "数字是 "+ str(num) 
		print "#"*3+"_"*30+"#"*3
		return is_right
	elif (int(num) < int(result)):
		print "数值太小了"
		return is_right
	else: 
		print "数值太大了"
		return is_right
	
def guessStart():
	print "*"*70
	isRight = False;
	max_num = raw_input("输入最大值整数范围:\n")
	while (int(max_num)<=0):
		print "数字不合法"
		max_num = raw_input("输入最大值整数范围:\n")	
	return max_num;
#暂时不用
def checkMacNum(inputNum,maxNum):
	print "Guess a number in 0 to "+str(max_num)
	input = raw_input("")
	if(input>0 and input< maxNum):
		return input
	else:
		print "the number is not fit"


########### 主流程
print "猜数字游戏开始："
isContinue = True;
while isContinue:
	max_num = guessStart()
	random_num = random.randint(0,int(max_num))
#	checkMacNum();
	isRight = False
	while (not isRight):
		guess_num = raw_input("猜一个整数: ")
	 	isRight = guessOnce(guess_num,random_num)



print "exit success"
print "_"*100