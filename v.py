import time
import rsa2
from Common import *
import socket
import multiprocessing
import threading

def jieshou():
    client,addr=server.accept()
    print("已连接")
    addr=addr[0]
    try :
        indata = (client.recv(2048)).decode('utf-8')
    except Exception as e:
            print("没收到")

    return indata,addr,client
def unpack(pack):
    length = pack[0:4]
    length = int(length)
    Ticketv = pack[4:4+length]
    de_Ticket = Des(Ticketv,Kv,1)
    Kc2v = de_Ticket[0:8]
    all_length = len(pack)
    Authenticatorc = [4+length:4 + length + all_length - 258*3]
    de_Authenticatorc = Des(Authenticatorc,Kc2v,1)
    TS5 = de_Authenticatorc[-10:]
    C=pack[-258*3:-258*2]
    key = pack[-258*2:]
    if yanzheng(Ticketv+Authenticatorc,C,key)==True:
        print("RSA验证成功")
        packc = pack2c(Kc2v,TS5)

def pack2c(Kc2v,TS5):
    TS5=int(TS5)
    pack = Des(str(TS5+1),Kc2v,0)
    return pack







if __name__=='__main__':
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    hostname = socket.gethostname()
    ip=socket.gethostbyname(hostname)
    port = 9090
    server.bind((ip, port))
    server.listen(5)
    Ktgs = '12345678'
    Kv = '56789123'
    while True:
        try:
            client, addr = server.accept()
            m = multiprocessing.Process(target=fun, args=(client,addr))
            m.daemon = True  # daemon True设置为守护即主死子死.
            m.start()
        except ConnectionResetError:
            pass

        except Exception as e:
            print(e)