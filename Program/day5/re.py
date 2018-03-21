Author = 'Liu Lei'
import re
a=re.compile(r'^[123]',re.VERBOSE)
b=a.search('131p')
print(b.group())