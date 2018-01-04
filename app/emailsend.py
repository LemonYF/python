from email.mime.text import MIMEText
from email.header import Header
import smtplib

# 输入Email地址和口令:
from_addr = 'yefan1_test@163.com'
password = '1994421这个'
# 输入收件人地址:
to_addr = 'yefan_yf1@sina.com'
# 输入SMTP服务器地址:
smtp_server = 'smtp.163.com'
subject = 'nihao'

# 发件邮箱和收件邮箱需要真实地址，否则无法发送
msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
msg['Subject'] = Header(subject, 'utf-8')
msg['From'] = 'yefan1_test@163.com'
msg['To'] = 'yefan_yf1@sina.com'


server = smtplib.SMTP_SSL(smtp_server, 587)  # SMTPSSL协议默认端口是587
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
