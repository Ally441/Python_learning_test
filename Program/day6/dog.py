Author = 'Liu Lei'
class Dog:
    def __init__(self,name):
        self.name=name
    def bulk(self):
        print("%s,wwww!"%self.name)
    def __call__(self, *args, **kwargs):
        print('__call__')
    def __str__(self):
        return "liulei"
d1=Dog("ll")
print(d1)
d1()
print(d1.__dict__)
print(Dog.__dict__)
'''d2=Dog()
d1.bulk()'''