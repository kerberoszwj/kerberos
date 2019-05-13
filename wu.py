# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wu.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
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

        self.retranslateUi(Form)
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

