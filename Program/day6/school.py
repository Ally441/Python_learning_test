Author = 'Liu Lei'

class School(object):
    def __init__(self,name,addr):
        self.name=name
        self.addr=addr
        self.students=[]
        self.teachers=[]
    def enroll(self,stu_obj):
        print("为学员%s办理注册手续"%stu_obj)
        self.students.append(stu_obj)

class SchoolMember(object):
    def __init__(self,name,id,age):
        pass

    def tell(self):
        print('''---- info of 
        ''')
class Teacher(School):
    pass
