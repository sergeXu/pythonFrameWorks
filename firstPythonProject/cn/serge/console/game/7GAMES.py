# 7 GAMES

## get number length
def get_number_length(num):
    try:
        number = int(num)
    except Exception as ex:
        print ("参数错误")
### check every number 7
def number_relate_to_7(num):
    num_string = str(num)
    for num_char in num_string:
        if(num_char=='7'):
            return True;
    return False;

# define if about 7
def relevent_to_7(num):
    try:
        number = int(num)
    except Exception as ex:
        print ("参数错误")
    if (number % 7) == 0:
        return True
    elif number_relate_to_7(num):
        return True
    else:
        return False

def game7_start():
    print("7游戏开始!")
    print("-"*80)
    num_max = input("请输入最大值\n")
    try:
        num_max_int = int(num_max)
    except Exception as ex:
        print ("输入错误")
        return False
    print("数字序列为：")
    num = 0
    while num < num_max_int:
        num += 1;
        isRelated7 = relevent_to_7(num)
        if isRelated7 == False:
            print(num)
        else:
             print(" * ");
    print("Game end ")
    print("-" * 80)

## 调用入口
game7_start()