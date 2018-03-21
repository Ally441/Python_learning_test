Author = 'Liu Lei'
import time
user,passwd='liu','123'
def auth(auth_type):
    print("auth func:",auth_type)
    def outer_wrapper(func):
        def wrapper(*args, **kwargs):
            print("wrapper func ars:",*args,**kwargs)
            if auth_type=="local":
                username = input("username:").strip()
                password = input("password:").strip()
                if user == username and passwd == password:
                    print("User has passed authentication")
                    return func(*args, **kwargs)
                else:
                    exit("Invalid username or password")
            elif auth_type=="ldap":
                print("helllownsvdlz")
        return wrapper
    return outer_wrapper
@auth
def index():
    print('welcome to index page')
@auth(auth_type="local")
def home():
    print('welcome to home page')
    return "from home"
@auth(auth_type="ldap")
def bbs():
    print("welcome to bbs page")

home()
bbs()