import socket
from Common import *
import time
import multiprocessing

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
    a=0
    length=pack[0:4]
    IDv = pack[4:19]
    length=int(length)
    Tickettgs = pack[19:length+19]
    len_pack = len(pack)
    len_Authenticator = len_pack-258*3-4-15-length
    Authenticator = pack[length+19:length+19+len_Authenticator]
    C = pack[-258*3:-258*2]
    key = pack[:-258*2]
    data = IDv+Tickettgs+Authenticator
    de_Tickettgs = Des(Tickettgs,Ktgs,1)
    Kc2tgs = de_Tickettgs[0:8]
    IDc = de_Tickettgs[8:23]
    ADc = de_Tickettgs[23:38]
    IDtgs = de_Tickettgs[38:53]
    TS2 = de_Tickettgs[53:63]
    Lifetime2=de_Tickettgs[63:67]
    de_Authenticator = Des(Authenticator,Kc2tgs,1)
    IDc_1 = de_Authenticator[0:15]
    ADc_1 = de_Authenticator[15:30]
    TS3 = de_Authenticator[30:40]

    if yanzheng(data,C,key)==True:
        pack2C = pack_tgs(IDc,ADc,IDv,Kc2tgs)
        client.send(pack.encode('utf-8'))



def pack_tgs(IDc,ADc,IDv,Kc2tgs):
    Lifetime4 = '1000'
    Kc2v=getRandomKey()
    TS4=str(int(time.time()))
    de_Ticketv= Kc2v+"{:15}".format(IDc)+"{:15}".format(ADc)+"{:15}".format(IDv)+TS4+Lifetime4
    Ticketv = Des(de_Ticketv,Kv,0)
    de_data = Kc2v + "{:15}".format(IDv) + TS4 + Ticketv
    data = Des(de_data,Kc2tgs,0)
    length = str(len(data))
    (C,d,n)=qianming(data)
    pack = "{:4}".format(length)+data+"{:258}".format(C)+"{:258}".format(d)+"{:258}".format(n)
    return pack
def fun(client,addr):
    (indata, addr, client) = jieshou(client,addr)
    unpack_tgs(indata)

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
