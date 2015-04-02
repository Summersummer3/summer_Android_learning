# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\ui\Main_ui.ui'
#
# Created: Sat Jan 17 00:33:40 2015
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import json
import socket
import time
from PyQt4.QtGui import QMessageBox


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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(555, 417)
        
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        
        self.tabWidget = QtGui.QTabWidget(self.centralWidget)
        self.tabWidget.setGeometry(QtCore.QRect(30, 20, 491, 361))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        
        self.lineEdit = QtGui.QLineEdit(self.tab)
        self.lineEdit.setGeometry(QtCore.QRect(80, 40, 371, 21))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_2 = QtGui.QLineEdit(self.tab)
        self.lineEdit_2.setGeometry(QtCore.QRect(80, 80, 371, 21))
        self.lineEdit_2.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.lineEdit_3 = QtGui.QLineEdit(self.tab)
        self.lineEdit_3.setGeometry(QtCore.QRect(80, 120, 371, 21))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.lineEdit_4 = QtGui.QLineEdit(self.tab)
        self.lineEdit_4.setGeometry(QtCore.QRect(80, 160, 371, 21))
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.comboBox = QtGui.QComboBox(self.tab)
        self.comboBox.setGeometry(QtCore.QRect(80, 200, 69, 22))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.lineEdit_5 = QtGui.QLineEdit(self.tab)
        self.lineEdit_5.setGeometry(QtCore.QRect(210, 200, 241, 20))
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.label = QtGui.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(30, 40, 41, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(30, 80, 41, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(20, 120, 51, 20))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(30, 160, 41, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(20, 200, 51, 20))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self.tab)
        self.label_6.setGeometry(QtCore.QRect(160, 200, 41, 21))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.pushButton = QtGui.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(200, 280, 75, 41))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        
        self.pushButton.clicked.connect(self.buttonaction_1)
        
        self.lineEdit_6 = QtGui.QLineEdit(self.tab)
        self.lineEdit_6.setGeometry(QtCore.QRect(210, 240, 241, 20))
        self.lineEdit_6.setObjectName(_fromUtf8("lineEdit_6"))
        self.label_7 = QtGui.QLabel(self.tab)
        self.label_7.setGeometry(QtCore.QRect(160, 240, 41, 21))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.comboBox_2 = QtGui.QComboBox(self.tab)
        self.comboBox_2.setGeometry(QtCore.QRect(80, 240, 69, 22))
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.label_8 = QtGui.QLabel(self.tab)
        self.label_8.setGeometry(QtCore.QRect(20, 240, 54, 21))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        
        
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.lineEdit_7 = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_7.setGeometry(QtCore.QRect(110, 80, 301, 20))
        self.lineEdit_7.setObjectName(_fromUtf8("lineEdit_7"))
        self.lineEdit_8 = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_8.setGeometry(QtCore.QRect(110, 140, 301, 20))
        self.lineEdit_8.setObjectName(_fromUtf8("lineEdit_8"))
        self.lineEdit_8.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEdit_9 = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_9.setGeometry(QtCore.QRect(110, 200, 301, 20))
        self.lineEdit_9.setObjectName(_fromUtf8("lineEdit_9"))
        self.lineEdit_9.setEchoMode(QtGui.QLineEdit.Password)
        self.label_9 = QtGui.QLabel(self.tab_2)
        self.label_9.setGeometry(QtCore.QRect(30, 80, 54, 21))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_10 = QtGui.QLabel(self.tab_2)
        self.label_10.setGeometry(QtCore.QRect(30, 140, 54, 21))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.label_11 = QtGui.QLabel(self.tab_2)
        self.label_11.setGeometry(QtCore.QRect(30, 200, 54, 21))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.pushButton_2 = QtGui.QPushButton(self.tab_2)
        self.pushButton_2.setGeometry(QtCore.QRect(190, 260, 75, 31))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        
        self.pushButton_2.clicked.connect(self.buttonaction_2)
        
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.lineEdit_10 = QtGui.QLineEdit(self.tab_3)
        self.lineEdit_10.setGeometry(QtCore.QRect(100, 80, 301, 20))
        self.lineEdit_10.setObjectName(_fromUtf8("lineEdit_10"))
        self.lineEdit_11 = QtGui.QLineEdit(self.tab_3)
        self.lineEdit_11.setGeometry(QtCore.QRect(100, 140, 301, 20))
        self.lineEdit_11.setObjectName(_fromUtf8("lineEdit_11"))
        self.lineEdit_11.setEchoMode(QtGui.QLineEdit.Password)
        self.pushButton_3 = QtGui.QPushButton(self.tab_3)
        self.pushButton_3.setGeometry(QtCore.QRect(190, 210, 75, 31))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        
        self.pushButton_3.clicked.connect(self.buttonaction_3)
        
        self.label_12 = QtGui.QLabel(self.tab_3)
        self.label_12.setGeometry(QtCore.QRect(23, 80, 61, 21))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.label_13 = QtGui.QLabel(self.tab_3)
        self.label_13.setGeometry(QtCore.QRect(40, 140, 31, 21))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.lineEdit_12 = QtGui.QLineEdit(self.tab_4)
        self.lineEdit_12.setGeometry(QtCore.QRect(120, 100, 301, 21))
        self.lineEdit_12.setObjectName(_fromUtf8("lineEdit_12"))
        self.lineEdit_13 = QtGui.QLineEdit(self.tab_4)
        self.lineEdit_13.setGeometry(QtCore.QRect(270, 160, 151, 21))
        self.lineEdit_13.setObjectName(_fromUtf8("lineEdit_13"))
        self.comboBox_3 = QtGui.QComboBox(self.tab_4)
        self.comboBox_3.setGeometry(QtCore.QRect(120, 160, 69, 22))
        self.comboBox_3.setObjectName(_fromUtf8("comboBox_3"))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.setItemText(4, _fromUtf8(""))
        self.label_14 = QtGui.QLabel(self.tab_4)
        self.label_14.setGeometry(QtCore.QRect(23, 100, 61, 21))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.label_15 = QtGui.QLabel(self.tab_4)
        self.label_15.setGeometry(QtCore.QRect(30, 160, 51, 21))
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.label_16 = QtGui.QLabel(self.tab_4)
        self.label_16.setGeometry(QtCore.QRect(220, 160, 31, 21))
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.pushButton_4 = QtGui.QPushButton(self.tab_4)
        self.pushButton_4.setGeometry(QtCore.QRect(180, 240, 75, 31))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.pushButton_4.clicked.connect(self.buttonaction_4)
        self.tabWidget.addTab(self.tab_4, _fromUtf8(""))
        
        self.tab_5 = QtGui.QWidget()
        self.tab_5.setObjectName(_fromUtf8("tab_5"))
        self.lineEdit_14 = QtGui.QLineEdit(self.tab_5)
        self.lineEdit_14.setGeometry(QtCore.QRect(120, 80, 301, 21))
        self.lineEdit_14.setObjectName(_fromUtf8("lineEdit_14"))
        self.lineEdit_15 = QtGui.QLineEdit(self.tab_5)
        self.lineEdit_15.setGeometry(QtCore.QRect(120, 130, 301, 21))
        self.lineEdit_15.setObjectName(_fromUtf8("lineEdit_15"))
        self.lineEdit_15.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEdit_16 = QtGui.QLineEdit(self.tab_5)
        self.lineEdit_16.setGeometry(QtCore.QRect(120, 180, 301, 21))
        self.lineEdit_16.setObjectName(_fromUtf8("lineEdit_16"))
        self.label_17 = QtGui.QLabel(self.tab_5)
        self.label_17.setGeometry(QtCore.QRect(40, 80, 54, 21))
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.label_18 = QtGui.QLabel(self.tab_5)
        self.label_18.setGeometry(QtCore.QRect(40, 130, 54, 21))
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.label_19 = QtGui.QLabel(self.tab_5)
        self.label_19.setGeometry(QtCore.QRect(40, 180, 54, 21))
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.pushButton_5 = QtGui.QPushButton(self.tab_5)
        self.pushButton_5.setGeometry(QtCore.QRect(180, 240, 75, 31))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        
        self.pushButton_5.clicked.connect(self.buttonaction_5)
        
        self.tabWidget.addTab(self.tab_5, _fromUtf8(""))

        self.tab_6 = QtGui.QWidget()
        self.tab_6.setObjectName(_fromUtf8("tab_6"))
        self.lineEdit_17 = QtGui.QLineEdit(self.tab_6)
        self.lineEdit_17.setGeometry(QtCore.QRect(130, 90, 301, 21))
        self.lineEdit_17.setObjectName(_fromUtf8("lineEdit_17"))
        self.lineEdit_18 = QtGui.QLineEdit(self.tab_6)
        self.lineEdit_18.setGeometry(QtCore.QRect(130, 160, 301, 21))
        self.lineEdit_18.setObjectName(_fromUtf8("lineEdit_18"))
        self.lineEdit_18.setEchoMode(QtGui.QLineEdit.Password)
        self.label_20 = QtGui.QLabel(self.tab_6)
        self.label_20.setGeometry(QtCore.QRect(40, 90, 54, 21))
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.label_21 = QtGui.QLabel(self.tab_6)
        self.label_21.setGeometry(QtCore.QRect(40, 160, 54, 21))
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.pushButton_6 = QtGui.QPushButton(self.tab_6)
        self.pushButton_6.setGeometry(QtCore.QRect(200, 240, 75, 31))
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        
        self.pushButton_6.clicked.connect(self.buttonaction_6)
        
        self.tabWidget.addTab(self.tab_6, _fromUtf8(""))
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "银行管理系统", None))
        self.comboBox.setItemText(0, _translate("MainWindow", "身份证", None))
        self.comboBox.setItemText(1, _translate("MainWindow", "军官证", None))
        self.comboBox.setItemText(2, _translate("MainWindow", "其他", None))
        self.label.setText(_translate("MainWindow", "账户名", None))
        self.label_2.setText(_translate("MainWindow", "密码", None))
        self.label_3.setText(_translate("MainWindow", "手机号码", None))
        self.label_4.setText(_translate("MainWindow", "地址", None))
        self.label_5.setText(_translate("MainWindow", "证件类型", None))
        self.label_6.setText(_translate("MainWindow", "证件号", None))
        self.pushButton.setText(_translate("MainWindow", "确定", None))
        self.label_7.setText(_translate("MainWindow", "预存款", None))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "活期", None))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "定期半年", None))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "定期一年", None))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "定期三年", None))
        self.label_8.setText(_translate("MainWindow", "储蓄类型", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "开户", None))
        self.label_9.setText(_translate("MainWindow", "证件号", None))
        self.label_10.setText(_translate("MainWindow", "密码", None))
        self.label_11.setText(_translate("MainWindow", "修改密码", None))
        self.pushButton_2.setText(_translate("MainWindow", "确定", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "修改密码", None))
        self.pushButton_3.setText(_translate("MainWindow", "确定挂失", None))
        self.label_12.setText(_translate("MainWindow", "挂失证件号", None))
        self.label_13.setText(_translate("MainWindow", "密码", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "账号挂失", None))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "活期", None))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "定期半年", None))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "定期一年", None))
        self.comboBox_3.setItemText(3, _translate("MainWindow", "定期三年", None))
        self.label_14.setText(_translate("MainWindow", "存款证件号", None))
        self.label_15.setText(_translate("MainWindow", "存款方式", None))
        self.label_16.setText(_translate("MainWindow", "金额", None))
        self.pushButton_4.setText(_translate("MainWindow", "确定存款", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "存款", None))
        self.label_17.setText(_translate("MainWindow", "取款账号", None))
        self.label_18.setText(_translate("MainWindow", "密码", None))
        self.label_19.setText(_translate("MainWindow", "金额", None))
        self.pushButton_5.setText(_translate("MainWindow", "确定取款", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "取款", None))
        self.label_20.setText(_translate("MainWindow", "注销账号", None))
        self.label_21.setText(_translate("MainWindow", "密码", None))
        self.pushButton_6.setText(_translate("MainWindow", "确定注销", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("MainWindow", "取消账号", None))
    
    def buttonaction_1(self):
        try:
            str1 = self.lineEdit.text()
            str2 = self.lineEdit_2.text()
            str3 = int(self.lineEdit_3.text())
            str4 = self.lineEdit_4.text()
            str5 = self.comboBox.currentText()
            str6 = int(self.lineEdit_5.text())
            str7 = "1"
            str8 = int(self.lineEdit_6.text())
            str9 = self.comboBox_2.currentText()
            if(str8<10):
                msg_box = QMessageBox(QMessageBox.Warning, "失败", "存款金额不得小于10元")
                msg_box.exec_()
            else:    
                info_dict = {"username":str1,"password":str2,"phoneno":str3,"address":str4,
                             "idtype":str5,"idno":str6,"situation":str7,"money":str8,"type":str9}
                out = json.dumps(info_dict).encode(encoding='utf_8')
                sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                sock.connect(('localhost',8002))
                sock.send(b'2')
                time.sleep(1)
                sock.send(out)
                flag = sock.recv(1024).decode('utf_8')
                if(flag == '1'):
                
                    msg_box = QMessageBox(QMessageBox.Warning, "提示", "操作成功")
                    msg_box.exec_()
                
                else:
                    if(flag == '0'):
                        msg_box = QMessageBox(QMessageBox.Warning, "提示", "操作失败，账号已存在")
                        msg_box.exec_()
                    else:
                        msg_box = QMessageBox(QMessageBox.Warning, "提示", "操作失败，用户名、密码和证件号不得为空")
                        msg_box.exec_()
                sock.close()
                
        except ValueError:
            
            msg_box = QMessageBox(QMessageBox.Warning, "提示", "操作失败，请检查格式！")
            msg_box.exec_()
            
    def buttonaction_2(self):
        str1 = self.lineEdit_7.text()
        str2 = self.lineEdit_8.text()
        str3 = self.lineEdit_9.text()
        if(str1=='' or str2=='' or str3==''):
            msg_box = QMessageBox(QMessageBox.Warning, "提示", "操作失败，用户名和密码及修改密码不得为空")
            msg_box.exec_()
        else:    
            info_dict = {"idno":str1,"password":str2,"new_password":str3}
            out = json.dumps(info_dict).encode(encoding='utf_8')
            sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            sock.connect(('localhost',8002))
            sock.send(b'3')
            time.sleep(1)
            sock.send(out)
            if(sock.recv(1024).decode('utf_8')=='1'):
                msg_box = QMessageBox(QMessageBox.Warning, "提示", "密码修改成功")
                msg_box.exec_()
            else:
                msg_box = QMessageBox(QMessageBox.Warning, "提示", "原密码错误或修改失败")
                msg_box.exec_()
            sock.close()
                    
    def buttonaction_3(self):
        str1 = self.lineEdit_10.text()
        str2 = self.lineEdit_11.text()
        
        if(str1=='' or str2==''):
            msg_box = QMessageBox(QMessageBox.Warning, "提示", "操作失败，用户名和密码及修改密码不得为空")
            msg_box.exec_()
        else:
            info_dict = {"idno":str1,"password":str2}
            out = json.dumps(info_dict).encode(encoding='utf_8')
            sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            sock.connect(('localhost',8002))
            sock.send(b'4')
            time.sleep(1)
            sock.send(out)
            if(sock.recv(1024).decode('utf_8')=='1'):
                msg_box = QMessageBox(QMessageBox.Warning, "提示", "挂失成功")
                msg_box.exec_()
            else:
                msg_box = QMessageBox(QMessageBox.Warning, "提示", "原密码错误或挂失失败")
                msg_box.exec_()
            sock.close()
            
    def buttonaction_4(self):
        try:
            str1 = self.lineEdit_12.text()
            str2 = int(self.lineEdit_13.text())
            str3 = self.comboBox_3.currentText()
            
            if(str1=='' or str2==''):
                msg_box = QMessageBox(QMessageBox.Warning, "提示", "操作失败，用户名和密码及修改密码不得为空")
                msg_box.exec_()
            else:
                info_dict = {"idno":str1,"money":str2,"type":str3}
                out = json.dumps(info_dict).encode(encoding='utf_8')
                sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                sock.connect(('localhost',8002))
                sock.send(b'5')
                time.sleep(1)
                sock.send(out)
                flag = sock.recv(1024).decode('utf_8')
                if(flag=='1'):
                    msg_box = QMessageBox(QMessageBox.Warning, "提示", "存款成功")
                    msg_box.exec_()
                else:
                    if(flag=='2'):
                        msg_box = QMessageBox(QMessageBox.Warning, "提示", "账号不存在！")
                        msg_box.exec_()
                    else:
                        msg_box = QMessageBox(QMessageBox.Warning, "提示", "账号已被挂失！")
                        msg_box.exec_()
                sock.close()
                
        except ValueError:
            msg_box = QMessageBox(QMessageBox.Warning, "提示", "操作失败，金额请输入数字")
            msg_box.exec_()
        
    def buttonaction_5(self):
        try:
            str1 = self.lineEdit_14.text()
            str2 = self.lineEdit_15.text()
            str3 = int(self.lineEdit_16.text())
            
            
            if(str1=='' or str2=='' or str3==''):
                msg_box = QMessageBox(QMessageBox.Warning, "提示", "操作失败，用户名和密码及修改密码不得为空")
                msg_box.exec_()
            else:
                info_dict = {"idno":str1,"password":str2,"money":str3}
                out = json.dumps(info_dict).encode(encoding='utf_8')
                sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                sock.connect(('localhost',8002))
                sock.send(b'6')
                time.sleep(1)
                sock.send(out)
                flag = sock.recv(1024).decode('utf_8')
                if(flag=='1'):
                    msg_box = QMessageBox(QMessageBox.Warning, "提示", "取款成功")
                    msg_box.exec_()
                else:
                    if(flag=='2'):
                        msg_box = QMessageBox(QMessageBox.Warning, "提示", "账号或密码错误")
                        msg_box.exec_()
                    else:
                        if(flag=='3'):
                            msg_box = QMessageBox(QMessageBox.Warning, "提示", "取款失败，余额不足！")
                            msg_box.exec_()
                        else:    
                            msg_box = QMessageBox(QMessageBox.Warning, "提示", "账号已被挂失！")
                            msg_box.exec_()
                sock.close()
                
        except ValueError:
            msg_box = QMessageBox(QMessageBox.Warning, "提示", "操作失败，金额请输入数字")
            msg_box.exec_()
        
    def buttonaction_6(self):
        str1 = self.lineEdit_17.text()
        str2 = self.lineEdit_18.text()
        
        if(str1=='' or str2==''):
            msg_box = QMessageBox(QMessageBox.Warning, "提示", "操作失败，用户名和密码及修改密码不得为空")
            msg_box.exec_()
        else:
            info_dict = {"idno":str1,"password":str2}
            out = json.dumps(info_dict).encode(encoding='utf_8')
            sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            sock.connect(('localhost',8002))
            sock.send(b'7')
            time.sleep(1)
            sock.send(out)
            flag = sock.recv(1024).decode('utf_8')
            if(flag=='1'):
                msg_box = QMessageBox(QMessageBox.Warning, "提示", "注销成功")
                msg_box.exec_()
            else:
                if(flag=='2'):
                    msg_box = QMessageBox(QMessageBox.Warning, "提示", "原账号还有余额 无法注销")
                    msg_box.exec_()
                else:
                    msg_box = QMessageBox(QMessageBox.Warning, "提示", "账号或密码错误！")
                    msg_box.exec_()
            sock.close()
            
        


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    
    sys.exit(app.exec_())

