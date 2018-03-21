Author = 'Liu Lei'
import xml.etree.ElementTree as ET

new_xml=ET.Element("namelist")#根节点
name=ET.SubElement(new_xml,"name",attrib={"enrolled":"yes"})
name.text="liu"
age=ET.SubElement(name,"age",attrib={"enrolled":"no"})
sex=ET.SubElement(name,"sex")
age.text='60'
sex.text='boy'
name2=ET.SubElement(new_xml,"name",attrib={"enrolled":"yes"})
name2.text="lei"
age=ET.SubElement(name2,"age",attrib={"enrolled":"no"})
sex=ET.SubElement(name2,"sex")
age.text='18'
age.text='girl'
et=ET.ElementTree(new_xml)#生成文档对象
et.write("test.xml",encoding="utf-8",xml_declaration=True)
ET.dump(new_xml)#打印生成格式