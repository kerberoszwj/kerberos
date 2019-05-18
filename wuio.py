from PyQt5 import QtWidgets, QtGui
import sys
from client import *


from wu import Ui_Form    # 导入生成form.py里生成的类

class mywindow(QtWidgets.QWidget,Ui_Form):
    def __init__(self):
        super(mywindow,self).__init__()
        self.setupUi(self)
        str_up = self.textEdit_3.placeholderText()

    #定义槽函数
    def slot1(self):
        if kaishi(self.lineEdit.text(),self.lineEdit_2.text())==True:
           self.textEdit.setText(" 登入正确")
           self.textEdit_2.setText(" ")


        else:
            self.textEdit.setText(" 请用户重新输入")



    def  slot2(self):

       str="ffffffffffffffff"
       yi=self.textEdit_3.toPlainText()

       ios=self.textEdit_4.toPlainText()
       self.textEdit_4.setText( ios+yi+str)





if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = mywindow()
    window.show()
    sys.exit(app.exec_())
