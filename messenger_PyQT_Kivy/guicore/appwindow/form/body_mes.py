# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'b_test.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets



class Ui_MainWindow_Body(object):

    def setupUi_body(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 622)
        MainWindow.setMinimumSize(QtCore.QSize(800, 622))
        MainWindow.setMaximumSize(QtCore.QSize(800, 622))

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(800, 600))
        self.centralwidget.setMaximumSize(QtCore.QSize(800, 16777215))
        self.centralwidget.setObjectName("centralwidget")

        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setSpacing(10)
        self.gridLayout_2.setObjectName("gridLayout_2")

        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")

        self.gridLayout_2.addWidget(self.line_3, 0, 3, 1, 1)
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")

        self.gridLayout_2.addWidget(self.line_4, 0, 5, 1, 1)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.gridLayout_2.addWidget(self.line, 1, 4, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")

        self.display = QtWidgets.QTextEdit(self.centralwidget)
        self.display.setMinimumSize(QtCore.QSize(435, 450))
        self.display.setMaximumSize(QtCore.QSize(440, 460))
        self.display.setObjectName("display")
        self.display.setReadOnly(True)

        self.gridLayout.addWidget(self.display, 0, 0, 1, 1)
        self.line_10 = QtWidgets.QFrame(self.centralwidget)
        self.line_10.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")

        self.gridLayout.addWidget(self.line_10, 1, 0, 1, 1)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")

        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.btn_bold = QtWidgets.QPushButton(self.centralwidget)
        self.btn_bold.setMaximumSize(QtCore.QSize(24, 24))
        self.btn_bold.setStyleSheet("#btn_bold {background-image: url(src/icon/b.jpg); background-position: center}")
        self.btn_bold.setShortcut('Ctrl+b')
        self.btn_bold.setText("")
        self.btn_bold.setObjectName("btn_bold")
        self.horizontalLayout_2.addWidget(self.btn_bold)

        self.btn_italic = QtWidgets.QPushButton(self.centralwidget)
        self.btn_italic.setMaximumSize(QtCore.QSize(24, 24))
        self.btn_italic.setStyleSheet("#btn_italic {background-image: url(src/icon/i.jpg); background-position: center}")
        self.btn_italic.setShortcut('Ctrl+i')
        self.btn_italic.setText("")
        self.btn_italic.setObjectName("btn_italic")
        self.horizontalLayout_2.addWidget(self.btn_italic)

        self.btn_underlined = QtWidgets.QPushButton(self.centralwidget)
        self.btn_underlined.setMaximumSize(QtCore.QSize(24, 24))
        self.btn_underlined.setStyleSheet("#btn_underlined {background-image: url(src/icon/u.jpg); background-position: center}")
        self.btn_underlined.setShortcut('Ctrl+u')
        self.btn_underlined.setText("")
        self.btn_underlined.setObjectName("btn_underlined")
        self.horizontalLayout_2.addWidget(self.btn_underlined)

        self.btn_smile_1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_smile_1.setMaximumSize(QtCore.QSize(24, 24))
        self.btn_smile_1.setStyleSheet("#btn_smile_1 {border:none; background-image: url(src/smile/ab.gif);background-repeat: no-repeat; background-position: center;}")
        self.btn_smile_1.setText("")
        self.btn_smile_1.setObjectName("btn_smile_1")
        self.horizontalLayout_2.addWidget(self.btn_smile_1)

        self.btn_smile_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_smile_2.setMaximumSize(QtCore.QSize(24, 24))
        self.btn_smile_2.setStyleSheet("#btn_smile_2 {border:none; background-image: url(src/smile/ac.gif); background-repeat: no-repeat; background-position: center;}")
        self.btn_smile_2.setText("")
        self.btn_smile_2.setObjectName("btn_smile_2")
        self.horizontalLayout_2.addWidget(self.btn_smile_2)

        self.btn_smile_3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_smile_3.setMaximumSize(QtCore.QSize(24, 24))
        self.btn_smile_3.setStyleSheet("#btn_smile_3 {border:none; background-image: url(src/smile/ai.gif); background-repeat: no-repeat; background-position: center;}")
        self.btn_smile_3.setText("")
        self.btn_smile_3.setObjectName("btn_smile_3")
        self.horizontalLayout_2.addWidget(self.btn_smile_3)

        # self.bnt_7 = QtWidgets.QPushButton(self.centralwidget)
        # self.bnt_7.setMaximumSize(QtCore.QSize(24, 24))
        # self.bnt_7.addAction(self.bold)
        # self.bnt_7.setText("")
        # self.bnt_7.setObjectName("bnt_7")
        # self.horizontalLayout_2.addWidget(self.bnt_7)

        # self.bnt_8 = QtWidgets.QPushButton(self.centralwidget)
        # self.bnt_8.setMaximumSize(QtCore.QSize(24, 24))
        # self.bnt_8.setText("")
        # self.bnt_8.setObjectName("bnt_8")
        # self.horizontalLayout_2.addWidget(self.bnt_8)

        # self.bnt_9 = QtWidgets.QPushButton(self.centralwidget)
        # self.bnt_9.setMaximumSize(QtCore.QSize(24, 24))
        # self.bnt_9.setText("")
        # self.bnt_9.setObjectName("bnt_9")
        # self.horizontalLayout_2.addWidget(self.bnt_9)

        # self.bnt_10 = QtWidgets.QPushButton(self.centralwidget)
        # self.bnt_10.setMaximumSize(QtCore.QSize(24, 24))
        # self.bnt_10.setText("")
        # self.bnt_10.setObjectName("bnt_10")
        # self.horizontalLayout_2.addWidget(self.bnt_10)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.input = QtWidgets.QTextEdit(self.centralwidget)
        self.input.setPlaceholderText('Input messege')
        self.input.setMinimumSize(QtCore.QSize(360, 45))
        self.input.setMaximumSize(QtCore.QSize(400, 50))
        self.input.setObjectName("input")

        self.verticalLayout.addWidget(self.input)

        self.gridLayout_4.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.btn = QtWidgets.QPushButton(self.centralwidget)
        self.btn.setMinimumSize(QtCore.QSize(48, 48))
        self.btn.setMaximumSize(QtCore.QSize(48, 48))
        self.btn.setStyleSheet("#btn {border: none; background-image: url(src/img/b1.png);}\n"
"#btn:pressed {border: none; background-image: url(src/img/b2.png);}")
        self.btn.setText("")
        self.btn.setObjectName("btn")

        self.gridLayout_4.addWidget(self.btn, 0, 1, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_4, 2, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 5, 1, 1)

        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")

        self.gridLayout_2.addWidget(self.line_2, 1, 0, 1, 1)
        self.verticalScrollBar = QtWidgets.QScrollBar(self.centralwidget)
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")

        self.gridLayout_2.addWidget(self.verticalScrollBar, 1, 1, 1, 1)

        self.display_list = QtWidgets.QTextEdit(self.centralwidget)
        self.display_list.setPlainText('Contact list: ')
        self.display_list.setObjectName("display_list")
        self.display_list.setReadOnly(True)
        self.gridLayout_2.addWidget(self.display_list, 1, 3, 1, 1)
        
        self.line_9 = QtWidgets.QFrame(self.centralwidget)
        self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")

        self.gridLayout_2.addWidget(self.line_9, 2, 5, 1, 1)
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")

        self.gridLayout_2.addWidget(self.line_5, 1, 6, 1, 1)
        self.line_7 = QtWidgets.QFrame(self.centralwidget)
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")

        self.gridLayout_2.addWidget(self.line_7, 2, 3, 1, 1)
        self.line_8 = QtWidgets.QFrame(self.centralwidget)
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")

        self.gridLayout_2.addWidget(self.line_8, 2, 4, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        self.menuSettings = QtWidgets.QMenu(self.menuBar)
        self.menuSettings.setObjectName("menuSettings")
        self.menuReference = QtWidgets.QMenu(self.menuBar)
        self.menuReference.setObjectName("menuReference")

        MainWindow.setMenuBar(self.menuBar)

        self.actionAdd_contact = QtWidgets.QAction(MainWindow)
        self.actionAdd_contact.setObjectName("actionAdd_contact")
        self.actionEdit_contact = QtWidgets.QAction(MainWindow)
        self.actionEdit_contact.setObjectName("actionEdit_contact")
        self.actionContact_list = QtWidgets.QAction(MainWindow)
        self.actionContact_list.setObjectName("actionContact_list")
        self.actionUser_profile = QtWidgets.QAction(MainWindow)
        self.actionUser_profile.setObjectName("actionUser_profile")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionvideo_and_audio_settings = QtWidgets.QAction(MainWindow)
        self.actionvideo_and_audio_settings.setObjectName("actionvideo_and_audio_settings")
        self.actionAbout_as = QtWidgets.QAction(MainWindow)
        self.actionAbout_as.setObjectName("actionAbout_as")
        
        self.menuFile.addAction(self.actionAdd_contact)
        self.menuFile.addAction(self.actionEdit_contact)
        self.menuFile.addAction(self.actionContact_list)
        self.menuFile.addAction(self.actionUser_profile)
        self.menuFile.addAction(self.actionExit)
        self.menuSettings.addAction(self.actionvideo_and_audio_settings)
        self.menuReference.addAction(self.actionAbout_as)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuSettings.menuAction())
        self.menuBar.addAction(self.menuReference.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
        self.menuReference.setTitle(_translate("MainWindow", "Reference"))
        self.actionAdd_contact.setText(_translate("MainWindow", "Add contact"))
        self.actionEdit_contact.setText(_translate("MainWindow", "Edit contact"))
        self.actionContact_list.setText(_translate("MainWindow", "Contact list"))
        self.actionUser_profile.setText(_translate("MainWindow", "User profile"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionvideo_and_audio_settings.setText(_translate("MainWindow", "video and audio settings"))
        self.actionAbout_as.setText(_translate("MainWindow", "About as"))

