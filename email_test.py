# -*- coding: utf-8 -*-

from email.mime.text import MIMEText
from email import encoders
from email.header import Header
from email.utils import parseaddr, formataddr
import smtplib

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr.encode('utf-8') if isinstance(addr, unicode) else addr))


content = '''
    <div style="border: 1px solid #CCC;margin-bottom:50px;
        width: 590px;
        font-size: 12px;
        line-height: 1.125;">
        <div style="padding: 15px 0 15px 30px; border-bottom: 1px solid #EEE">
            <img src="http://dev.jzvoice.com.cn/img/logo.png">
        </div>
        <div style="padding: 50px 30px">
            <div style="margin-bottom: 35px;font-size: 14px;font-weight: bold;">
                亲爱的 290910802@qq.com
            </div>
            <div style="margin-bottom: 30px">
                我们收到您的密码重置请求，点击下面链接重置你的密码
            </div>
            <div style="margin-bottom: 50px">
                <a href="http://dev.jzvoice.com.cn" target="_blank">http://dev.jzvoice.com.cn/aaaa/bbbb/cccc/ddddddd/eeeeeee/fffffff.html</a>
            </div>
            <div>
                此邮件30分钟内有效，如果你忽略这条信息，密码将不进行更改
            </div>
        </div>
    </div>
    '''

msg = MIMEText(content, 'html', 'utf-8')

from_addr = 'jzvocie@126.com'
password = ''   # smtp授权码
smtp_server = 'smtp.126.com'
to_addr = '290910802@qq.com'

msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
msg['To'] = _format_addr('管理员 <%s>' % to_addr)
msg['Subject'] = Header('来自SMTP的问候……', 'utf-8').encode()


server = smtplib.SMTP_SSL(smtp_server, 465)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
