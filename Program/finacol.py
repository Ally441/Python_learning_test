Author = 'Liu Lei'
def fin(max):
    n,a,b=0,0,1
    while n<max:
        yield b
        a,b=b,a+b
        n=n+1
    return 'Done'
gen=fin(10)
g=fin(6)
for i in gen:
    print(i)
while True:
    try:
        x=next(gen)#next(gen)==gen.__next__()
        print('gen:',x)
    except StopIteration as e:
        print('Generator return value:',e.value)
        break