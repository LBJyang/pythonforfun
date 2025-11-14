from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
from email.header import Header


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, "utf-8").encode(), addr))


from_addr = "15904082220@163.com"
password = "YQScBURvpXyAPQjm"
to_addr = "yangfan6262008@gmail.com"
smtp_server = "smtp.163.com"

msg = MIMEText("hello,send by Python...", "plain", "utf-8")
msg["From"] = _format_addr(f"Python爱好者<{from_addr}>")
msg["To"] = _format_addr(f"管理员<{to_addr}>")
msg["Subject"] = Header("来自SMTP的问候……", "utf-8").encode()

import smtplib

server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
