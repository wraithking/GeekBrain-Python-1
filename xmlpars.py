#подключаем библиотеку
import xml.etree.ElementTree as ET

#загружае файл 
tree = ET.parse('config.xml')

#читаем файл в переменную
root = tree.getroot()

#задаем корень - надо ли?
root.findall(".")
print(root.tag)

#найти и вывести всех детей корня
for child in root:
    print(child.tag, child.attrib)

#найти и вывести конкретный эллемент
for appdata in root.findall("app-deployment/*[@name='Adapter']"):
    name = appdata.get('name')
    target = appdata.get('target')
    plan = appdata.get('plan')
    print(name, target, plan)
