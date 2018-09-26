import fileinput
import sys

old_plan = '/u01/app/oracle/product/Plan.xml'
new_plan = '/u01/app/oracle/product/New_plan.xml'

old_tag = '<name>Adapter</name>'
new_tag = '<name>Adapter</name> \n <plan-path>/u01/111</plan-path>'

fileToSearch = 'config.xml'

for line in fileinput.input(fileToSearch, inplace=True):
        if old_plan in line:
            sys.stdout.write(line.replace(old_plan, new_plan))
            fileinput.close()
        elif new_plan in line:
            fileinput.close()
        else:
            sys.stdout.write(line.replace(old_tag, new_tag))
            fileinput.close()
