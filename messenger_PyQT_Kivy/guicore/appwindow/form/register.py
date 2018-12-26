# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'reg.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow_Register(object):
    
    def setupUi_register(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(370, 390)
        MainWindow.setMinimumSize(QtCore.QSize(370, 390))
        MainWindow.setMaximumSize(QtCore.QSize(370, 390))

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(0, 0, 370, 390))
        self.graphicsView.setMinimumSize(QtCore.QSize(370, 390))
        self.graphicsView.setMaximumSize(QtCore.QSize(370, 390))
        self.graphicsView.setStyleSheet(
            "background-image: url(src/img/regi_win.png); background-position: center; background-repeat: no-repeat;")
        self.graphicsView.setObjectName("graphicsView")

        self.btn_log = QtWidgets.QPushButton(self.centralwidget)
        self.btn_log.setGeometry(QtCore.QRect(200, 320, 151, 42))
        self.btn_log.setStyleSheet("#btn_log {border:none;     background-image: url(src/img/btn_reg.png); background-position: center; background-repeat: no-repeat;}\n"
                                   "\n"
                                   "#btn_log:hover {border:none;     background-image:url(src/img/btn_reg_hover.png); background-position: center; background-repeat: no-repeat;}\n"
                                   "\n"
                                   "#btn_log:pressed {border:none;     background-image: url(src/img/btn_reg_press.png); background-position: center; background-repeat: no-repeat;}\n"
                                   )
        self.btn_log.setText("")
        self.btn_log.setObjectName("btn_log")

        self.setlog = QtWidgets.QLineEdit(self.centralwidget)
        self.setlog.setGeometry(QtCore.QRect(48, 90, 295, 30))
        self.setlog.setObjectName("setlog")

        self.setpass = QtWidgets.QLineEdit(self.centralwidget)
        self.setpass.setGeometry(QtCore.QRect(48, 177, 295, 30))
        self.setpass.setObjectName("setpass")
        self.setpass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.setpass.setStyleSheet('lineedit-password-character: 9679')

        self.setconfirm = QtWidgets.QLineEdit(self.centralwidget)
        self.setconfirm.setGeometry(QtCore.QRect(48, 261, 295, 30))
        self.setconfirm.setObjectName("setconfirm")
        self.setconfirm.setEchoMode(QtWidgets.QLineEdit.Password)
        self.setconfirm.setStyleSheet('lineedit-password-character: 9679')

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
