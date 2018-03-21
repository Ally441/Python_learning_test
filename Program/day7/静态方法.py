Author = 'Liu Lei'
class Dog(object):

    name="liulei"
    def __init__(self,name):
        self.name=name
        self.__food=None
    #@staticmethod#实际上跟类没什么关系
    @property
    def eat(self):
        print("%s is eating %s "%(self.name,self.__food))
    @eat.setter
    def eat(self,food):
        print("set to food:",food)
        self.__food=food
    @eat.deleter
    def eat(self):
        del self.__food
        print("delete all")
    @classmethod
    def talk(self):
        print("%s is talking"%self.name)
d=Dog("liulei")
d.eat
d.eat="hangge"
d.eat
d.talk()
del d.eat
d.eat
