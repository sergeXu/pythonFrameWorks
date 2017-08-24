#coding=utf-8  

import random
#guess number game
def guessOnce(num,result):
#	print "guessOnce: "+str(num)+ " "+str(result)
	is_right=(int(num) == int(result))
	if is_right:
		print "#"*3+"_"*30+"#"*3
		print "That is it, you are right, Wining!!!"
		print "The number is "+ str(num) 
		print "#"*3+"_"*30+"#"*3
		return is_right
	elif (int(num) < int(result)):
		print "the number is too small\n"
		return is_right
	else: 
		print "the number is too big\n"
		return is_right
	
def guessStart():
	print "*"*70
	isRight = False;
	max_num = raw_input("input Max number:\n")
	while max_num<=0:
		print "the number is not fit"
		max_num = raw_input("input Max number:\n")	
	return max_num;
#暂时不用
def checkMacNum(inputNum,maxNum):
	print "Guess a number in 0 to "+str(max_num)
	input = raw_input("")
	if(input>0 and input< maxNum):
		return input
	else:
		print "the number is not fit"

isContinue = True;
while isContinue:
	max_num = guessStart()
	random_num = random.randint(0,int(max_num))
#	checkMacNum();
	isRight = False
	while (not isRight):
		guess_num = raw_input("Guess a num: ")
	 	isRight = guessOnce(guess_num,random_num)



print "exit success"
print "_"*100