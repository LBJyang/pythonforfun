import socket, ssl

hostname = "www.sina.com.cn"
port = 443
# 1. 创建一个 SSLContext，适用于客户端验证服务器证书
context = ssl.create_default_context()

# 2. 建立普通 TCP 连接
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((hostname, port))

# 3. 用 context.wrap_socket 把普通 socket 升级为 SSL socket
ssl_sock = context.wrap_socket(sock, server_hostname=hostname)

# 4. 发送 HTTP 请求（HTTPS 的 GET 请求）
ssl_sock.send(
    b"GET / HTTP/1.1\r\nHost: " + hostname.encode() + b"\r\nConnection: close\r\n\r\n"
)

# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# ssl_s = ssl.wrap_socket(s)
# s.connect(("www.sina.com.cn", 443))
# s.send(b"GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n")

buffer = []
while True:
    d = ssl_sock.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data = b"".join(buffer)
ssl_sock.close()
header, html = data.split(b"\r\n\r\n", 1)
print(header.decode("utf-8"))
with open("sina.html", "wb") as f:
    f.write(html)
