# 调查问卷-学生

## 1、相关支持

- flask（需安装）
- xlutils（需安装）
- wtforms（需安装）
- flask_wtf（需安装）
- re
- email
- smtplib

没记错的话最后两个是自带的 **:-)**，pip.txt文件里已经写了安装命令，直接cmd输入就行。

## 2、使用方法

使用cmd进入app.py所在的目录，输入：

	python app.py

即可在本机运行服务器，局域网内其他用户访问：

	(hostip):14250

（hostip为你的本机ip）便能进入网页。<br>
使用mail.py可以为用户发送一些邮件。

### 修改问卷内容：

修改question.txt，使用 utf-8 without BOM 编码，格式：

	你的问题
	选项A
	选项B
	选项C
	选项D
	选项E
	选项F
	……
	END

如果没有6个选项，**务必留下空行，结束时必须以END结尾！**

### 修改表单内容

请自行学习flask-wtf的相关内容，只需要对源码进行一部分修改就可以完成你自己的任务。

### 发送邮件

使用mail.py可以发送邮件，邮件地址为 （填写的QQ号）@qq.com。<br>
邮件内容可以修改mailmsg.txt里的内容。
值得一提的时，用户的称谓是由他填写的决定的。

### 其他

该程序并没有很大的适用性，如果学习了相关内容修改也不会很复杂。

## 3、注意事项

question.txt的内容格式一定要符合要求，不然会报错。

## 4、数据保存

answer.xls是保存用户答案的Excel表格<BR>
number.xls是保存用户表单的Excel表格<BR>
之后的数据你需要自己处理。