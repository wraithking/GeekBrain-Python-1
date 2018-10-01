import fileinput
import sys

#Если в файле нету oracle_sid записать в файл
#если нету oracle_home записать в файл
#если нету oracle_path записать в файл

oracle_sid  = 'ORACLE_SID=DEMO'
oracle_home = 'ORACLE_HOME=/u01/app/oracle/product/DEMO_1'
oracle_path = 'PATH=$PATH:$ORACLE_HOME/bin'

fileToSearch = 'a.bash_profile'
got_tag = False
for line in fileinput.input(fileToSearch, inplace=True, backup='.bak'):
    if oracle_sid not in line:
        got_tag = False
        fileToSearch.write(line + '\n sdsds' + oracle_sid)
        sys.stdout.write(line + '\n sdsds' + oracle_sid)
        sys.stdout.write(oracle_home)
    elif oracle_home in line:
        got_tag = False
        sys.stdout.write(line + '\n' + oracle_home)
    else:
        got_tag = False
        sys.stdout.write(line + '\n' + oracle_path)
fileinput.close()

