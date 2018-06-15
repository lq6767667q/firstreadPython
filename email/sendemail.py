from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
from wechatpy import parse_message, create_reply

import smtplib


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

# 输入Email地址和口令:
from_addr = 'liurui_777777@163.com'
password = '930906'
# 输入收件人地址:
to_addr = 'liurui_777777@163.com'
# 输入SMTP服务器地址:
smtp_server = 'smtp.163.com'

msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
msg['From'] = _format_addr('lr <%s>' % from_addr)
msg['To'] = _format_addr('六柒柒柒 <%s>' % to_addr)
msg['Subject'] = Header('关门关门~~~', 'utf-8').encode()

xml = '<xml><ToUserName><![CDATA[gh_c04197442c2d]]></ToUserName>\n<FromUserName><![CDATA[oiU7c0-RPA0vBOnV_y-0KocLC39Y]]></FromUserName>\n<CreateTime>1518329698</CreateTime>\n<MsgType><![CDATA[text]]></MsgType>\n<Content><![CDATA[\xe5\x95\x8a]]></Content>\n<MsgId>6521176397905932635</MsgId>\n</xml>'
msg = parse_message(xml)
print(msg)

try:
    smtp_port = 465
    server = smtplib.SMTP_SSL(smtp_server, smtp_port)
    server.set_debuglevel(1)
    server.login(from_addr, password)
    # server.sendmail(from_addr, [to_addr], msg.as_string())
    server.quit()
    print ("邮件发送成功")
except smtplib.SMTPException:
    print ("Error: 无法发送邮件")
