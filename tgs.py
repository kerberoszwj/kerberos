import socket
from Common import *



server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host=socket.gethostname()
port = 9090

server.bind(('192.168.1.105', port))
server.listen(5)
Ktgs = '12345678'
def jieshou():
    client,addr=server.accept()
    print("已连接")
    addr=addr[0]
    try :
        indata = (client.recv(2048)).decode('utf-8')
    except Exception as e:
            print("没收到")
    return indata,addr,client


def unpack_tgs(pack):
    print(pack)

    length=pack[0:4]
    IDv = pack[4:19]
    length=int(length)
    Tickettgs = pack[19:length+19]
    len_pack = len(pack)
    len_Authenticator = len_pack-258*3-4-15-length
    Authenticator = pack[length+19:length+19+len_Authenticator]
    C = pack[-258*3:-258*2]
    key = pack[-258*2:]
    data = IDv+Tickettgs+Authenticator
    print(data)
    print("C",C)
    print("key",key)
    if yanzheng(data,C,key)==True:
        print("RSA验证成功")

def pack_tgs():
    print()







(indata, addr, client) = jieshou()
print(indata)
unpack_tgs(indata)
