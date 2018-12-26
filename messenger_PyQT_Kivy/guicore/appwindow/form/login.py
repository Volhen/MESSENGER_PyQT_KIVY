# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'aut2.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow_Login(object):

    def setupUi_login(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(370, 360)
        MainWindow.setMinimumSize(QtCore.QSize(370, 360))
        MainWindow.setMaximumSize(QtCore.QSize(370, 360))

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(0, 0, 370, 365))
        self.graphicsView.setMinimumSize(QtCore.QSize(370, 365))
        self.graphicsView.setMaximumSize(QtCore.QSize(370, 360))
        self.graphicsView.setStyleSheet(
            "background-image: url(src/img/log.png); background-position: center; background-repeat: no-repeat;")
        self.graphicsView.setObjectName("graphicsView")

        self.setlog = QtWidgets.QLineEdit(self.centralwidget)
        self.setlog.setGeometry(QtCore.QRect(42, 132, 295, 30))
        self.setlog.setObjectName("setlog")

        self.setpass = QtWidgets.QLineEdit(self.centralwidget)
        self.setpass.setGeometry(QtCore.QRect(42, 235, 295, 30))
        self.setpass.setObjectName("setpass")
        self.setpass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.setpass.setStyleSheet('lineedit-password-character: 9679')

        self.btn_log = QtWidgets.QPushButton(self.centralwidget)
        self.btn_log.setGeometry(QtCore.QRect(200, 302, 151, 41))
        self.btn_log.setStyleSheet("#btn_log {border:none;     background-image: url(src/img/btn.jpg); background-position: center; background-repeat: no-repeat;}\n"
                                   "\n"
                                   "#btn_log:hover {border:none;     background-image:url(src/img/hover_btn.jpg); background-position: center; background-repeat: no-repeat;}\n"
                                   "\n"
                                   "#btn_log:pressed {border:none;     background-image: url(src/img/push_btn.png); background-position: center; background-repeat: no-repeat;}\n"
                                   )
        self.btn_log.setText("")
        self.btn_log.setObjectName("btn_log")
        self.btn_reg = QtWidgets.QPushButton(self.centralwidget)

        self.btn_reg.setGeometry(QtCore.QRect(220, 10, 151, 41))
        self.btn_reg.setStyleSheet("#btn_reg {border:none;     background-image: url(src/img/register.png); background-position: center; background-repeat: no-repeat;}\n"
                                   "\n"
                                   "#btn_reg:hover {border:none;     background-image:url(src/img/register_hover.png); background-position: center; background-repeat: no-repeat;}\n"
                                   "\n"
                                   "#btn_reg:pressed {border:none;     background-image:url(src/img/register_press.png); background-position: center; background-repeat: no-repeat;}\n"
                                   )
        self.btn_reg.setText("")
        self.btn_reg.setObjectName("btn_reg")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
