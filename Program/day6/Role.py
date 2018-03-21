Author = 'Liu Lei'
class Role:
    n=123
    n_list=[]
    name="liulei"
    def __init__(self,name,role,weapon,life_value=100,money=15000):
        self.name=name#静态属性
        self.role=role
        self.weapon=weapon
        self.__life_value=life_value
        self.money=money
    def show(self):
        print("name:%s __life_value:%s" %(self.name,self.__life_value))
    def shot(self):
        print("shooting")
    def got_shot(self):
        print("ah...,I got shot...")
    def buy_gun(self,gun_name):
        print("%s just bought %s" %(self.name,gun_name))
    def __del__(self):
        print("is really dead")
r1=Role('Alex','police','AK47') #实例化(初始化一个类):把一个类变成一个具体对象的过程.
r1.show()
r1.shot()
del r1
r2=Role('liu','terrorist','M12')
r2.buy_gun("AK47")
'''print(r1.life_value)
r1.buy_gun('AK47')
r1.shot()
r1.got_shot()
del r1.weapon
r1.name="ally"
r1.bullet_prove=True
r1.n="change"
Role.n=100
r3=Role("asas","sads","sadlsad")
print(r3.n)
r2.name="jack"
print(r1.name,r1.bullet_prove)
print(r2.name)
print(r1.n,r2.n)
print(Role.name)
print(Role.n)
r1.n="change"
r2.n="exchange"
r1.n_list.append("from r1")
r2.n_list.append("from r2")
Role.n=100
print(r1.n,r1.n_list)
print(r2.n_list)
print(Role.n_list)'''