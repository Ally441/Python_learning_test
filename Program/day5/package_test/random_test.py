Author = 'Liu Lei'
import random,sys#验证码
checkcode=''
for i in range(4):
    current=random.randint(0,4)
    if current == i:
        tmp=chr(random.randint(65,90))
    else:
        tmp=random.randint(0,9)
    checkcode+=str(tmp)
print(checkcode)
print(sys.argv)