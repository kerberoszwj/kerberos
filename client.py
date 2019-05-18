import hashlib
# 导入socket包
import socket, threading
import time
from Common import *




def fengzhuang(data):
    length = "{:4}".format(str(len(data)))
    print(length+data)
    a=length+data
    return a


def logging(user,mima):


        # 输入账号密码

        ts = time.time()
        ts=str(int(ts))
        a=user + ' ' + mima + "{:15}".format(IDc) + "{:15}".format(IDtgs) + ts
        (C,d,n)=qianming(a)
        data = a+"{:258}".format(C)+"{:258}".format(d)+"{:258}".format(n)
        print(data)
        out=fengzhuang(data)
        # 发送给服务器
        print(out)
        client.send(out.encode('utf-8'))
        len_mima = len(mima)
        while len_mima < 8:
            mima = mima + '0'
            len_mima = len_mima + 1
        global Kc
        Kc=mima


def recv_basic(client):

    data_1 = (client.recv(2048)).decode('utf-8')

    client.close()
    return data_1


def recv_(client):
    total_data=''
    data = (client.recv(2048)).decode('utf-8')

    return data

'''def indatas():
        # 接受来自服务器的信息
    try:
        indata = (client.recv()).decode('utf-8')
        print(indata)
    except Exception as e:
        print("没收到AS的回复")'''



def jiance(C,key,undata,Ts2,Lifetime2,Ts3):#检测时间戳和RSA验证
    a=0
    if yanzheng(undata, C, key)==True:
        print("签名验证成功")
        a=a+1
    '''print(Ts3)
    Ts3=int(Ts3)
    Ts2=int(Ts2)
    Lifetime2 = int(Lifetime2)
    print(Ts3,Ts2,Lifetime2)'''
    if int(Ts3)-int(Ts2)<int(Lifetime2):
        a=a+1
    return a


def lianjie(ip):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port=9090
    client.connect((ip, port))
    print("连接成功")
    return client

def pack_(Ticekttgs,Kc2tgs,Ts3):
    Authenticator = Des("{:15}".format(IDv)+"{:15}".format(ADc)+Ts3,Kc2tgs,0)
    print('auth',Authenticator)
    data = "{:15}".format(IDv)+Ticekttgs+Authenticator
    length = "{:4}".format(str(len(Ticekttgs)))
    (C,d,n)=qianming(data)
    pack = length + data + "{:258}".format(C)+"{:258}".format(d)+"{:258}".format(n)
    return pack

def unpack_(pack):
    length=int(pack[0:4])
    data = pack[4:4+length]
    print("data",data)
    C=pack[-258*3:-258*2]
    key=pack[-258*2:]
    undata = data
    data = Des(data,Kc,1)
    global Kc2tgs
    Kc2tgs = data[0:8]
    IDtgs = data[8:23]
    Ts2 = data[23:33]
    #global Ts3
    Ts3 = time.time()
    Ts3_ = str(int(Ts3))
    Lifetime2 = data[33:37]
    Tickettgs = data[37:]
    if jiance(C,key,undata,Ts2,Lifetime2,Ts3_ )==2:
        print("成功")
        pack2tgs = pack_(Tickettgs,Kc2tgs,Ts3_)
        print("pack2tgs",pack2tgs)
        client = lianjie(IPtgs)
        client.send(pack2tgs.encode('utf-8'))
        print("已发送")
        tgs_pack = recv_basic(client)
        unpack_tgs(tgs_pack)
        pack_v = pack2v(Ticketv)
        client = lianjie(IPv)
        client.send(pack_v.encode('utf-8'))
        pack2c = recv_(client)
        if unpack_c(pack2c)==True:
            return True
        else:
            client.close()


def unpack_c(pack):
    length = int(pack[0:4])
    data = pack[4:4+length]
    C = pack[-258*3:-258*2]
    key = pack[-258*2:]
    print("data",data)

    de_data = Des(data,Kc2v,1)
    print("de_data",de_data)
    print("key",key)
    if yanzheng(data,C,key)==True:
        print("RSA验证成功")
        print("kerberos验证成功")
        return True






def unpack_tgs(tgs_pack):
    length = tgs_pack[0:4]
    length = int(length)
    data = tgs_pack[4:4+length]
    data = Des(data,Kc2tgs,1)
    global Kc2v
    Kc2v = data[0:8]
    IDv = data[8:23]
    TS4 =data[23:33]
    global Ticketv
    Ticketv = data[33:]
    C = tgs_pack[-258*3:-258*2]
    key = tgs_pack[-258*2:]
    if yanzheng(data,C,key)==True:
        print("来自tgs的验证成功")



def pack2v(Ticketv):
    TS5 = str(int(time.time()))
    Authenticatorc = Des("{:15}".format(IDc)+"{:15}".format(ADc)+TS5,Kc2v,0)
    data = Ticketv + Authenticatorc
    length = str(len(Ticketv))
    (C,d,n) = qianming(data)
    pack_v = "{:4}".format(length)+data+"{:258}".format(C)+"{:258}".format(d)+"{:258}".format(n)
    return pack_v

def kaishi(user,mima):
    # 创建客户端对象
    global client ,IDc,ADc,IDv,IPtgs,IDtgs,IPv,host,port, Kc,Ts3
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    IDc = str(socket.gethostname())  # 本机名字用于签名认证
    ADc = socket.gethostbyname(IDc)  # 本机地址
    IDv = '1234455'
    IPtgs = '192.168.1.101'
    IDtgs = '1234'  # 乱设置的
    IPv = '192.168.1.108'
    # 目标主机
    # host = input('输入目标ip')
    host = '192.168.1.107'
    # 目标端口
    port = 9090

    # 连接客户端
    client.connect((host, port))

    print('-' * 5 + '已连接到服务器' + '-' * 5)
    Kc = ''
    Ts3 = ''
    logging(user,mima)
    pack1 = recv_basic(client)
    print("123")
    print("pack1",pack1)
    result = unpack_(pack1)
    return result

'''user=input()
mima=input()
kaishi(user,mima)'''


