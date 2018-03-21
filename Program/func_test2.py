Author = 'Liu Lei'
import time
def logging():
    time_format='%Y-%M-%D %x'
    time_current=time.strftime(time_format)
    print(time_current)
    with open('a.txt','a+') as file:
        file.write('end action\n')
def test1():
    """test1 starting action..."""
    print('in the test1')
    logging()
'''def test2():
    """testing start action2..."""
    print('in the test2')
    logging()'''
def test3():
    """testing start action3..."""
    print('in the test3')
    logging()
def test4(x,y=0):
    print(x+y)
def test5(x,*args):
    print(x)
    print(args)
def test2(**kwargs):
    print(kwargs)
test2(name='liulei',age=18,sex='girl')
test2(**{'name':'liu','age':18})
'''test1()
test2()
test3()
test4(1,2)'''
test5(1,2,3,4,5,6,7,8,9,10)
def expr(num,n):
    if n==0:
        return 1
    return num*expr(num,n-1)
print(expr(2,5))
def Fib(a,b,n):
    if n==0:
        return b
    else:
        return Fib(b,a+b,n-1)
print(Fib(3,4,5))
def add(a,b,f):
    return f(a)+f(b)
res=add(-3,-6,abs)
print(res)