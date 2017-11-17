### 联系方式
def line():
    print('-'*30)
def run():
    name_decode = b'\xe5\xbe\x90\xe5\xbf\x97\xe6\x9d\xb0'
    occupation = b'\xe9\x98\xbf\xe9\x87\x8c\xe5\xb7\xb4\xe5\xb7\xb4-\xe8\x8f\x9c\xe9\xb8\x9f-CTO-\xe7\xa0\x94\xe5\x8f\x91\xe4\xb8\xad\xe5\x8f\xb0\xe6\x8a\x80\xe6\x9c\xaf\xe9\x83\xa8'
    num = [5,8,1,9,4,0,3,2]
    index = [2,0,2,0,1,1,3,3,5,6,4]
    tel = ""
    for t in index:
        tel += str(num[t])
    line()
    print(name_decode.decode() + ": "+tel)
    print(occupation.decode())
    line()
run();