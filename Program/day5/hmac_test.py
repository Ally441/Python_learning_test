Author = 'Liu Lei'
import hmac
h=hmac.new(b"123",b"fuck you")
print(h.digest())
print(h.hexdigest())