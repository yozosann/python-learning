from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.multipart import MIMEBase
from email.utils import parseaddr, formataddr
import smtplib

# 我们编写了一个函数_format_addr()来格式化一个邮件地址。注意不能简单地传入name <addr@example.com>，因为如果包含中文，需要通过Header对象进行编码。

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

# 输入Email地址和口令:
from_addr = 'ytj123yue_@126.com' # input('From: ')
password = '1314159' # input('Password: ')
# 输入收件人地址:
to_addr = '407763432@qq.com' # input('To: ')
# 输入SMTP服务器地址:
smtp_server = 'smtp.126.com' # input('SMTP server: ')

# 邮件对象:
msg = MIMEMultipart()
msg['From'] = _format_addr('91彩票协会 <%s>' % from_addr)
msg['To'] = _format_addr('管理员 <%s>' % to_addr)
msg['Subject'] = Header('【彩票中奖提示】', 'utf-8').encode()

# 邮件正文:
msg.attach(MIMEText('<html><body><h1>Hello</h1>' +
    '<p><img src="cid:0"></p>' +
    '</body></html>', 'html', 'utf-8'))

with open('./blur.jpg', 'rb') as f:
    mime = MIMEBase('image', 'jpg', filename='blur.jpg')
    # 加上必要的头信息
    mime.add_header('Content-Disposition', 'attachment', filename='blur.jpg')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    # 把邮件内容读进来
    mime.set_payload(f.read())
    # 用Base64编码:
    encoders.encode_base64(mime)
    # 添加到MIMEMultipart:
    msg.attach(mime)

server = smtplib.SMTP(smtp_server, 25) # SMTP协议默认端口是25
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()