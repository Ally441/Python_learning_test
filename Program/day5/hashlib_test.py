Author = 'Liu Lei'
import hashlib
#md5
m=hashlib.md5()
m.update(b"Hello")
print(m.hexdigest())
m.update(b"It's me")
print(m.digest())#2进制格式hash
print(m.hexdigest())#16进制格式hash
n=hashlib.md5()
n.update(b"HelloIt's me")
print(n.hexdigest())
#     sha1
hash=hashlib.sha1()
hash.update(b'Hello')
print(hash.hexdigest())
#     sha256
hash=hashlib.sha256()
hash.update(b'Hello')
print(hash.hexdigest())
#     sha384
hash=hashlib.sha384()
hash.update(b'Hello')
print(hash.hexdigest())
#     sha512
hash=hashlib.sha512()
hash.update(b'Hello')
print(hash.hexdigest())