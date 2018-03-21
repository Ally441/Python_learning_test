Author = 'Liu Lei'
import shelve,datetime
d=shelve.open('shelve_test')
print(d.get("info"))
print(d.get("name"))
print(d.get("date"))
'''info={"age":20,"job":'student'}
name=["liu","test","lei"]
d["name"]=name
d["info"]=info
d["date"]=datetime.datetime.now()
d.close()'''