Author = 'Liu Lei'
import json,pickle
def sayhi(name):
    print("hello",name)
info={
    'name':'liulei',
    'age':22,
    'func':sayhi
}
f=open("text.txt","rb")
data=pickle.loads(f.read())
print(data['func']("liu"))
