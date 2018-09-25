#!/usr/bin/env python3
import fileinput

old_plan = '/u01/app/oracle/product/Plan.xml'
new_plan = '/u01/app/oracle/product/Adapter_plan.xml'

#
# print(new_plan)
# print(old_plan)

with fileinput.FileInput('config.xml', inplace=True) as file:
    # for each line in file operation
    for line in file:
        # If we not find specific XML file
        if old_plan and new_plan not in line:
            # Not find string - add new string
            print(
                line.replace('<name>Adapter</name>', '<name>Adapter</name>\n<plan-path>', new_plan, '</plan-path>'),
                end='')

        else:
            # Change xml file
            print(line.replace(old_plan, new_plan), end='')
