#подключаем библиотеку
import xml.etree.ElementTree as ET


ET.register_namespace("", "http://xmlns.oracle.com/weblogic/domain")
ET.register_namespace("sec", "http://xmlns.oracle.com/weblogic/security")
ET.register_namespace("xsi", "http://www.w3.org/2001/XMLSchema-instance")
ET.register_namespace("wls", "http://xmlns.oracle.com/weblogic/security/wls")
ET.register_namespace("pas","http://xmlns.oracle.com/weblogic/security/providers/passwordvalidator")
ET.register_namespace("schemaLocation", "http://xmlns.oracle.com/weblogic/security/wls http://xmlns.oracle.com/weblogic/security/wls/1.0/wls.xsd http://xmlns.oracle.com/weblogic/domain http://xmlns.oracle.com/weblogic/1.0/domain.xsd http://xmlns.oracle.com/weblogic/security/xacml http://xmlns.oracle.com/weblogic/security/xacml/1.0/xacml.xsd http://xmlns.oracle.com/weblogic/security/providers/passwordvalidator/1.0/passwordvalidator.xsd http://xmlns.oracle.com/weblogic/security http://xmlns.oracle.com/weblogic/1.0/security.xsd")


#загружаем файл
tree = ET.parse('config_3.xml')

#Получаем дерево эллементов (или объект типа дерево ? )
root = tree.getroot()


#Задаем корень - надо ли?
root.findall(".")

#нНйти и заменить конкретный эллемент
for appdata in root.findall(
        "{http://xmlns.oracle.com/weblogic/domain}app-deployment[{http://xmlns.oracle.com/weblogic/domain}name='Adapter']"):
    appdata.find(
        '{http://xmlns.oracle.com/weblogic/domain}plan-path').text = "/u01/app/oracle/product/Adapter_plan_1024.xml"

    #записать в файл
    tree.write('config_3.xml')
