from email.header import Header
from email.mime.text import MIMEText
from xlrd import open_workbook
import smtplib
from_addr = 'zhouzihao2008@126.com'
password = 'zhouzihao626078'
smtp_server = 'smtp.126.com'
fp = open('mailmsg.txt','r',encoding='utf-8')
text = fp.read()
fp.close()
book = open_workbook('number.xls')
sheet = book.sheet_by_index(0)
i = int(sheet.cell(0,0).value)
server = smtplib.SMTP(smtp_server,25)
server.set_debuglevel(1)
server.login(from_addr,password)
for x in range(int(input('从第多少行开始'))-1,i):
    print(x,':')
    name = sheet.cell(x,0).value
    print(name)
    to_addr = str(int(sheet.cell(x,1).value))+'@qq.com'
    print(to_addr)
    msg = MIMEText(name+':\n'+text,'plain','utf-8')
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Subject'] = Header('通中科技社联期待你的加入','utf-8').encode()
    server.sendmail(from_addr,[to_addr],msg.as_string())
    if x%10==0:
        server.quit()
        server = smtplib.SMTP(smtp_server, 25)
        server.set_debuglevel(1)
        server.login(from_addr, password)
server.quit()