Author = 'Liu Lei'

list_1=[1,2,3,2,3,1,4,6]
list_1=set(list_1)
list_2=set([1,2,3,7,8,9,11,2])
'''
print(list_1,type(list_1))
print(list_1,list_2)
print(list_1.intersection(list_2))#交
print(list_1.union(list_2)) #并
print(list_1.difference(list_2))#差
print(list_1.issubset(list_2))#子集
print(list_1.issuperset(list_2))#父集
print(list_1.symmetric_difference(list_2))#对称差集
'''
print(list_1&list_2)
print(list_1 | list_2)
print(list_1-list_2)
print(list_1^list_2)
list_1.add(123)
print(list_1)
list_1.update(list_2)
print(list_1)
a=1
print(a in list_1)
print(list_1)
print(list_1.pop())
print(list_1.pop())
print(list_1.pop())
print(list_1.pop())
print(list_1.pop())
print(list_1.pop())
print(list_1)