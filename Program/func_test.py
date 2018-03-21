Author = 'Liu Lei'
import time
def timer(func):
    def deco(*args,**kwargs):
        start_time=time.time()
        func(*args,**kwargs)
        end_time=time.time()
        print('cost time %s'%(end_time-start_time))
    return deco
@timer #test1=timer(test1)
def test1():
    time.sleep(3)
    print('in the bar')
@timer #test2=timer(test2)
def test2(name,age):
    print('in the bar',name,age)

test1() # timer(test1)()
test2('name','20')