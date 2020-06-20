"""
    http请求响应示例
"""
from socket import *

s = socket()
s.bind(("0.0.0.0", 8001))
s.listen(5)

c, addr = s.accept()
print("Connect from ", addr)

# 接收消息
data = c.recv(4096)
print(data.decode())

# 发送给浏览器一些内容，显示
# 按照响应格式组织
# response = """HTTP/1.1 200 OK\r\nContent-Type:text/html\r\n\r\nThis is a http test"""
response = "HTTP/1.1 200 OK\r\n"  # 响应行
response += "Content-Type:text/html\r\n"  # 响应头可以有多个
response += "\r\n"  # 空行
# response += "This is a http test"  # 响应体

with open("python.html") as f:
    response += f.read() # 响应体

c.send(response.encode())

c.close()
s.close()
