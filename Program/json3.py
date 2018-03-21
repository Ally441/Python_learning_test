Author = 'Liu Lei'
import json
#def sayhi(name):
#    print("hello",name)
info={
    'name':'liulei',
    'age':22
}
f=open("text.txt","r")

data=json.loads(f.read())
print(data)