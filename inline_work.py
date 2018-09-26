#!/usr/bin/env python3
import fileinput

old_plan = '/u01/app/oracle/product/Adapter.rar'
new_plan = '/u01/app/oracle/product/New_Adapter.rar'

old_tag = '<name>Adapter</name>'
new_tag = "<name>Adapter</name> <plan-path>" + new_plan + "</plan-path>"

with fileinput.FileInput('config.xml', inplace=True) as file:
    for line in file:
        print(line.replace(old_tag, new_tag), end='')
fileinput.close()
