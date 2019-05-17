import socket
import threading

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect(('192.168.1.105', 5963))
sock.send(b'1')  # 发送验证
print(sock.recv(1024).decode())  # 接收TCP数据，数据以字符串形式返回，bufsize指定要接收的最大数据量。flag提供有关消息的其他信息
print(sock.recv(1024).decode())
nickName = input('input your name: ')
sock.send(nickName.encode())  # encode方法把二进制转str


def sendThreadFunc():
    while True:
        try:
            myWord = input()  # 用户名
            sock.send(myWord.encode())
            # print(sock.recv(1024).decode())
        except ConnectionAbortedError:
            print('服务器关闭了这个连接')
            break
        except ConnectionResetError:
            print('服务器关闭')
            break


def recvThreadFunc():
    while True:
        try:
            otherWord = sock.recv(1024)
            if otherWord == "disconnect" or not otherWord.strip():
                sock.close()
                break
            else:
                print(otherWord.decode())
        except ConnectionAbortedError:
            print('服务器关闭连接')
            break
        except ConnectionResetError:
            print('服务器关闭')
            break


th1 = threading.Thread(target=sendThreadFunc)#方法
th2 = threading.Thread(target=recvThreadFunc)
threads = [th1, th2]
# 等待所有线程完成
for t in threads:
    t.setDaemon(True)#设置是后台线程
    t.start()
t.join()#阻塞当前上下文环境的线程，直到调用此方法的线程终止或到达指定的timeout（可选参数）
