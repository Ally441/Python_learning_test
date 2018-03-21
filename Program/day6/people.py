Author = 'Liu Lei'
class People:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.friends=[]
        print("----doesn't run-----")
    def eat(self):
        print("%s is eating ..."%self.name)
    def sleep(self):
        print("%s is sleeping ..."%self.name)
    def talk(self):
        print("%s is talking ...."%self.name)
class Relation(object):
    def __init__(self,n1,n2):
        print("init in relation")
    def make_friends(self,obj):
        print("%s is making friends with %s"%(self.name,obj.name))
        self.friends.append(obj)
class Man(People,Relation):

    '''def __init__(self,name,age,money):
        People.__init__(self,name,age)
        self.money=money
        print("%s have %s money "%(self.name,self.money))'''
    def swimming(self):
        print("%s is swimming...."%self.name)
    def sleep(self):
        People.sleep(self)
        print("man is sleeping...")
class Woman(People,Relation):
    def __init__(self,name,age):
        super(Woman,self).__init__(name,age)
    def get_birth(self):
        print("%s is born a baby..."%self.name)

m1=Man("liulei","20")
m1.swimming()
w1=Woman("ally","18")
'''m1.eat()
m1.sleep()
m1.swimming()
w1=Woman("ally","20")
w1.get_birth()
m1.make_friends(w1)'''
m1.make_friends(w1)
print(m1.friends[0])
print(m1.friends)
print(m1.friends[0].name)
w1.name="jack"
print(m1.friends[0].name)