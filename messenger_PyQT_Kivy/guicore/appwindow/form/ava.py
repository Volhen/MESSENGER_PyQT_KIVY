# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ava_2.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow_profile(object):

    def setupUi_profile(self, MainWindow):

        MainWindow.setObjectName("User profile")
        MainWindow.resize(640, 479)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.gridLayout_4 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName("gridLayout_4")

        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_5.setObjectName("verticalLayout_5")

        self.line_7 = QtWidgets.QFrame(self.centralwidget)
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.verticalLayout_5.addWidget(self.line_7)
        
        self.display = QtWidgets.QLabel(self.centralwidget)
        self.display.setMinimumSize(QtCore.QSize(200, 300))
        self.display.setMaximumSize(QtCore.QSize(200, 300))
        self.display.setStyleSheet("background-image: url(src/avatar/ava_0.jpg); border: none; background-repeat: no-repeat; background-position: center;")
        self.display.setText("")
        self.display.setObjectName("display")
        self.display.setAlignment(QtCore.Qt.AlignCenter)
        self.verticalLayout_5.addWidget(self.display)


        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_5.addWidget(self.line_3)

        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")

        self.btn_rsc = QtWidgets.QPushButton(self.centralwidget)
        self.btn_rsc.setMinimumSize(QtCore.QSize(80, 25))
        self.btn_rsc.setMaximumSize(QtCore.QSize(50, 25))
        self.btn_rsc.setObjectName("btn_rsc")
        self.verticalLayout.addWidget(self.btn_rsc)

        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")

        self.label_size_zoom = QtWidgets.QLabel(self.centralwidget)
        self.label_size_zoom.setAlignment(QtCore.Qt.AlignCenter)
        self.label_size_zoom.setObjectName("size_zoom")
        self.label_size_zoom.setEnabled(False)
        self.gridLayout_2.addWidget(self.label_size_zoom, 0, 0, 1, 2)

        self.btn_zoom_out = QtWidgets.QPushButton(self.centralwidget)
        self.btn_zoom_out.setMaximumSize(QtCore.QSize(25, 25))
        self.btn_zoom_out.setObjectName("btn_zoom_out")
        self.btn_zoom_out.setEnabled(False)
        self.gridLayout_2.addWidget(self.btn_zoom_out, 1, 0, 1, 1)

        self.btn_zoom_in = QtWidgets.QPushButton(self.centralwidget)
        self.btn_zoom_in.setMaximumSize(QtCore.QSize(25, 25))
        self.btn_zoom_in.setObjectName("btn_zoom_in")
        self.btn_zoom_in.setEnabled(False)
        self.gridLayout_2.addWidget(self.btn_zoom_in, 1, 1, 1, 1)

        self.verticalLayout.addLayout(self.gridLayout_2)
        self.verticalLayout_5.addLayout(self.verticalLayout)

        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")

        self.verticalLayout_5.addWidget(self.line_4)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")

        self.rbtn_normal = QtWidgets.QRadioButton(self.centralwidget)
        self.rbtn_normal.setChecked(True)
        self.rbtn_normal.setObjectName("rbtn_normal")
        self.rbtn_normal.setEnabled(False)
        self.gridLayout_3.addWidget(self.rbtn_normal, 2, 1, 1, 1)

        self.rbtn_sepia = QtWidgets.QRadioButton(self.centralwidget)
        self.rbtn_sepia.setChecked(False)
        self.rbtn_sepia.setObjectName("rbtn_sepia")
        self.rbtn_sepia.setEnabled(False)
        self.gridLayout_3.addWidget(self.rbtn_sepia, 1, 0, 1, 1)
        
        self.rbtn_gray = QtWidgets.QRadioButton(self.centralwidget)
        self.rbtn_gray.setObjectName("rbtn_gray")
        self.rbtn_gray.setEnabled(False)
        self.gridLayout_3.addWidget(self.rbtn_gray, 1, 1, 1, 1)
        
        self.rbtn_negative = QtWidgets.QRadioButton(self.centralwidget)
        self.rbtn_negative.setObjectName("rbtn_negative")
        self.rbtn_negative.setEnabled(False)
        self.gridLayout_3.addWidget(self.rbtn_negative, 2, 0, 1, 1)

        self.rbtn_black_white = QtWidgets.QRadioButton(self.centralwidget)
        self.rbtn_black_white.setObjectName("rbtn_black_white")
        self.rbtn_black_white.setEnabled(False)
        self.gridLayout_3.addWidget(self.rbtn_black_white, 3, 0, 1, 1)

        self.label_effects = QtWidgets.QLabel(self.centralwidget)
        self.label_effects.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_effects.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_effects.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_effects.setTextFormat(QtCore.Qt.AutoText)
        self.label_effects.setAlignment(QtCore.Qt.AlignCenter)
        self.label_effects.setWordWrap(False)
        self.label_effects.setOpenExternalLinks(False)
        self.label_effects.setObjectName("label_effects")
        self.label_effects.setEnabled(False)
        self.gridLayout_3.addWidget(self.label_effects, 0, 0, 1, 2)

        self.verticalLayout_5.addLayout(self.gridLayout_3)
        
        self.gridLayout_4.addLayout(self.verticalLayout_5, 0, 1, 1, 1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")

        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(20)
        self.verticalLayout_3.setObjectName("verticalLayout_3")

        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setSpacing(27)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")

        self.horizontalLayout_7.addWidget(self.label_5)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_7.addWidget(self.lineEdit_3)

        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.line_21 = QtWidgets.QFrame(self.centralwidget)
        self.line_21.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_21.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_21.setObjectName("line_21")
        self.verticalLayout_3.addWidget(self.line_21)

        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setSpacing(27)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")

        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_8.addWidget(self.label_7)

        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.horizontalLayout_8.addWidget(self.lineEdit_4)

        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        self.line_20 = QtWidgets.QFrame(self.centralwidget)
        self.line_20.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_20.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_20.setObjectName("line_20")
        self.verticalLayout_3.addWidget(self.line_20)

        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setSpacing(22)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")

        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_9.addWidget(self.label_8)

        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.horizontalLayout_9.addWidget(self.lineEdit_6)

        self.verticalLayout_3.addLayout(self.horizontalLayout_9)
        self.line_13 = QtWidgets.QFrame(self.centralwidget)
        self.line_13.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_13.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_13.setObjectName("line_13")
        self.verticalLayout_3.addWidget(self.line_13)

        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setSpacing(44)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")

        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_11.addWidget(self.label_9)

        self.checkBox_3 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_3.setObjectName("checkBox_3")
        self.horizontalLayout_11.addWidget(self.checkBox_3)

        self.checkBox_4 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_4.setObjectName("checkBox_4")
        self.horizontalLayout_11.addWidget(self.checkBox_4)

        self.horizontalLayout_10.addLayout(self.horizontalLayout_11)
        self.verticalLayout_3.addLayout(self.horizontalLayout_10)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.line_22 = QtWidgets.QFrame(self.centralwidget)
        self.line_22.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_22.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_22.setObjectName("line_22")
        self.verticalLayout_4.addWidget(self.line_22)

        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")

        self.btn_Ok = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Ok.setMinimumSize(QtCore.QSize(60, 50))
        self.btn_Ok.setMaximumSize(QtCore.QSize(50, 50))
        self.btn_Ok.setObjectName("btn_Ok")
        self.horizontalLayout_12.addWidget(self.btn_Ok)

        self.btn_Cancel = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Cancel.setMinimumSize(QtCore.QSize(60, 50))
        self.btn_Cancel.setMaximumSize(QtCore.QSize(50, 50))
        self.btn_Cancel.setObjectName("btn_Cancel")
        self.horizontalLayout_12.addWidget(self.btn_Cancel)

        self.verticalLayout_4.addLayout(self.horizontalLayout_12)
        self.gridLayout_4.addLayout(self.verticalLayout_4, 0, 3, 1, 1)
        self.line_15 = QtWidgets.QFrame(self.centralwidget)
        self.line_15.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_15.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_15.setObjectName("line_15")
        self.gridLayout_4.addWidget(self.line_15, 0, 4, 1, 1)

        self.line_14 = QtWidgets.QFrame(self.centralwidget)
        self.line_14.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_14.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_14.setObjectName("line_14")
        self.gridLayout_4.addWidget(self.line_14, 0, 0, 1, 1)

        self.line_16 = QtWidgets.QFrame(self.centralwidget)
        self.line_16.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_16.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_16.setObjectName("line_16")
        self.gridLayout_4.addWidget(self.line_16, 0, 2, 1, 1)

        self.line_11 = QtWidgets.QFrame(self.centralwidget)
        self.line_11.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.gridLayout_4.addWidget(self.line_11, 1, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_rsc.setText(_translate("MainWindow", "Set avatar"))
        self.label_size_zoom.setText(_translate("MainWindow", "Size zoom"))
        self.btn_zoom_out.setText(_translate("MainWindow", "-"))
        self.btn_zoom_in.setText(_translate("MainWindow", "+"))
        self.rbtn_normal.setText(_translate("MainWindow", "Normal"))
        self.rbtn_sepia.setText(_translate("MainWindow", "Sepia"))
        self.rbtn_gray.setText(_translate("MainWindow", "Gray"))
        self.rbtn_negative.setText(_translate("MainWindow", "Negative"))
        self.rbtn_black_white.setText(_translate("MainWindow", "Black-white"))
        self.label_effects.setText(_translate("MainWindow", "Efects"))
        self.label_5.setText(_translate("MainWindow", "LOGIN:"))
        self.label_7.setText(_translate("MainWindow", "NAME:"))
        self.label_8.setText(_translate("MainWindow", "E-MAIL:"))
        self.label_9.setText(_translate("MainWindow", "SEX:"))
        self.checkBox_3.setText(_translate("MainWindow", "male"))
        self.checkBox_4.setText(_translate("MainWindow", "female"))
        self.btn_Ok.setText(_translate("MainWindow", "OK"))
        self.btn_Cancel.setText(_translate("MainWindow", "CANCEL"))

