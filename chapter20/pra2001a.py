from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
from email.utils import parseaddr, formataddr

import smtplib


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, "utf-8").encode(), addr))


from_addr = "15904082220@163.com"
password = "YQScBURvpXyAPQjm"
to_addr = "yangfan6262008@gmail.com"
smtp_server = "smtp.163.com"

msg = MIMEMultipart("alternative")
msg["From"] = _format_addr(f"Python爱好者<{from_addr}>")
msg["To"] = _format_addr(f"管理员<{to_addr}>")
msg["Subject"] = Header("带附件的邮件……", "utf-8").encode()

msg.attach(MIMEText("hello", "plain", "utf-8"))
msg.attach(MIMEText("<html><body><h1>Hello</h1></body></html>", "html", "utf-8"))
# with open("./test.png", "rb") as f:
#     mime = MIMEBase("image", "png", filename="test.png")
#     mime.add_header("Content-Disposition", "attachment", filename="test.png")
#     mime.add_header("Content-ID", "<0>")
#     mime.add_header("X-Attachment-Id", "0")
#     mime.set_payload(f.read())
#     encoders.encode_base64(mime)
#     msg.attach(mime)

server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
