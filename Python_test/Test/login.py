# -*- coding: utf_8 -*-

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import QtCore, QtGui
import json, socket, time, sys, PyQt4
import Test.main,Test.manage

try:    
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(400, 292)
        Dialog.setSizeGripEnabled(True)
        self.dialog = Dialog
        self.lineEdit = QtGui.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(130, 100, 191, 21))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_2 = QtGui.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(130, 150, 191, 20))
        self.lineEdit_2.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(80, 100, 31, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(80, 150, 31, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(140, 50, 151, 21))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(170, 200, 75, 31))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton.clicked.connect(self.print)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", "账号", None))
        self.label_2.setText(_translate("Dialog", "密码", None))
        self.label_3.setText(_translate("Dialog", "欢迎来到银行管理系统", None))
        self.pushButton.setText(_translate("Dialog", "登陆", None))
        
    def print(self):
        
        str1 = self.lineEdit.text()
        str2 = self.lineEdit_2.text()
        if(str1=='root' and str2=='root'):
            self.dialog.hide()
            MainWindow1 = QtGui.QMainWindow()
            ui = Test.manage.Ui_MainWindow()
            ui.setupUi(MainWindow1)
            MainWindow1.show()
                
            MainWindow1.focusInEvent() 
            
        else:    
            str_dict = {"username" : str1, "password" : str2}
            out = json.dumps(str_dict).encode(encoding='utf_8')
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect(('localhost', 8002))
            sock.send(b'1')
            time.sleep(1)
            sock.send(out)
            if(sock.recv(1024).decode('utf_8')=='1'):
            #QtCore.QObject.connect( self.pushButton, QtCore.SIGNAL("clicked()"), self, QtCore.SLOT(quit()))
                
                self.dialog.hide()
                MainWindow = QtGui.QMainWindow()
                ui = Test.main.Ui_MainWindow()
                ui.setupUi(MainWindow)
                MainWindow.show()
                
                MainWindow.focusInEvent()   #ʹ保持的方法！
                
                
                
            else:
                msg_box = QMessageBox(QMessageBox.Warning, "登陆失败", "账户名或密码错误")
                msg_box.exec_()
                
            sock.close()
        
if __name__ == "__main__":

    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui =Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
    