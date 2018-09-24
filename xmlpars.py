import xml.etree.ElementTree as ET
tree = ET.parse('config.xml')
root = tree.getroot()

root.findall(".")
print(root.tag)
#
# root.findall(".//*[@name='DEMOAPP']/configuration-property")

a = root.findall("./security-configuration/*[@name='DEMOAPP']")

print(a)
