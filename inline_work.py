#!/usr/bin/env python3
import fileinput

with fileinput.FileInput('config.xml', inplace=True) as file:
    for line in file:
        print(line.replace('/u01/app/oracle/product/Adapter.rar', '/u01/app/oracle/product/New_Adapter.rar'), end='')
