Author = 'Liu Lei'
import time
def consumer(name):
    print("%s 准备吃包子！" %name)
    while True:
        bz=yield

        print("包子[%s]来了,被[%s]吃了" %(bz,name))
def producer(name):
    c=consumer('A')
    c2=consumer('B')
    c.__next__()
    c2.__next__()
    print("start make bz")
    for i in range(10):
        time.sleep(1)
        print("make two bzs")
        c.send(i)
        c2.send(i)
producer('liulei')