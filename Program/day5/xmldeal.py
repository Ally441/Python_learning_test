Author = 'Liu Lei'
import xml.etree.ElementTree as ET
tree=ET.parse("xmltest.xml")
root=tree.getroot()
'''print(root)
print(root.tag)
for chlid in root:
    print(chlid.tag,chlid.attrib)
    for i in chlid:
        print(i.tag,i.text,i.attrib)
for node in root.iter("year"):
    print(node.tag,node.text)
'''
for node in root.iter("year"):
    new_year=int(node.text)+1
    node.text=str(new_year)
    node.set("update","liu")
tree.write("xmltest.xml")
for country in root.findall("country"):
    rank=int(country.find("rank").text)
    if rank>50:
        root.remove(country)
tree.write("xmltest.xml")