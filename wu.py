# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wu.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

import socket, threading,_thread
import time
from Common import *

class Ui_Form(QtWidgets.QMainWindow):

    def __init__(self):
        super(Ui_Form, self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        str_up = self.textEdit_3.placeholderText()
        self.client1 = None
        self.xiaoxi = list()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(749, 873)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(550, 70, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(100, 220, 211, 181))
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(170, 160, 72, 15))
        self.label.setMinimumSize(QtCore.QSize(72, 15))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(90, 80, 101, 31))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(370, 80, 113, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(10, 90, 72, 15))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(280, 90, 72, 15))
        self.label_3.setObjectName("label_3")
        self.textEdit_2 = QtWidgets.QTextEdit(Form)
        self.textEdit_2.setGeometry(QtCore.QRect(430, 220, 191, 181))
        self.textEdit_2.setObjectName("textEdit_2")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(490, 170, 72, 15))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(90, 480, 211, 16))
        self.label_5.setObjectName("label_5")
        self.textEdit_3 = QtWidgets.QTextEdit(Form)
        self.textEdit_3.setGeometry(QtCore.QRect(40, 530, 461, 131))
        self.textEdit_3.setObjectName("textEdit_3")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(560, 630, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(100, 690, 72, 15))
        self.label_6.setObjectName("label_6")
        self.textEdit_4 = QtWidgets.QTextEdit(Form)
        self.textEdit_4.setGeometry(QtCore.QRect(40, 740, 651, 101))
        self.textEdit_4.setObjectName("textEdit_4")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(560, 690, 93, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(550, 120, 93, 28))
        self.pushButton_4.setObjectName("pushButton_4")

        #self.retranslateUi(Form)
        self.pushButton.clicked.connect(Form.slot1)
        self.pushButton_2.clicked.connect(Form.slot2)
        self.pushButton_4.clicked.connect(self.lineEdit_2.clear)
        self.pushButton_4.clicked.connect(self.lineEdit.clear)
        self.pushButton_4.clicked.connect(self.textEdit.clear)
        self.pushButton_3.clicked.connect(self.textEdit_4.clear)
        self.pushButton_3.clicked.connect(self.textEdit_3.clear)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "connect"))
        self.label.setText(_translate("Form", "Status"))
        self.label_2.setText(_translate("Form", "Account"))
        self.label_3.setText(_translate("Form", "password"))
        self.label_4.setText(_translate("Form", "Data"))
        self.label_5.setText(_translate("Form", "input you message here"))
        self.pushButton_2.setText(_translate("Form", "send"))
        self.label_6.setText(_translate("Form", "message:"))
        self.pushButton_3.setText(_translate("Form", "clear"))
        self.pushButton_4.setText(_translate("Form", "clear"))

    def fengzhuang(self, data):
        length = "{:4}".format(str(len(data)))
        print(length + data)
        a = length + data
        return a

    def logging(self, user, mima):

        # 输入账号密码

        ts = time.time()
        ts = str(int(ts))
        a = user + ' ' + mima + "{:15}".format(IDc) + "{:15}".format(IDtgs) + ts
        (C, d, n) = qianming(a)
        data = a + "{:258}".format(C) + "{:258}".format(d) + "{:258}".format(n)
        print(data)
        out = self.fengzhuang(data)
        # 发送给服务器
        print(out)
        client.send(out.encode('utf-8'))
        len_mima = len(mima)
        while len_mima < 8:
            mima = mima + '0'
            len_mima = len_mima + 1
        global Kc
        Kc = mima

    def recv_basic(self, client):

        data_1 = (client.recv(2048)).decode('utf-8')

        client.close()
        return data_1

    def myrecv_(self):
        print('threadfunction')
        while True:
            data = (self.client1.recv(2048)).decode('utf-8')
            print(data)
            self.xiaoxi.append(data)
            print("123")
            print(self.xiaoxi)

    def recv_(self, client):
        total_data = ''
        data = (client.recv(2048)).decode('utf-8')

        return data

    '''def indatas():
            # 接受来自服务器的信息
        try:
            indata = (client.recv()).decode('utf-8')
            print(indata)
        except Exception as e:
            print("没收到AS的回复")'''

    def jiance(self, C, key, undata, Ts2, Lifetime2, Ts3):  # 检测时间戳和RSA验证
        a = 0
        if yanzheng(undata, C, key) == True:
            print("签名验证成功")
            a = a + 1
        '''print(Ts3)
        Ts3=int(Ts3)
        Ts2=int(Ts2)
        Lifetime2 = int(Lifetime2)
        print(Ts3,Ts2,Lifetime2)'''
        if int(Ts3) - int(Ts2) < int(Lifetime2):
            a = a + 1
        return a

    def lianjie(self, ip):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        port = 9090
        client.connect((ip, port))
        print("连接成功")
        return client

    def pack_(self, Ticekttgs, Kc2tgs, Ts3):
        Authenticator = Des("{:15}".format(IDv) + "{:15}".format(ADc) + Ts3, Kc2tgs, 0)
        print('auth', Authenticator)
        data = "{:15}".format(IDv) + Ticekttgs + Authenticator
        length = "{:4}".format(str(len(Ticekttgs)))
        (C, d, n) = qianming(data)
        pack = length + data + "{:258}".format(C) + "{:258}".format(d) + "{:258}".format(n)
        return pack

    def unpack_(self, pack):
        length = int(pack[0:4])
        data = pack[4:4 + length]
        print("data", data)
        C = pack[-258 * 3:-258 * 2]
        key = pack[-258 * 2:]
        undata = data
        data = Des(data, Kc, 1)
        global Kc2tgs
        Kc2tgs = data[0:8]
        IDtgs = data[8:23]
        Ts2 = data[23:33]
        # global Ts3
        Ts3 = time.time()
        Ts3_ = str(int(Ts3))
        Lifetime2 = data[33:37]
        Tickettgs = data[37:]
        if self.jiance(C, key, undata, Ts2, Lifetime2, Ts3_) == 2:
            print("成功")
            pack2tgs = self.pack_(Tickettgs, Kc2tgs, Ts3_)
            print("pack2tgs", pack2tgs)
            client = self.lianjie(IPtgs)
            client.send(pack2tgs.encode('utf-8'))
            print("已发送")
            tgs_pack = self.recv_basic(client)
            self.unpack_tgs(tgs_pack)
            pack_v = self.pack2v(Ticketv)
            client1 = self.lianjie(IPv)

            print("client1", client1)
            client1.send(pack_v.encode('utf-8'))
            print('137')
            pack2c = self.recv_(client1)
            if self.unpack_c(pack2c) == True:
                return 1, client1
            else:
                client1.close()

    def unpack_c(self, pack):
        length = int(pack[0:4])
        data = pack[4:4 + length]
        C = pack[-258 * 3:-258 * 2]
        key = pack[-258 * 2:]
        print("data", data)

        de_data = Des(data, Kc2v, 1)
        print("de_data", de_data)
        print("key", key)
        if yanzheng(data, C, key) == True:
            print("RSA验证成功")
            print("kerberos验证成功")
            return True

    def unpack_tgs(self, tgs_pack):
        length = tgs_pack[0:4]
        length = int(length)
        data = tgs_pack[4:4 + length]
        data = Des(data, Kc2tgs, 1)
        global Kc2v
        Kc2v = data[0:8]
        IDv = data[8:23]
        TS4 = data[23:33]
        global Ticketv
        Ticketv = data[33:]
        C = tgs_pack[-258 * 3:-258 * 2]
        key = tgs_pack[-258 * 2:]
        if yanzheng(data, C, key) == True:
            print("来自tgs的验证成功")

    def pack2v(self, Ticketv):
        TS5 = str(int(time.time()))
        Authenticatorc = Des("{:15}".format(IDc) + "{:15}".format(ADc) + TS5, Kc2v, 0)
        data = Ticketv + Authenticatorc
        length = str(len(Ticketv))
        (C, d, n) = qianming(data)
        pack_v = "{:4}".format(length) + data + "{:258}".format(C) + "{:258}".format(d) + "{:258}".format(n)
        return pack_v

    def kaishi(self, user, mima):
        # 创建客户端对象
        global client, IDc, ADc, IDv, IPtgs, IDtgs, IPv, host, port, Kc, Ts3
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        IDc = str(socket.gethostname())  # 本机名字用于签名认证
        ADc = socket.gethostbyname(IDc)  # 本机地址
        IDv = '1234455'
        IPtgs = '192.168.1.111'
        IDtgs = '1234'  # 乱设置的
        IPv = '192.168.1.114'
        # 目标主机
        # host = input('输入目标ip')
        host = '192.168.1.110'
        # 目标端口
        port = 9090

        # 连接客户端
        client.connect((host, port))

        print('-' * 5 + '已连接到服务器' + '-' * 5)
        Kc = ''
        Ts3 = ''
        self.logging(user, mima)
        pack1 = self.recv_basic(client)
        print("123")
        print("pack1", pack1)
        (result, self.client1) = self.unpack_(pack1)
        return result, self.client1

    def fasong(self, data_, client1):

        length = len(data_)
        length = str(length)
        data = Des(data_, Kc2v, 0)
        print("Kc2v", Kc2v)
        print("data", data)
        (C, d, n) = qianming(data)
        print("data111", data)
        data = "{:4}".format(length) + "{:15}".format(IDc) + data + "{:258}".format(C) + "{:258}".format(
            d) + "{:258}".format(n)
        print("data", data)
        # print("client", client1)
        print("连接成功")
        bianliang = self.client1.send(data.encode('utf-8'))

        print("发了")
        # t = threading.Thread(target=self.myrecv_, args=(client1,))
        #self.textEdit_4.clear()
        #self.textEdit_4.setPlainText('123')
        try:
            _thread.start_new_thread(self.myrecv_, ())
        except:
            print('线程错误')
        # t.start()
        # t.join()
        #print('230')

    def recv_data(self, client):
        while True:
            try:
                indata = client.recvall()
            except Exception as e:
                break
            print(indata.decode('utf-8'))

    # 定义槽函数
    def slot1(self):
        # global client1
        (result, self.client1) = self.kaishi(self.lineEdit.text(), self.lineEdit_2.text())
        if result == 1:
            self.textEdit.setText(" 登入正确")
            self.textEdit_2.setText(" ")


        else:
            self.textEdit.setText(" 请用户重新输入")

    def slot2(self):

        yi = self.textEdit_3.toPlainText()

        self.fasong(yi, self.client1)
        self.textEdit_4.clear()
        messageStr = ''
        time.sleep(0.5)
        for i in self.xiaoxi:
            messageStr += i + '\n'
        print(self.xiaoxi)
        self.textEdit_4.setText(messageStr)

        #self.textEdit_2.setText()
        # ios=self.textEdit_4.toPlainText()

        # self.textEdit_4.setText()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Ui_Form()
    window.show()
    sys.exit(app.exec_())


