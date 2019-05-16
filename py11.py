import socket
'''
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect(('127.0.0.1', 5963))
#server.bind(('127.0.0.1', 9090))#本机
#server.listen(10)
print('client', socket.gethostbyname('127.0.0.1'), 'con ...')'''
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(('www.baidu.com', 0))
sourceIP = s.getsockname()[0]
print(sourceIP)