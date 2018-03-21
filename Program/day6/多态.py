Author = 'Liu Lei'
class Animal(object):
    def __init__(self,name):
        self.name=name
    def animal_talk(object):
        object.talk()
    def talk(self):
       raise NotImplementedError("Subclass must implement abstact method")
class Cat(Animal):
    def talk(self):
        print("%s:喵喵"%self.name)

class Dog(Animal):
    def talk(self):
        print("%s 汪汪"%self.name)

c1=Cat("liu")
c1.talk()
d1=Dog("lei")
d1.talk()
Animal.animal_talk(c1)
Animal.animal_talk(d1)