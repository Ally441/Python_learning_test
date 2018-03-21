Author = 'Liu Lei'
import functools
'''res=filter(lambda n:n>5,range(10))
for i in res:
    print(i)
res=map(lambda n:n*2,range(10))
res1=[lambda i:i*2 for i in range(10)]
for i in res:
    print(i)
'''
res=functools.reduce(lambda x,y:x*y,range(1,10))#reduce
print(res)
scientists =({'name':'Alan Turing', 'age':105, 'gender':'male'},
             {'name':'Dennis Ritchie', 'age':76, 'gender':'male'},
             {'name':'Ada Lovelace', 'age':202, 'gender':'female'},
             {'name':'Frances E. Allen', 'age':84, 'gender':'female'})
def reducer(sci,value):
    sum=sci+value['age']
    return sum
total=functools.reduce(reducer,scientists,0)
print(total)
'''def grouped_gender(group,value):
    group[value['gender']].append(value('name'))
    return group
res=functools.reduce(grouped_gender,scientists,{'male':[],'female':[]})
'''
a=frozenset([1,4,33,12,3,4])
print(globals())