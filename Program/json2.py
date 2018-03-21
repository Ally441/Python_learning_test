Author = 'Liu Lei'
import json
def sayhi(name):
    print("hello",name)
info={
    'name':'liulei',
    'age':22,
   # 'func':sayhi
}
f=open("text.txt",'w')
f.write(json.dumps(info))
info['age']=21
f.write(json.dumps(info))
f.close()