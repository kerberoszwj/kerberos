import rsa2
import hashlib
import socket
import time
import random
import pymysql
import socket,threading
from Common import *
'''a='123'
db  = pymysql.connect('localhost','root', '', 'keberos')
cursor = db.cursor()
cursor.execute('select * from users where user = %s',(a,))
myresult = cursor.fetchall()
for x in myresult:
    id=x[0]
print(id)
db.close()'''
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 9090
server.bind((host, port))
server.listen(5)
Ktgs='12345678' #tgs 和 AS共有的 自己设置的
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
    length=pack[0:4]
    length=int(length)
    len_data=length-(258*3+10+15*2)
    a=pack[4:4+len_data]
    user=a.split()[0]
    mima=a.split()[1]
    IDc =pack[4+len_data:15+4+len_data]
    IDtgs = pack[19+len_data:15+19+len_data]
    ts = pack[-258*3-10:-258*3]
    C=pack[-258*3:-258*2]
    data=pack[4:15+19+10+len_data]
    print(C)
    key=pack[-258*2:]
    if yanzheng(data,C,key)==True:
        print("RSA验证成功")
        if logging(user,mima)==True:
            print("有此用户")
            pack=fengbao(mima,IDtgs,IDc)
            client.send(pack.encode('utf-8'))

def fengbao(mima,IDtgs,IDc):
    Kc2tgs=getRandomKey() #随机生成的C发给tgs的
    Lifetime2='1000'
    len_mima=len(mima)
    while len_mima<8:
        mima=mima+'0'
        len_mima=len_mima+1
    Kc = mima
    TS2 = time.time()
    TS2 = str(int(TS2))
    ADc = addr
    Tickettgs=Des(Kc2tgs+"{:15}".format(IDc)+"{:15}".format(ADc)+"{:15}".format(IDtgs)+TS2+"{:4}".format(Lifetime2),Ktgs,0)
    print("加密前",Kc2tgs+"{:15}".format(IDtgs)+TS2+Lifetime2+Tickettgs)
    pack=Des(Kc2tgs+"{:15}".format(IDtgs)+TS2+Lifetime2+Tickettgs,mima,0)
    print("加密后的",pack)
    (C,d,n)=qianming(pack)
    print("Kc",Kc)
    length="{:4}".format(len(pack))
    pack=length + pack  + "{:258}".format(C)+"{:258}".format(d)+"{:258}".format(n)
    print(pack)
    return pack





def getRandomKey():
    key = ''
    for i in range(8):
        char = chr(random.randrange(32,127))
        key += char
    return key



def logging(user,mima):
    db = pymysql.connect('localhost', 'root', '', 'keberos')
    cursor = db.cursor()
    cursor.execute('select * from users where user = %s', (user,))
    myresult = cursor.fetchall()
    password = ''
    for x in myresult:
        password = x[2]
    db.close()
    if password == mima :
        return True
    else:
        return False




(pack,addr,client)=jieshou()
unpack(pack)



